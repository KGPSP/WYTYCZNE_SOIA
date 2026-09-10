---
tytuł: "Załącznik nr 11 — Wytyczne do opisu przedmiotu zamówienia"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 11 — Wytyczne do opisu przedmiotu zamówienia

## Zakres i zasady

Załącznik pomaga przygotować opis dostawy, ale nie jest gotowym OPZ. Zamawiający określa funkcję, obiekt, klasy zdolności, zakres dostawy i kryteria odbioru. Zgodność z instancją KG PSP nie może sprowadzać się do nazwy produktu lub ogólnej deklaracji „kompatybilne”.

Wymagania mają być związane z potrzebą i proporcjonalne. Przy wskazaniu istniejącego środowiska OrchestraOS/Orchestra należy przekazać potrzebne interfejsy, warunki dostępu do komponentów i kryteria oceny. Stosowanie nazw własnych i równoważności w konkretnym OPZ wymaga oceny według art. 99 i 101 Prawa zamówień publicznych. Sam zwrot „lub równoważny” nie zastępuje mierzalnych kryteriów.

## Najpierw przedmiot dostawy

| Przedmiot | Co trzeba rozdzielić |
| --- | --- |
| Nowy punkt alarmowania | Syrena, sterownik, moduły, zasilanie, konstrukcja, integracja, konfiguracja i odbiór. |
| Adaptacja istniejącego punktu | Elementy zachowane po sprawdzeniu, brakujące wyposażenie i prace integracyjne. |
| Montaż sprzętu powierzonego | Zakres już dostarczony oraz tylko brakujące materiały, połączenia i próby. |
| Sam sterownik | Zgodna platforma i jej interfejsy; bez automatycznego traktowania jako całego zestawu D. |
| Sama syrena | Właściwy tor wykonawczy i dokumentacja producenta P. |

Aplikację alarmową dostarcza KG PSP. Wykonawca zapewnia środowisko, instalację wskazanego pakietu i integrację sprzętową; nie zamawia się u niego opracowania odrębnej logiki alarmowania. Nie wycenia się drugi raz sprzętu posiadanego ani świadczeń zapewnianych centralnie.

## Dobór zdolności

