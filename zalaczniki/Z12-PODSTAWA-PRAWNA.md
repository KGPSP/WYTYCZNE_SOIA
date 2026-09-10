---
tytuł: "Załącznik nr 12 — Podstawa prawna i źródła"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 12 — Podstawa prawna i źródła

## Status opracowania

To dokumentacja projektu wytycznych, nie nowy akt prawny ani dowód podpisania wytycznych KG PSP. Wersja 0.5 porządkuje wymagania techniczne i wdrożeniowe. Ich zastosowanie w konkretnym postępowaniu i instalacji wymaga określenia właściwego zakresu i podstawy prawnej.

10.09.2026 sprawdzono metadane ELI aktów wymienionych poniżej oraz treść przepisów istotnych dla sygnałów, czasu, zamówień i wskazanych zmian ustawy o ochronie ludności. Daty wejścia w życie sprawdza się niezależnie od ogólnej etykiety statusu w rejestrze.

## Ochrona ludności i sygnały

[Ustawa z 5 grudnia 2024 r. o ochronie ludności i obronie cywilnej, Dz.U. 2024 poz. 1907](https://api.sejm.gov.pl/eli/acts/DU/2024/1907) określa w art. 70–74 systemy wykrywania zagrożeń, powiadamiania, ostrzegania i alarmowania oraz bezpiecznej łączności. Art. 71 reguluje przekazywanie sygnałów i decyzje organów, a art. 72 stanowi delegację do rozporządzenia o alarmach. Obowiązki komunikacyjne z art. 73 nie są specyfikacją interfejsów sterownika.

[Rozporządzenie MSWiA z 14 maja 2025 r., Dz.U. 2025 poz. 645](https://api.sejm.gov.pl/eli/acts/DU/2025/645/text.pdf) obowiązuje od 31.05.2025. Określa rodzaje alarmów, sposoby ogłaszania i odwoływania oraz tryb przekazywania. Katalog akustyczny przedstawia Z4. Parametry portów, system operacyjny i profil 1.5 nie wynikają wprost z tego rozporządzenia — są wymaganiami technicznymi projektu.

| Nowelizacja ustawy | Stan istotny dla przeglądu |
| --- | --- |
| [Dz.U. 2025 poz. 1705](https://api.sejm.gov.pl/eli/acts/DU/2025/1705/text.pdf) | Zmienia art. 30; wejście w życie 1.01.2027, więc nie traktuje się jej zmian jako obowiązujących 10.09.2026. |
| [Dz.U. 2026 poz. 646](https://api.sejm.gov.pl/eli/acts/DU/2026/646/text.pdf) | Obowiązuje od 29.05.2026; sprawdzony zakres nie zmienia art. 70–74. |
| [Dz.U. 2026 poz. 815](https://api.sejm.gov.pl/eli/acts/DU/2026/815/text.pdf) | Obowiązuje od 4.07.2026; zmienia w tej ustawie art. 5, 15, 38, 40 i 44, nie art. 70–74. |

Odczyt metadanych źródłowej ustawy wskazał te trzy akty zmieniające. Pliku ogłoszonego nie nazwano automatycznie tekstem ujednoliconym; wpływ zmian sprawdzono osobno. Przed przyszłym użyciem aktu należy ponownie sprawdzić rejestr.

## Materiały referencyjne KG PSP

W materiałach źródłowych znajdują się dokumenty opisane datami 27 i 28 maja 2025 r., dotyczące cyfrowych sygnałów syren. Potwierdzono ich treść, w tym różnice opisu sygnału dla jednostki ochrony przeciwpożarowej, ale niniejszy przegląd nie potwierdza autentyczności podpisu i formalnego statusu każdego egzemplarza.

Wdrożenie wymaga pakietu i manifestu zatwierdzonego przez KG PSP, z określonym pochodzeniem, wersją i metodą odbioru. Wartości SHA-256, tolerancje i procedury nie są uznawane za aktualnie wiążące tylko dlatego, że występują w kopii podręcznika. Nie oznacza to stwierdzenia, że źródłowy dokument nie istnieje lub nie został wydany.

## Zamówienia i interoperacyjność

[Prawo zamówień publicznych, ustawa z 11 września 2019 r.](https://api.sejm.gov.pl/eli/acts/DU/2019/2019), w szczególności art. 99 i 101, jest podstawą oceny opisu przedmiotu i równoważności. Wskazanie istniejącego środowiska KG PSP wymaga uzasadnienia, opisu interfejsów i kryteriów. Nie stanowi automatycznie podstawy ograniczenia wykonawców do jednego producenta.

OrchestraOS, Yocto, RAUC i provisioning opisują wymagany model integracji. Dokumentacja przekazana wykonawcom ma pozwalać przygotować zgodną platformę na ich sprzęcie. Szczegółowa ocena konkretnego OPZ pozostaje odrębna od redakcji wytycznych.

## Czas i pozostałe akty kontekstowe

| Źródło urzędowe | Znaczenie |
| --- | --- |
| [Ustawa o czasie urzędowym, Dz.U. 2004 poz. 144](https://api.sejm.gov.pl/eli/acts/DU/2004/144) | Utrzymywanie i rozpowszechnianie czasu urzędowego. |
| [Rozporządzenie o rozpowszechnianiu czasu, Dz.U. 2004 poz. 548](https://api.sejm.gov.pl/eli/acts/DU/2004/548/text.pdf) | Wskazuje m.in. serwery NTP GUM; nie ustanawia samo hierarchii wszystkich źródeł czasu sterownika. |
| [Krajowe Ramy Interoperacyjności, Dz.U. 2024 poz. 773](https://api.sejm.gov.pl/eli/acts/DU/2024/773) | Kontekst interoperacyjności i utrzymania systemów; nie jest źródłem liczby portów 1.5. |
| [Centralna Ewidencja Zasobów, Dz.U. 2025 poz. 493](https://api.sejm.gov.pl/eli/acts/DU/2025/493) | Ewidencja zasobów ochrony ludności; odrębna od technicznego rejestru Orchestra. |
| [Centralna Ewidencja Obiektów Zbiorowej Ochrony, Dz.U. 2025 poz. 922](https://api.sejm.gov.pl/eli/acts/DU/2025/922) | Kontekst ustawowy, nie profil sterowania syreną. |
| [Ustawa o zarządzaniu kryzysowym](https://api.sejm.gov.pl/eli/acts/DU/2007/590) | Planowanie i organizacja w aktualnym brzmieniu, wraz z właściwymi zmianami. |

Próg kontroli czasu i zasady pomiaru są wymaganiami technicznymi określonymi w profilu, a nie automatycznym wnioskiem z przepisów o czasie urzędowym. Zakres bezpiecznej pracy urządzenia i instalacji wynika także z właściwej dokumentacji technicznej i projektu obiektu.

## Źródła techniczne aktualizacji

Podstawą kierunku były dokumenty KG PSP: wizja SOIA.KGPSP v0.3, wymagania wspólne platformy v0.2, profile sterowników v0.2 oraz instrukcje kanałów i integracji. Ich szczegółowe instrukcje instalacyjne i PDF-y nie są wgrywane w tym wydaniu repozytorium.

Dokumentacja mechanizmów: [Yocto Project](https://docs.yoctoproject.org/brief-yoctoprojectqs/index.html), [BSP](https://docs.yoctoproject.org/bsp-guide/index.html), [OrchestraOS](https://cthings.co/orchestra-os) i [RAUC](https://rauc.readthedocs.io/en/latest/basic.html). Opis produktu nie jest dowodem wdrożenia funkcji w instancji KG PSP. Wersję oraz prawa do komponentów określa pakiet integracyjny.

Weryfikacja dokumentacji i publicznych metadanych nie zastępuje odbioru urządzeń, aplikacji i sieci. Nie wykonywano prób emisji, wysyłki SMS ani zmian systemów operacyjnych w ramach przygotowania tego wydania.
