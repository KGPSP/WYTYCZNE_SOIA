# Wytyczne SOiA

Publiczne repozytorium wytycznych organizacyjnych, technicznych i sprzętowych systemu ostrzegania i alarmowania. Aktualne wydanie dokumentacyjne: **projekt 0.5 z 10 września 2026 r.**

## Zawartość

1. **[Podręcznik SOiA — pełna wersja](PODRECZNIK_v2.md)** — komplet wytycznych w jednym pliku.
2. **[Podręcznik SOiA — wersja rozdzielona](PODRECZNIK_v2_ROZDZIELONY.md)** — nawigacja po [dwunastu załącznikach](zalaczniki/) o tej samej treści.
3. **[Platforma sterownika i provisioning KG PSP](PLATFORMA_KG_PSP.md)** — OrchestraOS, Yocto, budowa obrazu dla płyty, tożsamość i rejestracja w Orchestra.
4. **[Profil 1.5 dla kompaktowych sterowników](PROFIL_1_5.md)** — mniejsze wyposażenie z lokalnym audio, przy zachowaniu wspólnej platformy i bezpieczeństwa.
5. **[Zmiany wersji 0.5](ZMIANY_v0.5.md)** — zakres korekt i ciągłość identyfikatorów wymagań oraz prób.

Dokumenty pozostają projektem wytycznych. Nie poświadczają podpisania aktu, wdrożenia wszystkich planowanych funkcji ani odbioru konkretnego modelu. Materiały PDF nie są dołączane do tego wydania.

## Strona

[Otwórz Wytyczne SOiA w GitHub Pages](https://kgpsp.github.io/WYTYCZNE_SOIA/)

GitHub Pages publikuje to samo wydanie 0.5: podręcznik, dwanaście załączników, profil 1.5 i platformę KG PSP.

## Aktualizacja dokumentacji

Źródłem treści są pliki Markdown w katalogu głównym i `zalaczniki/`. Po ich zmianie uruchom `python scripts/sync_pages.py`, aby odświeżyć wersję strony. Kontrola CI sprawdza zgodność kopii oraz buduje witrynę przez `mkdocs build --strict`. Plików PDF nie kopiuje się do strony.
