---
tytuł: "Podręcznik SOiA"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

# Podręcznik SOiA

## Zasady podłączania syren alarmowych i innych urządzeń

**Wersja dokumentacyjna 0.5 · 10 września 2026 r. · Projekt wytycznych**

Dokument opisuje wymagania przygotowania, przyłączenia i utrzymania sterowników w zarządzanym systemie KG PSP. Decyzja o alarmowaniu wynika z właściwej procedury; system dostarcza polecenie, a aplikacja KG PSP weryfikuje je i wykonuje na właściwym torze. Sprzęt różnych wykonawców współpracuje przez uzgodnioną platformę i interfejsy.

Najważniejsze uzupełnienia tej wersji to **profil 1.5 dla urządzeń kompaktowych** oraz **OrchestraOS, Yocto i provisioning KG PSP**. Parametry dostosowuje się do funkcji i zakresu dostawy. Mniejsza liczba portów nie oznacza słabszej autoryzacji, historii, nadzoru lub ochrony kluczy.

## Jak korzystać z wytycznych

| Potrzeba | Punkt wejścia |
| --- | --- |
| Cel i odpowiedzialność organizacyjna | Z2 |
| Wspólny system bazowy i dołączanie urządzeń | [Platforma KG PSP](PLATFORMA_KG_PSP.md), następnie Z3 i Z7 |
| Mały sterownik i dobór wyposażenia | [Profil 1.5](PROFIL_1_5.md) i macierz Z3 |
| Sygnały i wykonanie | Z4 i Z5 |
| Feed, rejestracja, SMS i TETRA | Z6–Z8 |
| Konfiguracja i odbiór | Z9 i Z10 |
| Zakup i podstawa prawna | Z11 i Z12 |

## Zakres wersji i źródła rozstrzygające

Klasa I obejmuje wspólny rdzeń, 1.5 profil kompaktowy z audio, II profil rozszerzony z audio, a III lokalny TTS. Oznaczenia D/P określają zakres dostawy lub adresata. Nie są to wersje protokołu ani `deviceClass` komendy.

Publiczny poziom 0 pozostaje otwartym odczytem. Zgodność nowej platformy KG PSP wymaga właściwego obrazu Yocto/OrchestraOS, tożsamości, rejestracji i odbioru. Odczyt feedu, online w Managerze i fizyczna emisja to odrębne etapy.

W fazie 2026–2028 zestawy mają GSM/LTE, z SMS jako zapasem i możliwością dodatkowego IP przez Ethernet/Wi-Fi. Po tej fazie podstawowym kanałem poleceń ma być odebrana TETRA, z aktywnym zapasem GSM. Terminy i warunki przełączenia określa plan lokalizacji.

| Rodzaj zapisu | Znaczenie |
| --- | --- |
| Wymaganie W-* | Warunek w wybranej klasie/profilu i zakresie. |
| Scenariusz S-* | Próba właściwej funkcji i jej oczekiwany wynik. |
| Kontrakt aplikacji i metadane API | Obsługiwana wersja, klasy odbiorców i kody; nie są listą portów sprzętu. |
| Pakiet i karta konfiguracji | Wydania, zasoby, parametry oraz uprawnienia konkretnego modelu i egzemplarza. |
| Przepis prawa | Podstawa prawna we właściwym zakresie; dokument techniczny nie nadaje nowych kompetencji. |

Odczyt 10.09.2026 potwierdził publiczny profil IoT `0.1` i słownik `2026.1`. Funkcje planowane, w tym dodatkowe kody, TTS i integracja TETRA, wymagają osobnego kontraktu oraz odbioru. Publikacja wytycznych nie jest wdrożeniem aplikacji.

Dokument pozostaje ogólny: nie zawiera pinoutów konkretnych syren, numerów abonenckich, sekretów ani konfiguracji produkcyjnych. Nazwy OrchestraOS/Orchestra, Yocto i RAUC identyfikują środowisko integracji KG PSP; modele urządzeń i wykonawcy nie są narzucone. Pliki PDF materiałów źródłowych nie są dołączane do tego wydania.

Opis i diagram nie zastępują wymagania, ale wymaganie zakupowe również nie dowodzi istniejącej funkcji API. Sprzeczność pomiędzy zakresem zamówienia a dostępnym kontraktem trzeba rozstrzygnąć przed odbiorem; nie wolno zmieniać znaczenia komendy dla obejścia braku.

## Spis treści

- **Część I — Cel zasady i zakres systemu**
  - [Załącznik nr 2 — Informacja dla organów ochrony ludności i jednostek samorządu terytorialnego](zalaczniki/Z2-INFORMACJA-DLA-ORGANOW.md)
- **Część II — Terminologia i zasady interpretacji**
  - [Załącznik nr 1 — Słownik pojęć](zalaczniki/Z1-SLOWNIK.md)
- **Część III — Wymagania techniczne i funkcjonalne**
  - [Załącznik nr 3 — Wymagania minimalne dla urządzenia](zalaczniki/Z3-WYMAGANIA-MINIMALNE.md)
  - [Załącznik nr 4 — Katalog sygnałów i plików referencyjnych](zalaczniki/Z4-KATALOG-SYGNALOW.md)
  - [Załącznik nr 5 — Profile sterownika i maszyna stanów](zalaczniki/Z5-PROFILE-STEROWNIKA.md)
- **Część IV — Przyłączenie i kanały komunikacji**
  - [Załącznik nr 6 — Poziom 0 publiczny wykaz poleceń](zalaczniki/Z6-POZIOM-0-PUBLICZNY-WYKAZ.md)
  - [Załącznik nr 7 — Rejestracja urządzenia i kanały rejestrowane](zalaczniki/Z7-POZIOM-1-REJESTRACJA.md)
  - [Załącznik nr 8 — Sieć wydzielona SMS i przejście na TETRA](zalaczniki/Z8-POZIOM-2-APN-I-SMS.md)
- **Część V — Konfiguracja i odbiór**
  - [Załącznik nr 9 — Karta konfiguracji urządzenia](zalaczniki/Z9-KARTA-KONFIGURACJI.md)
  - [Załącznik nr 10 — Scenariusze sprawdzeń i protokół odbioru](zalaczniki/Z10-TESTY-I-ODBIOR.md)
- **Część VI — Przygotowanie zamówienia**
  - [Załącznik nr 11 — Wytyczne do opisu przedmiotu zamówienia](zalaczniki/Z11-ZAPISY-DO-OPZ.md)
- **Część VII — Podstawa prawna i źródła**
  - [Załącznik nr 12 — Podstawa prawna i źródła](zalaczniki/Z12-PODSTAWA-PRAWNA.md)

## Powiązane opracowania

[Platforma KG PSP](PLATFORMA_KG_PSP.md) · [Profil 1.5](PROFIL_1_5.md) · [Zmiany wersji 0.5](ZMIANY_v0.5.md) · [Pełny podręcznik](PODRECZNIK_v2.md)
