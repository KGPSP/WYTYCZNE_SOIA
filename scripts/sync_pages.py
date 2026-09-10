#!/usr/bin/env python3
"""Synchronize Pages Markdown and PDF copies from canonical repository sources."""
from pathlib import Path
import argparse
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "PODRECZNIK_v2.md": "index.md",
    "PODRECZNIK_v2_ROZDZIELONY.md": "PODRECZNIK_v2_ROZDZIELONY.md",
    "PLATFORMA_KG_PSP.md": "PLATFORMA_KG_PSP.md",
    "PROFIL_1_5.md": "PROFIL_1_5.md",
    "ZMIANY_v0.5.md": "ZMIANY_v0.5.md",
    "DOKUMENTY_PDF.md": "DOKUMENTY_PDF.md",
}


def page_text(source: str) -> str:
    text = (ROOT / source).read_text(encoding="utf-8")

    def link(match):
        value = match.group(1)
        url = urlsplit(value)
        if url.scheme or value.startswith("//"):
            return match.group(0)
        path = re.sub(r"(^|/)(?:README|PODRECZNIK_v2)\.md$", r"\1index.md", url.path)
        if path.startswith("docs/pdf/"):
            path = path.removeprefix("docs/")
        # GitHub keeps Polish letters in heading IDs; MkDocs uses ASCII slugs.
        fragment = unicodedata.normalize("NFKD", unquote(url.fragment)).encode("ascii", "ignore").decode()
        return "](" + urlunsplit((url.scheme, url.netloc, path, url.query, fragment)) + ")"

    text = re.sub(r"\]\(([^)]+)\)", link, text)
    # Python-Markdown requires four spaces for the nested lists used by GitHub.
    in_fence = False
    lines = []
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"^  [-*+] ", line):
            line = "  " + line
        lines.append(line)
    text = "\n".join(lines) + "\n"
    if source == "PODRECZNIK_v2.md":
        header = (ROOT / "scripts/pages-masthead.html").read_text(encoding="utf-8")
        meta = re.match(r"\A---\n.*?\n---\n", text, re.S)
        assert meta, "Missing handbook metadata"
        text = text[:meta.end()] + "\n" + header + "\n" + text[meta.end():].lstrip()
    notice = f"<!-- Generated from {source}; run python scripts/sync_pages.py. -->\n"
    meta = re.match(r"\A---\n.*?\n---\n", text, re.S)
    if meta:
        text = text[:meta.end()] + "\n" + notice + text[meta.end():]
    else:
        text = notice + text
    return text.rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if published sources differ from canonical Markdown")
    args = parser.parse_args()
    sources = dict(SOURCES)
    attachments = sorted((ROOT / "zalaczniki").glob("Z*-*.md"))
    if len(attachments) != 12:
        raise SystemExit("Expected exactly twelve canonical attachments")
    sources.update({str(path.relative_to(ROOT)): str(path.relative_to(ROOT)) for path in attachments})
    differences = []
    for source, destination in sources.items():
        target = ROOT / "docs" / destination
        expected = page_text(source)
        if not target.exists() or target.read_text(encoding="utf-8") != expected:
            differences.append(str(target.relative_to(ROOT)))
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(expected, encoding="utf-8")
    pdf_sources = sorted((ROOT / "instrukcje-i-materialy-robocze/pdf").glob("*.pdf"))
    if not pdf_sources:
        raise SystemExit("Missing canonical PDF package")
    pdf_target = ROOT / "docs/pdf"
    stale = {path.name for path in pdf_target.glob("*.pdf")} - {path.name for path in pdf_sources}
    if stale:
        raise SystemExit("Remove obsolete Pages PDF copies: " + ", ".join(sorted(stale)))
    for source in pdf_sources:
        target = pdf_target / source.name
        expected = source.read_bytes()
        if not target.exists() or target.read_bytes() != expected:
            differences.append(str(target.relative_to(ROOT)))
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(expected)
    if args.check and differences:
        print("Pages sources are out of sync:\n" + "\n".join(differences), file=sys.stderr)
        raise SystemExit(1)
    print(f"Pages {'verified' if args.check else 'synchronized'}: {len(sources)} Markdown documents; {len(pdf_sources)} PDFs; {len(differences)} differences")


if __name__ == "__main__":
    main()