Klasa I obejmuje wspólny rdzeń. I + 1.5 jest profilem kompaktowym z lokalnym audio; I + II profilem rozszerzonym. III dodaje lokalny TTS, także do 1.5, przy zachowaniu właściwej liczby I/O. Zasoby głosu nie zwiększają automatycznie liczby styków. Wiążąca jest [macierz Z3](Z3-WYMAGANIA-MINIMALNE.md#macierz-wyposażenia).

W opisie należy wskazać modelową konfigurację funkcjonalną, nie nazwę handlową sprzętu. Opcje niezbędne do spełnienia wymagań mają wejść do oferty. PTT jest funkcją jednego ze styków, jeśli tak przewiduje karta; nie stanowi automatycznie dodatkowego przekaźnika.

## Proponowany zapis platformy

> Dostawca zapewni sterownik zgodny z systemem KG PSP i wskazanym profilem Z3, z systemem Linux opartym na Yocto Project i OrchestraOS wydania KG PSP. KG PSP udostępni na wniosek wersjonowane komponenty i warunki integracji. Wykonawca dostosuje BSP, rozruch, sterowniki i konfigurację do swojej płyty, zbuduje oraz udokumentuje obraz i zapewni jego utrzymanie.

> Urządzenie będzie współpracować z właściwą instancją Orchestra KG PSP: indywidualna tożsamość, rejestracja, konfiguracja, telemetria, wersje, dostęp i podpisane aktualizacje RAUC w układzie A/B. Dane aplikacji i historia pozostaną zachowane przy aktualizacji i odtworzeniu. Przekazanie źródeł nie obejmuje automatycznie prywatnych kluczy produkcyjnych.

> Wykonawca zapewni udokumentowany lokalny kontrakt sprzętowy i uruchomienie pakietu aplikacji KG PSP bez zmiany jego logiki oraz bez obchodzenia zabezpieczeń. Przekaże manifest, SBOM, instrukcję odtworzenia budowy, wyniki prób i dokumentację utrzymania.

Podstawa: W-F01–W-F19 w właściwym zakresie, W-I08/09 i [platforma KG PSP](../PLATFORMA_KG_PSP.md). Warunki udostępnienia pakietu muszą być znane wykonawcom przed zobowiązaniem do integracji.

## Łączność i rozbudowa

> Zestaw zapewni własny LTE/IP oraz SMS MO/MT, wymagane Ethernet, Wi-Fi, GNSS i radio zgodnie z profilem. Wymagane anteny i opcje będą dostarczone oraz uruchomione. Zakres SIM, danych, SMS i ich kosztów zostanie rozdzielony od samego modemu.

> W fazie 2026–2028 zestaw zachowa gotowość GSM/LTE. Przygotowanie TETRA obejmie obsługiwane porty, miejsce, moc, antenę i adapter. Przełączenie TETRA na drogę podstawową nastąpi po odrębnym odbiorze; GSM pozostanie aktywnym zapasem. Odbiór docelowy wykaże sterowanie przy odłączonym GSM i internecie obiektu.

Podstawa: W-D01–W-D26. Nie zakłada się, że modem syreny jest automatycznie dostępny aplikacji sterownika. Odrębny zapas SMS w syrenie wymaga osobnego ujęcia, usług i arbitrażu. Bramka LoRaWAN nie jest wymagana po jednej sztuce na każdą syrenę bez projektu sieci.

## Tor wykonawczy

> Wykonawca określi i odbierze właściwy tor: lokalne audio i osobne PTT, udokumentowane API albo izolowaną aparaturę silnikową. Funkcje ALARM i ODWOLANIE będą rozróżnione; anulowanie oczekującej akcji lub techniczne STOP nie zastąpią sygnału odwołania.

> Dla toru elektronicznego wymagane zasoby będą znajdować się lokalnie przed alarmem, z zatwierdzonym manifestem i kontrolą integralności. Wariant API zmieniający miejsce plików lub używający generatora wymaga jawnego profilu i odbioru. Dla silnika zapewni się właściwy program, izolację, odcięcie i niezależny nadzór czasu.

Podstawa: W-C01–W-C17 i W-E01–W-E14. Moc i zasięg akustyczny, konstrukcję i parametry instalacji określa projekt obiektu. Nazwy zacisków jednego modelu nie są standardem dla innych urządzeń.

## Zasilanie i zachowanie instalacji

> Bilans obejmie rzeczywiste elementy zestawu oraz rezerwę rozbudowy. Podtrzymanie sterownika i łączności nie będzie utożsamiane z zasilaniem wzmacniacza albo silnika. Profil obciążenia, czasy i kryteria zostaną wskazane przed odbiorem.

> Integracja zachowa wymagane lokalne i dotychczasowe tory. Wspólny arbitraż będzie rozróżniał odrzucenie, odroczenie i duplikat. Po błędzie lub restarcie nie nastąpi samoczynne wznowienie starej emisji. Blokady bezpieczeństwa mają pierwszeństwo.

Podstawa: części H, J i K Z3. Obudowy, zabezpieczenia i warunki pracy dobiera się do zakresu oraz obiektu. Nie kopiuje się wszystkich parametrów zestawu rozbudowanego do małego modułu bez uzasadnienia.

## Dokumenty i kryteria odbioru

Umowa określa wersje wytycznych i profili, wymagany pakiet zgodności, interfejsy, prawa i okres wsparcia. Odbiór konfiguracji modelu, egzemplarza, aplikacji, kanałów i obiektu jest rozdzielony. Scenariusze Z10 obejmują negatywne próby autoryzacji, czasu i adresata oraz błędy zasilania i aktualizacji.

Nie dopuszcza się wymaganej funkcji, której nie wykonano albo dla której nie ma dowodu. Brak wsparcia w kontrakcie centrali jest zależnością do zamknięcia przed odbiorem tej funkcji, nie pozwoleniem na zmianę znaczenia innej komendy. Wypełniona karta Z9 i sekrety nie trafiają do publicznego repozytorium.

## Postanowienia do unikania

Ogólna „zgodność z SOiA” bez profilu i prób; utożsamienie „TTS ready” z działającym głosem; automatyczne wymaganie sześciu styków od profilu 1.5; policzenie PTT podwójnie; zamówienie samej możliwości doposażenia zamiast wymaganych opcji; uznanie SIM za provisioning; przekazanie całej logiki alarmowej producentowi urządzenia; uznanie online lub ACK za dowód emisji.
