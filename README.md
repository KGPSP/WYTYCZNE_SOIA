# Wytyczne SOiA

Publiczne repozytorium wytycznych organizacyjnych, technicznych i sprzętowych systemu ostrzegania i alarmowania. Aktualne wydanie podręcznika: **projekt 0.5 z 10 września 2026 r.**

## Zawartość

1. **[Podręcznik SOiA — pełna wersja](PODRECZNIK_v2.md)** — komplet wytycznych w jednym pliku.
2. **[Podręcznik SOiA — wersja rozdzielona](PODRECZNIK_v2_ROZDZIELONY.md)** — nawigacja po [dwunastu załącznikach](zalaczniki/) o tej samej treści.
3. **[Platforma sterownika i provisioning KG PSP](PLATFORMA_KG_PSP.md)** — OrchestraOS, Yocto, budowa obrazu dla płyty, tożsamość i rejestracja w Orchestra.
4. **[Profil 1.5 dla kompaktowych sterowników](PROFIL_1_5.md)** — mniejsze wyposażenie z lokalnym audio, przy zachowaniu wspólnej platformy i bezpieczeństwa.
5. **[Zmiany wersji 0.5](ZMIANY_v0.5.md)** — zakres korekt i ciągłość identyfikatorów wymagań oraz prób.
6. **[Instrukcje i materiały robocze — dokumenty PDF](instrukcje-i-materialy-robocze/README.md)** — 15 dokumentów dotyczących montażu, integracji syren, wymagań, konfiguracji i planowania kosztów; wykaz zawiera wersje i opisy.

Podręcznik i powiązane wytyczne Markdown pozostają projektem. Nie poświadczają podpisania aktu, wdrożenia wszystkich planowanych funkcji ani odbioru konkretnego modelu. Osobny pakiet PDF ma własne numery wersji oraz oznaczenie **AKCEPTACJA - BIŁ KGPSP**; opisano go w dziale instrukcji i materiałów roboczych.

## Strona

[Otwórz Wytyczne SOiA w GitHub Pages](https://kgpsp.github.io/WYTYCZNE_SOIA/)

GitHub Pages publikuje to samo wydanie 0.5: podręcznik, dwanaście załączników, profil 1.5 i platformę KG PSP, a także [komplet 15 dokumentów PDF do pobrania](https://kgpsp.github.io/WYTYCZNE_SOIA/DOKUMENTY_PDF/).

## Aktualizacja dokumentacji

Źródłem treści witryny są pliki Markdown w katalogu głównym i `zalaczniki/`. Po ich zmianie uruchom `python scripts/sync_pages.py`, aby odświeżyć wersję strony. Kontrola CI sprawdza zgodność kopii oraz buduje witrynę przez `mkdocs build --strict`. Pakiet PDF jest udostępniany w repozytorium i na stronie. Skrypt synchronizacji kopiuje PDF-y z `instrukcje-i-materialy-robocze/pdf/` do `docs/pdf/` bez zmiany zawartości, a kontrola CI sprawdza zgodność kopii.

Przy aktualizacji zestawu odśwież oba spisy: `instrukcje-i-materialy-robocze/README.md` oraz [listę do pobrania](DOKUMENTY_PDF.md), a także wykaz rozmiarów i sum SHA-256 w `docs/pdf/manifest.json`. Następnie uruchom synchronizację strony.
