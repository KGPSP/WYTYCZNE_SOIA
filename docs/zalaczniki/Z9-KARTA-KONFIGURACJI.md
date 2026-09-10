---
tytuł: "Załącznik nr 9 — Karta konfiguracji urządzenia"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

<!-- Generated from zalaczniki/Z9-KARTA-KONFIGURACJI.md; run python scripts/sync_pages.py. -->

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-tresci)

# Załącznik nr 9 — Karta konfiguracji urządzenia

Jedna karta opisuje jeden egzemplarz sterownika i jego powiązanie z obiektem. Wiele niezależnych torów ma osobną mapę. Wypełniona karta, identyfikatory operacyjne, numery i sekrety są przekazywane w chronionym obiegu, poza repozytorium publicznym. Nie wpisuje się do karty kluczy prywatnych.

Wartości operacyjne zatwierdza właściwy administrator. Wykonawca zapisuje konfigurację i wyniki pomiarów, a właściciel przejmuje dokumentację po odbiorze. Zmiana płyty, SIM, obrazu, profilu lub połączeń wymaga aktualizacji właściwych części karty i odpowiednich prób.

## A. Model i egzemplarz

| Pole | Wartość |
| --- | --- |
| Numer karty i rewizja | |
| Właściciel, obiekt i lokalizacja | |
| Model i rewizja płyty sterownika | |
| Numer seryjny i ID urządzenia w ewidencji KG PSP | |
| ID Orchestra i właściwa instancja | |
| ID syreny, model i rewizja elektroniki | |
| Klasy zdolności | I + ☐ 1.5 ☐ II; opcjonalnie ☐ III |
| Zakres dostawy | ☐ moduł ☐ zestaw D ☐ wymagania P ☐ sprzęt powierzony |
| Profil wykonawczy | ☐ elektroniczny ☐ silnikowy ☐ inny: … |
| Tryb integracji | ☐ AUDIO/PTT ☐ API ☐ izolowany tor silnikowy |
| Rodzaj inwestycji | ☐ nowa ☐ adaptacja |
| Dowód przyjęcia konfiguracji modelu | |

## B. Obraz i przygotowanie platformy

| Pole | Wartość |
| --- | --- |
| Wydanie komponentów Yocto/OrchestraOS od KG PSP | |
| OS, BSP, manifest i skrót obrazu | |
| Wersja adapterów i kontraktu sprzętowego | |
| Pakiet aplikacji KG PSP i metoda instalacji | |
| Zasoby i bilans A/B, danych, audio oraz rezerwy | |
| Profil zaufania aktualizacji i rozruchu | Identyfikatory, bez kluczy prywatnych |
| Provisioning egzemplarza i dowód rejestracji | |
| Flota aktualizacyjna i zakres uprawnień | |
| Sposób odtworzenia i wycofania urządzenia | |

## C. Mapa torów i obszaru

Każdy niezależny tor ma dokładnie jeden siedmiocyfrowy TERC. Nie wpisuje się listy sąsiednich gmin tylko dlatego, że dochodzi do nich dźwięk. Kod powiatu, województwa, miejscowości lub ulicy nie jest prawidłową konfiguracją tego pola.

| Tor | TERC gminy | Syrena lub odbiornik | Funkcje i interfejs |
| --- | --- | --- | --- |
| 1 | | | |
| 2, jeżeli występuje | | | |

| Interfejs | Liczba dostępna | Przydział i parametry | Rezerwa |
| --- | --- | --- | --- |
| Ethernet | | | |
| RS-232 | | | |
| USB | | | |
| Styki NO/NC/COM | | PTT lub RUN/CYKL uwzględnione w liczbie | |
| GPI | | | |
| GPO | | | |
| Audio OUT / wymagane IN | | | |

## D. Łączność i uprawnienia

| Pole | Wartość |
| --- | --- |
| Etap | ☐ GSM/LTE 2026–2028 ☐ odebrana migracja TETRA |
| Kanał podstawowy i zapasowy | |
| Ethernet/Wi-Fi obiektu i polityka przełączania | |
| Modemy i przypisanie usług SIM | |
| Operator, APN i wymagane dane/SMS MO/MT | |
| Numer urządzenia | |
| Nadawcy uprawnieni do sterowania | |
| Odbiorcy statusów i rodzaj zwrotek | |
| Administratorzy konfiguracji | |
| Profil SMS i mechanizm uwierzytelnienia | Referencja do sekretu w chronionym obiegu |
| Profil IoT, słownik, endpoint i zaufane klucze | |
| Źródła czasu i warunki utraty wiarygodności | |
| LoRaWAN node, bramka i profil LNS/CUPS | |
| TETRA: terminal/usługa lub obecna rezerwa | |

## E. Funkcja i zasoby lokalne

| Funkcja | Kod i wersja kontraktu | Zasób lub program lokalny | Wynik i sposób potwierdzenia |
| --- | --- | --- | --- |
| Test bez emisji | | | |
| ALARM dla ludności | | | |
| ODWOLANIE dla ludności | | | |
| Inne sygnały objęte profilem | | | |
| TTS, jeżeli zamówiony | | | |
| Anulowanie akcji oczekującej | | | |
| Techniczne STOP, jeżeli przewidziane | | | |

| Parametr | Wartość i dowód |
| --- | --- |
| Pakiet/manifest audio, skróty i akceptacja | |
| Program silnikowy i parametry obiektu | |
| Adapter poziomu/izolacji lub protokołu | |
| PTT, Tpre/Tpost i niezależny nadzór | |
| Lokalny TTS: głos, wersja, prawa i próba offline | |
| Tabela arbitrażu: odrzucenie/odroczenie/STOP | |
| Historia, retencja i zachowanie po restarcie | |

## F. Zasilanie i montaż

| Pole | Wartość i dowód |
| --- | --- |
| Elementy dostarczone, powierzone i obiektowe | |
| Mapa przewodów i zacisków powykonawczych | |
| Ochrona elektryczna, izolacja i przepięcia | |
| Zasilane elementy i profil obciążenia | |
| Podtrzymanie sterowania/łączności | |
| Osobny bilans wzmacniacza lub silnika | |
| Rezerwa zasilania i miejsca dla TETRA | |
| Deklarowane warunki pracy i warunki obiektu | |
| Temperatura przy odbiorze i ocena zakresu | |
| Przejście na rezerwę i powrót zasilania | |

## G. Odbiór i przekazanie

Wyniki każdego właściwego scenariusza Z10: **pozytywny**, **negatywny**, **nie wykonano** albo **nie dotyczy z uzasadnieniem zakresu**. Brak wymaganej funkcji nie jest „nie dotyczy”.

| Grupa | Dowody i wynik |
| --- | --- |
| Platforma, obraz i konfiguracja modelu | |
| Profil 1.5 lub rozszerzony, wyposażenie i opcje | |
| Provisioning, Orchestra i uprawnienia | |
| Aplikacja, kanały, adresat i odmowy | |
| Tor lokalny, sygnały i opcjonalny TTS | |
| Arbitraż, błędy, restart i podtrzymanie | |
| TETRA: przygotowanie lub odbiór migracji | |
| Dokumentacja, odtworzenie i utrzymanie | |

**Rozstrzygnięcie i zakres dopuszczonych funkcji:** …

**Niezgodności, zakres ograniczenia gotowości i termin działań:** …

**Wykonawca / przedstawiciel właściciela / data / podpisy:** …

Stan „online” ani pozytywny test samej łączności nie zastępują odbioru. Kartę przejmuje właściciel; kopie, retencja i wycofanie wersji są zarządzane zgodnie z właściwą polityką.
