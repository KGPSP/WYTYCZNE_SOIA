# Instrukcje i materiały robocze SOIA.KGPSP

[Powrót do głównego README](../README.md)

Zestaw dokumentów pomocniczych do organizacji montażu, dołączania syren do systemu KG PSP, przygotowania urządzeń i odbioru instalacji. Obejmuje **15 plików PDF, łącznie 235 stron**, według stanu z **10 września 2026 r.**

**Status widoczny w przekazanych PDF-ach: AKCEPTACJA - BIŁ KGPSP.** Każdy dokument ma własny numer wersji. Status dotyczy dokumentacji; wykonanie instalacji i dopuszczenie urządzeń wymagają właściwych konfiguracji, pomiarów i prób opisanych w materiałach.

Dokumentacja będzie rozwijana. Przy przygotowywaniu prac należy sprawdzić wersję opracowania, jego zakres i dokumenty, do których odsyła. Numery wersji tych PDF-ów są odrębne od numeru wydania podręcznika SOiA w katalogu głównym repozytorium.

## Wykaz dokumentów

Nazwy w tabeli prowadzą bezpośrednio do odpowiednich PDF-ów.

| Nr | Dokument | Wersja | Strony | Zawartość i zastosowanie |
| --- | --- | --- | ---: | --- |
| 1 | [Spis dokumentów WYTYCZNE_KRAJ](pdf/00_SPIS_DOKUMENTOW_WYTYCZNE_KRAJ_v0.1.pdf) | 0.1 | 8 | Przewodnik po pakiecie: odbiorcy, rola poszczególnych opracowań i kolejność korzystania zależna od zadania. |
| 2 | [Rekomendacje dla KW PSP dotyczące montażu SS100 z KPO i bramek LoRaWAN](pdf/REKOMENDACJE_KW_PSP_MONTAZ_SS100_KPO_LORA_v0.4.pdf) | 0.4 | 16 | Zakres montażu posiadanych zestawów, odpowiedzialność wykonawcy i KG PSP, SIM/LAN, provisioning, sprawdzenia oraz zasady odbioru. Punkt wyjścia do organizacji prac w województwie. |
| 3 | [Wizja systemu SOIA.KGPSP](pdf/WIZJA_SYSTEMU_SOIA_KGPSP_v0.3.pdf) | 0.3 | 20 | Warstwy systemu, OrchestraOS, aplikacja KG PSP, budowa obrazu dla płyty, tożsamość, rejestracja urządzeń i kolejne poziomy gotowości. |
| 4 | [Adaptacja i zakup syren dla SOIA KGPSP](pdf/ADAPTACJA_I_ZAKUP_SYREN_SOIA_KGPSP_v0.1.pdf) | 0.1 | 22 | Dobór kompletnego rozwiązania dla istniejących syren i nowych punktów: profile wykonania, interfejsy, łączność, przygotowanie do TETRA oraz odbiór. |
| 5 | [Plakat doboru syren](pdf/PLAKAT_DOBORU_SYREN_SOIA_KGPSP_v0.3_A2.pdf) | 0.3 | 1 | Mapa doboru dla SAD, DSE-600, Pavian i nowej instalacji; wspólna platforma, łączność i uruchomienie. Format A2. |
| 6 | [Minimalne wymagania dla sterownika zgodnego z systemem KG PSP](pdf/MINIMALNE_WYMAGANIA_STEROWNIKA_SMS_IOT_ORCHESTRA_LNS_v0.2.pdf) | 0.2 | 21 | Funkcjonalne wymagania przyłączenia do KG PSP: komponenty Yocto/OrchestraOS na wniosek, bezpieczeństwo, zarządzanie, kanały i interfejsy. Obejmuje 39 wymagań oraz 18 prób zgodności. |
| 7 | [Minimalne wymagania dla sterowników SOiA — profile urządzeń](pdf/MINIMALNE_WYMAGANIA_STEROWNIKOW_KG_PSP_v0.2.pdf) | 0.2 | 15 | Dobór zasobów i portów do zadania, zestawienie wariantów sprzętowych oraz ich powiązanie ze wspólnymi wymaganiami platformy. |
| 8 | [Wymagania dla oprogramowania SS100 — SMS i IoT Feed](pdf/WYMAGANIA_SS100_SMS_IOT_FEED_v0.2.pdf) | 0.2 | 33 | Dwa kanały poleceń, lokalne pliki ALARM/ODWOLANIE, audio/PTT, kwalifikacja komend, trwała historia i scenariusze odbioru. Zawiera pełną instrukcję AUDIO/PTT jako załącznik nr 1. |
| 9 | [Instrukcja instalatora SS100 z KPO](pdf/Instrukcja_instalatora_SS100_KPO_v0.3.pdf) | 0.3 | 20 | Montaż SS100 i UG67, internet, mapa zacisków, połączenie syreny, przekazanie do obsługi KG PSP, kontrole M-01–10 i P-01–09 oraz karty obiektu i pomiarów. |
| 10 | [Instrukcja instalacyjna SS100 — PC-550A Z18 AUDIO/PTT](pdf/Instrukcja_instalacyjna_SS100_PC550A_Z18_AUDIO_PTT_v0.2.pdf) | 0.2 | 12 | Instrukcja dla wskazanego interfejsu: dopasowanie audio, osobne PTT, przygotowanie stanowiska, pomiary i trzystronicowa karta odbioru. Numeracji Z18 nie przenosi się na inne modele. |
| 11 | [Opracowanie techniczne LINE OUT — PC-550A Z18](pdf/SS100_LINE_OUT_PC550A_Z18_AUDIO_PTT_v0.1.pdf) | 0.1 | 10 | Wyjaśnienie połączenia wyjścia liniowego z wejściem mikrofonowym, tłumienia, separacji DC, sterowania PTT oraz kwalifikacji adaptera. Uzupełnienie instrukcji instalacyjnej. |
| 12 | [Syrena silnikowa SAD — definicja, budowa i podłączenie](pdf/SYRENA_SILNIKOWA_SAD_DEFINICJA_BUDOWA_PODLACZENIE_v0.2.pdf) | 0.2 | 21 | Profil syreny silnikowej ze sterownikiem SS-22, izolowana warstwa wykonawcza, nadzór oraz warianty obwodów. Wymaga projektu i odbioru konkretnej instalacji. |
| 13 | [Konfiguracja urządzenia do sterowania syreną przez SMS](pdf/INSTRUKCJA_KONFIGURACJI_URZADZENIA_SMS_SYRENY_KRAJ_v0.1.pdf) | 0.1 | 14 | Przygotowanie SIM, numerów, uprawnień i odpowiedzi oraz karta konfiguracji dla opisanego profilu urządzenia. Przykładowych nastaw nie przenosi się automatycznie na całą flotę. |
| 14 | [Konfiguracja odbiornika publicznego IoT Feed](pdf/INSTRUKCJA_KONFIGURACJI_ODBIORNIKA_IOT_FEED_KRAJ_v0.1.pdf) | 0.1 | 15 | HTTPS, podpis, klucze zaufania, TERC, czas, historia i kwalifikacja komend. Opis API odnosi się do daty sprawdzenia wskazanej w dokumencie. |
| 15 | [Wstępny szacunek montażu SS100 z KPO wraz z integracją](pdf/WSTEPNY_SZACUNEK_MONTAZU_SS100_KPO_Z_INTEGRACJA_v0.1.pdf) | 0.1 | 7 | Kalkulacja budżetowa jednego punktu: materiały, robocizna, sprzęt, dojazd, integracja i rezerwa. Wartości wymagają dopasowania do obiektu i aktualnej wyceny. |

