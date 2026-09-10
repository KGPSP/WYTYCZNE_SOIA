# Zmiany wytycznych w wersji 0.5

10 września 2026 r. · Projekt wytycznych

[← Wytyczne SOiA](README.md)

Aktualizację poprzedził przegląd wszystkich dwunastu załączników, dokumentów platformy KG PSP, publicznych metadanych IoT oraz wskazanych źródeł prawnych i technicznych. Wersja 0.5 porządkuje wymagania ogólne; nie poświadcza wdrożenia aplikacji lub odbioru modeli.

## Główne zmiany

| Obszar | Zmiana |
| --- | --- |
| Rdzeń I i profil 1.5 | Oddzielono wspólną platformę i bezpieczeństwo od rozbudowanej liczby portów. Dodano kompaktowy profil z audio. |
| TTS | Klasa III rozszerza funkcje i zasoby; sama nie zwiększa liczby przekaźników i I/O. |
| Platforma | Obowiązkowy obraz Yocto/OrchestraOS wydania KG PSP dla konkretnej płyty, przygotowany przez wykonawcę z udostępnionych komponentów. |
| Provisioning | Rozdzielono przyjęcie modelu, przygotowanie egzemplarza, rejestrację Orchestra, aplikację i odbiór obiektu. |
| Role | KG PSP dostarcza aplikację alarmową; wykonawca zapewnia platformę i interfejsy. Manager utrzymuje urządzenia, nie podejmuje drugiej decyzji alarmowej. |
| Sygnały | Oddzielono nominalny katalog, zatwierdzony pakiet lokalny i faktycznie ogłoszone kody API. |
| Wykonanie | Ujednolicono odrzucenie, odroczenie, anulowanie akcji, odwołanie dźwiękowe, techniczne STOP i odcięcie. |
| SMS | Rozdzielono starszy moduł, nowy kontrakt aplikacji i usługę operatorską. Uwierzytelnienie treści i historia nie wynikają z samej SIM. |
| Feed | Doprecyzowano 304, ważność, normalny polling i wyjątki, przyszłe akcje oraz nieznane ID anulowania. |
| Sprzęt i montaż | PTT może użyć istniejącego styku; mały sterownik nie musi przełączać 230 V. Oddzielono napęd/wzmacniacz od zasilania sterownika. |
| Migracja | GSM/LTE w fazie 2026–2028; docelowa TETRA po odbiorze lokalizacji, z czynnym zapasem GSM. |
| Odbiór | Karta obejmuje wydania, porty, tożsamość, rejestrację i dowody. Dodano próby platformy oraz profilu 1.5. |

## Ciągłość i granice

Zachowano identyfikatory 166 wymagań W-* i 103 scenariuszy S-* z wydania 0.4. Dodano W-D26, W-F15–W-F19 i S-104–S-120. Wersja wynikowa zawiera 172 wymagania oraz 120 scenariuszy. Zmiany zakresu opisano w Z3; nie zmieniają automatycznie wcześniejszych zamówień i protokołów.

Pełna i rozdzielona postać korzystają z tej samej treści załączników. Podstawa poprzednia pozostaje dostępna w [historii wydania 0.4](https://github.com/KGPSP/WYTYCZNE_SOIA/tree/49126d36904fa0d7166ea1d0456c6f3a81babf1c).

Nie dodano PDF, danych operacyjnych ani plików z konfiguracją urządzeń. Aktualizacja dokumentacji nie jest wdrożeniem TTS, nowego słownika API lub TETRA. Przed odbiorem właściwe funkcje wymagają zgodnego kontraktu, konfiguracji i dowodu.
