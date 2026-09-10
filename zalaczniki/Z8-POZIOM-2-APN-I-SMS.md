---
tytuł: "Załącznik nr 8 — Sieć wydzielona SMS i przejście na TETRA"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 8 — Sieć wydzielona SMS i przejście na TETRA

## Kanał i poziom podłączenia

Sieć wydzielona ogranicza dostęp, ale nie zastępuje walidacji komendy. SMS jest kanałem wykonawczym z własnym kontraktem, a nie powiadomieniem o zmianie feedu. Wymagania aplikacyjne nie powstają przez samą wymianę karty SIM.

W fazie 2026–2028 zestawy korzystają z GSM/LTE, z SMS jako zapasem i możliwością dodatkowego IP przez Ethernet lub Wi-Fi. Po tej fazie TETRA ma być podstawowym kanałem poleceń, po jej zapewnieniu i odbiorze. GSM pozostaje czynny. Zmiana operatora lub APN oraz migracja TETRA są osobnymi procesami.

## Trzy odrębne profile SMS

| Profil | Zakres i ograniczenia |
| --- | --- |
| Zastany moduł syreny | Składnia i funkcje według DTR. Może obsługiwać hasło oraz listę numerów, bez ID i ważności komendy. Nie przypisuje się mu zabezpieczeń nieobecnych w parserze. |
| Nowa aplikacja KG PSP | Pełna walidacja uzgodnionego kontraktu, kryptograficzna autentyczność i integralność, adresat, ważność, ID i trwała ochrona przed odtworzeniem. |
| Warstwa operatorska | Usługi nadawcze i odbiorcze, SIM, APN i ograniczenia sieciowe. Nie zastępuje dwóch powyższych profili. |

Właściciel i administrator określają dopuszczony zakres użycia starszego modułu oraz sposób jego współpracy z nowym sterownikiem. Starszy SMS bez ID i czasu nie jest pełnym odpowiednikiem podpisanego feedu. Nie wysyła się automatycznie tego samego żądania równolegle wszystkimi kanałami bez wspólnej identyfikacji i arbitrażu.

## Przygotowanie SIM i numerów

Karta musi obsługiwać dane, jeżeli służy do IP, oraz SMS przychodzące i wychodzące w wymaganych kierunkach. Umowa wyłącznie na dane nie potwierdza SMS. Sprawdza się aktywność, blokady, antenę, powrót po restarcie i zgodność z modemem.

Oddzielnie zapisuje się numer urządzenia, numery uprawnione do sterowania, odbiorców statusów i administratorów konfiguracji. Numer widoczny w odebranej wiadomości musi odpowiadać przyjętemu profilowi. Nadpis tekstowy ani wpis w polu nadawcy usługi nie tworzą działającej skrzynki odbiorczej.

Jeżeli niezależny modem syreny i modem sterownika mają pracować równocześnie, trzeba zapewnić usługi dla obu. Zamknięta grupa abonencka ogranicza ruch tylko w zakresie potwierdzonym przez operatora; sama lista w urządzeniu nie zmienia zasad sieci.

## Kontrakt wiadomości i odpowiedzi

Nowy kontrakt określa funkcję, adresata, ID operacji, ważność, materiał uwierzytelniający, kodowanie, długość i zachowanie po błędzie. Składni nie ustala sam instalator. Hasło, czas i rosnący licznik przesłane bez ochrony integralności nie są kryptograficznym uwierzytelnieniem treści.

Modem udostępnia aplikacji pełną treść, nadawcę i metadane. Profil może ograniczać polecenie do jednego SMS; jeśli dopuszcza multipart, musi określić identyfikację części, limit liczby, rozmiaru i czasu oraz walidację kompletnej wiadomości przed wykonaniem. Nie wolno wykonywać fragmentu ani uznawać braku części za pustą komendę.

| Informacja zwrotna | Co potwierdza |
| --- | --- |
| Przyjęcie przez usługę nadawczą | Zarejestrowanie wysyłki. |
| Raport doręczenia | Etap transportu określony przez operatora. |
| ACK aplikacji | Rozpoznanie i kwalifikację operacji zgodnie z kontraktem. |
| Start i koniec | Właściwy etap lokalnej funkcji, wraz z ID operacji. |
| Błąd lub niepewność | Brak pełnego dowodu powodzenia; bez automatycznej drugiej emisji. |
| Pomiar zewnętrzny | Efekt w zakresie rzeczywistego czujnika i pomiaru. |

Test łączności bez emisji nie wymaga fikcyjnego potwierdzenia dźwięku. Spóźnionego statusu bez ID operacji nie należy przypisywać nowemu zleceniu wyłącznie przez zgodny numer syreny. Treść rejestrowana w logach nie może ujawniać haseł lub sekretów.

## Przejście na TETRA

Przygotowanie obejmuje port obsługiwany przez OS, miejsce, zasilanie, antenę i adapter. Docelowo wymagane są konkretny terminal, właściwa usługa sieciowa, tożsamość i integracja centralna. Samo złącze USB ani katalogowa możliwość TETRA nie potwierdzają tej zdolności.

Usługa IP TETRA i SDS są różnymi drogami. Wariant IP wymaga wykazanej osiągalności i pojemności dla ruchu aplikacji. SDS wymaga jawnego transportu polecenia, z zachowaniem znaczenia, autentyczności, ważności i historii. Nie zakłada się przesyłania całego feedu co 30 s przez każdy terminal bez oceny pojemności.

TETRA przenosząca tylko komunikat „pobierz feed” pozostaje zależna od innego IP. Docelowy tor podstawowy musi wykazać wykonanie wymaganej funkcji przy odłączonym GSM i internecie obiektu. Duże aktualizacje mogą nadal korzystać z LAN/Wi-Fi/LTE. Nie zmienia to pierwszeństwa TETRA dla poleceń po odbiorze migracji.

## Próby migracji i eksploatacja

Przed przełączeniem sprawdza się nową drogę, stary zapas, wspólną historię, utratę i powrót zasięgu oraz brak odtworzenia przeterminowanych poleceń. Dotychczasową usługę wyłącza się dopiero zgodnie z planem ciągłości; GSM pozostaje aktywnym zapasem fazy docelowej.

Przepustowość SMS, radia i zwrotek musi odpowiadać zakładanemu obszarowi oraz oknu wykonania. Brak ACK nie dowodzi awarii syreny ani niewykonania. Wynik zbiorczy nie ukrywa błędów poszczególnych urządzeń. Dane dostępowe, numery i parametry sieci pozostają w chronionej karcie konfiguracji.
