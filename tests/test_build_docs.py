from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = REPOSITORY / "scripts" / "build_docs.py"


class BuildDocsTests(unittest.TestCase):
    def test_build_creates_a_separate_page_for_each_attachment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            attachments = root / "zalaczniki"
            attachments.mkdir()
            (root / "PODRECZNIK_v2.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    tytuł: "Podręcznik testowy"
                    ---

                    # Podręcznik testowy

                    [Załącznik nr 1](zalaczniki/Z1-TEST.md)

                    > [!important] Stan docelowy
                    > Treść komunikatu.
                    """
                ),
                encoding="utf-8",
            )
            (attachments / "Z1-TEST.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    tytuł: "Załącznik nr 1 — Test"
                    ---

                    [← Powrót do podręcznika](../PODRECZNIK_v2.md#spis-treści)

                    # Załącznik nr 1 — Test

                    ## Treść załącznika

                    > [!note] Informacja
                    > Zachowana treść.
                    """
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(BUILD_SCRIPT), "--root", str(root)],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            index = (root / "docs" / "index.md").read_text(encoding="utf-8")
            attachment = (root / "docs" / "zalaczniki" / "Z1-TEST.md").read_text(
                encoding="utf-8"
            )
            self.assertIn('class="institutional-masthead"', index)
            self.assertIn('!!! info "Stan docelowy"', index)
            self.assertNotIn("Treść załącznika", index)
            self.assertIn("# Załącznik nr 1 — Test", attachment)
            self.assertIn("(../index.md#spis-tresci)", attachment)
            self.assertNotIn("PODRECZNIK_v2.md", attachment)
            self.assertIn('!!! note "Informacja"', attachment)
            self.assertIn("Zachowana treść.", attachment)
            self.assertNotIn("> [!", index + attachment)
            self.assertEqual(report["callouts"], 2)

    def test_build_rejects_a_link_to_a_missing_attachment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            attachments = root / "zalaczniki"
            attachments.mkdir()
            (root / "PODRECZNIK_v2.md").write_text(
                "# Podręcznik\n\n[Brakujący załącznik](zalaczniki/Z2-BRAK.md)\n",
                encoding="utf-8",
            )
            (attachments / "Z1-TEST.md").write_text(
                "# Załącznik nr 1 — Test\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(BUILD_SCRIPT), "--root", str(root)],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Z2-BRAK.md", result.stderr)

    def test_build_rejects_an_attachment_missing_from_the_main_index(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            attachments = root / "zalaczniki"
            attachments.mkdir()
            (root / "PODRECZNIK_v2.md").write_text(
                "# Podręcznik bez odnośnika\n",
                encoding="utf-8",
            )
            (attachments / "Z1-POMINIETY.md").write_text(
                "# Załącznik nr 1 — Pominięty\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(BUILD_SCRIPT), "--root", str(root)],
                text=True,
                capture_output=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Z1-POMINIETY.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
