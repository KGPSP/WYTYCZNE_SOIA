---
tytuł: "Załącznik nr 4 — Katalog sygnałów i plików referencyjnych"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

<!-- Generated from zalaczniki/Z4-KATALOG-SYGNALOW.md; run python scripts/sync_pages.py. -->

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-tresci)

# Załącznik nr 4 — Katalog sygnałów i plików referencyjnych

## Sygnał, plik i komenda

Sygnał akustyczny, jego plik referencyjny i kod w protokole są różnymi pojęciami. Przepisy określają rodzaj i nominalny przebieg sygnału. KG PSP określa zatwierdzony pakiet lokalny. Kontrakt centrali określa, jakie funkcje można aktualnie wywołać danym kanałem. Zmiana wytycznych nie wdraża nowego kodu w centrali.

## Katalog akustyczny

Podstawa: [rozporządzenie MSWiA z 14 maja 2025 r., Dz.U. poz. 645](https://api.sejm.gov.pl/eli/acts/DU/2025/645/text.pdf), załącznik, strona 4.

| Funkcja | Przebieg nominalny |
| --- | --- |
| Ogłoszenie alarmu dla ludności cywilnej | Sygnał modulowany, 180 s. |
| Odwołanie alarmu dla ludności cywilnej | Sygnał ciągły, 180 s. |
| Alarm dla jednostki ochrony przeciwpożarowej | Trzykrotnie wzrastający i opadający dźwięk, z przerwami 30 s, łącznie 180 s. |
| Alarm ćwiczebny lub treningowy | Sygnał ciągły, 60 s. |

W profilu podstawowym dla ludności wymagane są ogłoszenie i odwołanie alarmu. Pozostałe funkcje dobiera się do profilu zastosowania i uprawnień, zachowując ich właściwe przebiegi. Dostępność lokalna nie jest uprawnieniem do zdalnego uruchomienia.

Odwołanie jest odrębną emisją, nie ciszą, STOP ani anulowaniem akcji oczekującej. Syrena silnikowa realizuje sygnał programem napędu, a elektroniczna odtwarza zasób we właściwym torze. Zapowiedzi słowne i sygnalizacja wizualna wymagają odpowiednich profili.

## Stan publicznego kontraktu

Odczyt publicznych metadanych 10.09.2026 potwierdził profil `PL-CAP-DIST-IOT` w wersji `0.1`, słownik `2026.1` i klasę odbiorcy `SIREN_CONTROLLER`.

| Kod ogłoszony w metadanych | Znaczenie |
| --- | --- |
| `SIREN_ALARM_MODULATED_3M` | Ogłoszenie alarmu, z kwalifikacją według kontraktu. |
| `SIREN_CANCEL_PENDING` | Anulowanie wskazanej znanej akcji oczekującej; bez dźwięku odwołania. |

Źródła: [profil](https://alarm.soia.info/api/v1/iot/profile) i [słowniki](https://alarm.soia.info/api/v1/iot/dictionaries). Jest to datowany odczyt. Przed odbiorem sprawdza się wersję przeznaczoną do współpracy z urządzeniem.

W tym odczycie nie potwierdzono odrębnej publicznej komendy dźwiękowego odwołania, wywołania jednostki, sygnału ćwiczebnego ani ogólnego TTS. Nie przypisuje się im z góry kodów rzekomo obowiązującego słownika 2026.2. Ich wdrożenie wymaga zgodnego kontraktu i aplikacji. Kody SMS wynikają z konkretnego profilu, a nie z uniwersalnej cyfry polecenia.

## Lokalny pakiet i kontrola integralności

Dla podstawowego toru elektronicznego sterownik ma lokalne zasoby ALARM i ODWOLANIE, po 180 s. Nazwy fizycznych plików, format, wersję i skróty określa zatwierdzony manifest. Pakiet musi mieścić się w pamięci oraz przetrwać restart, aktualizację i odtworzenie.

| Element manifestu | Znaczenie |
| --- | --- |
| Wydanie i akceptacja | Wiadomo, kto i dla jakiego profilu zatwierdził zasób. |
| Funkcja i plik | Jednoznaczne powiązanie lokalnej funkcji z zasobem. |
| Format i parametry | Kodowanie, kanały, próbkowanie i nominalny czas. |
| Skrót i pochodzenie | Możliwość sprawdzenia, że dostarczono właściwy zasób. |
| Metoda odbioru | Punkt pomiaru, tolerancja i niepewność pomiarowa. |

W obiegu istnieją materiały referencyjne z maja 2025 r. Nie przenosi się sum z dowolnej kopii jako aktualnych kotwic wdrożenia bez potwierdzenia wydania i akceptacji. Tolerancje nie zmieniają nominalnego czasu sygnału. Odsłuch nie zastępuje sprawdzenia integralności, a skrót pliku nie potwierdza akustycznego efektu instalacji.

## Dystrybucja i aktualizacja

Pliki dostarcza się przed uruchomieniem funkcji. Aktualizacja pakietu może korzystać z zatwierdzonego mechanizmu utrzymania KG PSP, z kontrolą wersji i integralności oraz potwierdzeniem instalacji. Jest osobna od pobierania IoT Feed; alarm nie wymaga pobrania audio ani strumieniowania z internetu.

Wariant API z plikami w syrenie wymaga odrębnego przyjęcia miejsca zasobu, jego kontroli i mapy funkcji. Nie zastępuje milcząco profilu lokalnych plików w sterowniku. Pakiet aplikacji, pakiet audio, słownik kodów i wytyczne mają odrębne wersje.

## Sprawdzenia okresowe

Plan utrzymania określa częstotliwość i zakres sprawdzeń na podstawie właściwych wytycznych, DTR i oceny instalacji. Sprawdza się zasoby, sygnały, ochronę przed błędnym uruchomieniem oraz zasilanie. Niezgodność wymaga ustalenia przyczyny i zakresu ograniczenia gotowości; ponowne wgranie pliku nie naprawia automatycznie usterki toru fizycznego. Próby emisji organizuje się zgodnie z właściwą procedurą.
