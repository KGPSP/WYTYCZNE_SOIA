---
tytuł: "Profil 1.5 dla kompaktowych sterowników"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
---

<!-- Generated from PROFIL_1_5.md; run python scripts/sync_pages.py. -->

[← Wytyczne SOiA](index.md)

# Profil 1.5 dla kompaktowych sterowników

**Profil 1.5 umożliwia zastosowanie mniejszego sterownika z lokalnym audio i mniejszą liczbą portów, przy zachowaniu wspólnej platformy oraz zabezpieczeń KG PSP.** Jest dodawany do rdzenia klasy I. Oznaczenie dotyczy zdolności i wyposażenia; nie jest nazwą producenta, modelem, poziomem podłączenia ani wersją protokołu.

Wiążące liczby i wymagania znajdują się w [macierzy Z3](zalaczniki/Z3-WYMAGANIA-MINIMALNE.md#macierz-wyposazenia). Profil 1.5 nie powstaje przez pominięcie dowolnych wymagań klasy I lub przez zmianę etykiety istniejącego urządzenia.

## Kiedy wybrać profil kompaktowy

| Potrzeba | Wybór |
| --- | --- |
| Jeden niewielki punkt, ograniczona liczba sygnałów i lokalne pliki | I + 1.5 po sprawdzeniu bilansu portów i zasobów. |
| Syrena silnikowa z prostym torem wykonawczym | I + 1.5 może obsłużyć profil silnikowy; wyjścia sterują izolowaną aparaturą, a audio pozostaje niewykorzystane. |
| Więcej niezależnych Ethernetów, wejść i wyjść | I + II albo jawna kompletacja rozszerzeń. |
| Zmienny tekst do wypowiedzenia | Dodać III, z właściwymi zasobami i TTS offline. Sama synteza nie wymaga zwiększenia I/O. |
| Posiadany zgodny sterownik o większych możliwościach | Wykorzystać go; profil kompaktowy nie jest nakazem wymiany sprawnej platformy. |

Syrena silnikowa nie odtwarza plików ani mowy. Syrena elektroniczna bez TTS może odtwarzać gotowe nagrania. Zdolność syntezy mowy nie wynika z samej obecności wyjścia audio lub pamięci.

## Co pozostaje wspólne

OrchestraOS wydania KG PSP, budowa na Yocto dla konkretnej płyty, provisioning, indywidualna tożsamość, zarządzanie Orchestra i aplikacja KG PSP obowiązują tak samo jak na większej platformie. Nie obniża się walidacji poleceń, kontroli czasu i adresata, trwałości historii, ograniczenia czasu wyjść ani ochrony kluczy.

Profil kompaktowy zachowuje wymagania jakości lokalnego audio z Z3. Ma dwa kanały LINE OUT i osobno sterowane PTT oraz pamięć na zatwierdzony pakiet. PTT może korzystać z jednego z dwóch przekaźników; nie trzeba doliczać trzeciego tylko dlatego, że PTT występuje osobno w wykazie funkcji.

Każda opcja niezbędna do wykonania wymagań, w tym Wi-Fi, GNSS, wymagane audio IN albo dodatkowy port, ma być dostarczona i uruchomiona. Deklaracja „opcjonalne” nie jest potwierdzeniem kompletnej konfiguracji. Wczesne propozycje handlowe nie zastępują macierzy Z3.

## Porty i przyszła TETRA

Karta podaje rzeczywiste zajęcie RS-232, USB, Ethernetu, styków i GPI/GPO. Nie liczy się jednego portu dwukrotnie dla urządzeń pracujących równocześnie. Zapas dla TETRA obejmuje obsługiwany interfejs, miejsce, moc, antenę i możliwość instalacji adaptera. Nie wystarcza samo wolne USB.

Terminal, dostęp do sieci, usługa danych i integracja centralna wymagają odrębnego odbioru. Powiadomienie radiowe o konieczności pobrania feedu nie zapewnia samodzielnego wykonania przy braku GSM i internetu obiektu. Docelowy profil TETRA musi wykazać wymaganą niezależność.

## Warunek przyjęcia

Wykonawca przedstawia konfigurację modelu, obraz i BSP, mapę portów, bilans zasobów oraz zasilania, interfejsy i dowody prób. Odbiór obejmuje [Z10](zalaczniki/Z10-TESTY-I-ODBIOR.md), w tym próby profilu kompaktowego i platformy. Wynik pozytywny dotyczy dostarczonego wydania i konfiguracji, a nie całej rodziny urządzeń.

Oznaczenie 1.5 nie zmienia `deviceClass` w IoT Feed. Wersja wytycznych 0.5 nie oznacza wdrożenia nowej wersji API, TTS ani TETRA. Te zdolności są wykazywane osobno.
