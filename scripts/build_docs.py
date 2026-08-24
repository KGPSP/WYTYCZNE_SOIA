from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CALLOUT_RE = re.compile(
    r"^> \[!(warning|caution|important|note)\](?:[ \t]+(.*))?$",
    re.IGNORECASE | re.MULTILINE,
)
CALLOUT_TYPES = {
    "warning": "warning",
    "caution": "danger",
    "important": "info",
    "note": "note",
}
TITLE_RE = re.compile(r'^tytuł:\s*["\']?(.*?)["\']?\s*$', re.MULTILINE)
ATTACHMENT_LINK_RE = re.compile(r"\]\((?:\./)?zalaczniki/([^\s)#]+\.md)(?:#[^)]*)?\)")

DOCS_MAIN_FRONT_MATTER = """---
title: "Podręcznik SOiA"
description: "Zasady podłączania syren alarmowych i innych urządzeń do SOiA"
author: "Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej"
date: 2026-08-23
version: "0.4"
---

"""

PUBLICATION_INFORMATION = """<a id="poczatek"></a>
<div class="institutional-masthead" role="banner" aria-label="Instytucje związane z publikacją">
  <img class="institutional-logo logo-psp" src="assets/images/logo-psp.svg" alt="Państwowa Straż Pożarna">
  <img class="institutional-logo logo-mswia" src="assets/images/logo-mswia.svg" alt="Ministerstwo Spraw Wewnętrznych i Administracji">
  <img class="institutional-logo logo-olioc" src="assets/images/logo-olioc.svg" alt="Ochrona ludności i obrona cywilna">
</div>

<div class="publication-information" aria-label="Informacje o publikacji">
  <div class="document-repository">
    <p><strong>Repozytorium wszystkich publicznych dokumentów SOiA:</strong>
    <a href="https://github.com/KGPSP/WYTYCZNE_SOIA">KGPSP/WYTYCZNE_SOIA</a>.</p>
  </div>

  <div class="ai-disclosure" role="note" aria-label="Informacja o wykorzystaniu sztucznej inteligencji">
  <img src="assets/images/partially-ai-modified-eu.png" alt="PARTIALLY AI-MODIFIED — oficjalne oznaczenie UE dla treści częściowo zmodyfikowanej z wykorzystaniem AI">
    <div class="ai-disclosure__content">
      <strong>Partially AI-Modified — informacja o wykorzystaniu sztucznej inteligencji</strong>
      <p>Materiał zawiera treść pierwotnie opracowaną przez człowieka, która została częściowo zmodyfikowana i zredagowana z wykorzystaniem narzędzi sztucznej inteligencji. Treść podlegała przeglądowi i kontroli redakcyjnej człowieka, a odpowiedzialność redakcyjną za publikację ponosi wydawca.</p>
      <p>Zastosowano wariant <a href="https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content">Partially AI-Modified z zestawu ikon UE</a>, z uwzględnieniem <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj">art. 50 rozporządzenia (UE) 2024/1689</a>. Ikona jest dobrowolnym oznaczeniem i sama w sobie nie stanowi potwierdzenia zgodności prawnej ani merytorycznej dokumentu.</p>
    </div>
  </div>
</div>

"""


def strip_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError("Niezamknięty front matter")
    return text[4:closing], text[closing + 5 :].lstrip("\n")


def convert_callouts(text: str) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        match = CALLOUT_RE.match(line.rstrip("\r\n"))
        if not match:
            output.append(line)
            index += 1
            continue

        source_type = match.group(1).lower()
        title = (match.group(2) or source_type.title()).replace("\\", "\\\\").replace(
            '"', '\\"'
        )
        output.append(f'!!! {CALLOUT_TYPES[source_type]} "{title}"\n\n')
        index += 1
        while index < len(lines) and lines[index].startswith(">"):
            body = lines[index][1:]
            if body.startswith(" "):
                body = body[1:]
            output.append(f"    {body}")
            index += 1
    return "".join(output)


def title_from_front_matter(front_matter: str, fallback: str) -> str:
    match = TITLE_RE.search(front_matter)
    return match.group(1) if match else fallback


def docs_front_matter(title: str) -> str:
    safe_title = title.replace('"', '\\"')
    return f'---\ntitle: "{safe_title}"\n---\n\n'


def convert_attachment_links(text: str) -> str:
    return text.replace(
        "../PODRECZNIK_v2.md#spis-treści",
        "../index.md#spis-tresci",
    )


def build(root: Path) -> dict[str, int]:
    source = root / "PODRECZNIK_v2.md"
    attachments_dir = root / "zalaczniki"
    if not source.is_file():
        raise FileNotFoundError(f"Brak pliku źródłowego: {source}")
    attachments = sorted(attachments_dir.glob("*.md"))
    if not attachments:
        raise FileNotFoundError(f"Brak załączników w katalogu: {attachments_dir}")

    source_text = source.read_text(encoding="utf-8")
    available_names = {path.name for path in attachments}
    referenced_names = set(ATTACHMENT_LINK_RE.findall(source_text))
    missing_names = sorted(referenced_names - available_names)
    if missing_names:
        raise FileNotFoundError(
            "Brak plików załączników wskazanych w podręczniku: " + ", ".join(missing_names)
        )
    unlinked_names = sorted(available_names - referenced_names)
    if unlinked_names:
        raise ValueError(
            "Załączniki pominięte w głównym indeksie podręcznika: "
            + ", ".join(unlinked_names)
        )

    docs = root / "docs"
    docs_attachments = docs / "zalaczniki"
    docs_attachments.mkdir(parents=True, exist_ok=True)

    _, main_body = strip_front_matter(source_text)
    index = DOCS_MAIN_FRONT_MATTER + PUBLICATION_INFORMATION + convert_callouts(main_body)
    (docs / "index.md").write_text(index, encoding="utf-8")

    callouts = len(CALLOUT_RE.findall(main_body))
    for attachment_source in attachments:
        front_matter, body = strip_front_matter(attachment_source.read_text(encoding="utf-8"))
        title = title_from_front_matter(front_matter, attachment_source.stem)
        callouts += len(CALLOUT_RE.findall(body))
        rendered = docs_front_matter(title) + convert_callouts(convert_attachment_links(body))
        (docs_attachments / attachment_source.name).write_text(rendered, encoding="utf-8")

    report = {"attachments": len(attachments), "callouts": callouts}
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Buduje rozdzieloną dokumentację MkDocs SOiA")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    print(json.dumps(build(arguments.root.resolve()), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