## Korzystanie z pakietu

- **Organizacja montażu KPO:** rozpocznij od rekomendacji dla KW PSP, następnie instrukcji instalatora i dokumentacji właściwego toru syreny.
- **Adaptacja lub nowa dostawa:** użyj przewodnika adaptacji, wspólnych wymagań platformy i profili urządzeń; plakat ułatwia wstępny dobór.
- **Konfiguracja i odbiór:** rozdziel wymagania aplikacji, przygotowanie SMS/IoT oraz fizyczne sprawdzenie połączenia z syreną.

PDF wymagań oprogramowania ma 33 strony, ponieważ zawiera także pełną 12-stronicową instrukcję AUDIO/PTT. Ta sama instrukcja jest dostępna osobno w pozycji 10 dla wygody instalatora.

Oznaczenia i przykłady w dokumentach należy stosować w granicach wskazanego modelu, profilu i zakresu dostawy. Akceptacja dokumentacji, rejestracja urządzenia, dostęp do zarządzania i potwierdzenie emisji syreny są odrębnymi zdarzeniami.

## Aktualizacje

Przy wymianie pliku należy zaktualizować jego wersję, nazwę i opis w tym wykazie. Bieżący pakiet obejmuje wyłącznie wymienione PDF-y; kopie archiwalne, pliki robocze programu i lokalne materiały źródłowe nie są częścią tego katalogu.

Pakiet jest publikowany w repozytorium GitHub oraz w [GitHub Pages — dokumenty PDF do pobrania](https://kgpsp.github.io/WYTYCZNE_SOIA/DOKUMENTY_PDF/). Kopie na stronie są synchronizowane z plikami w tym katalogu; kontrola CI sprawdza ich zgodność bajt po bajcie. Przy aktualizacji zestawu odśwież także spis `DOKUMENTY_PDF.md` i wykaz `docs/pdf/manifest.json` w katalogu głównym repozytorium, a następnie uruchom `python scripts/sync_pages.py`.
