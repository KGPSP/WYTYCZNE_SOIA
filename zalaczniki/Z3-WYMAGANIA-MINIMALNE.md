---
tytuł: "Załącznik nr 3 — Wymagania minimalne dla urządzenia"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 3 — Wymagania minimalne dla urządzenia

## Zakres i pierwszeństwo wymagań

Wymagania dotyczą nowej platformy sterującej włączanej do zarządzanego systemu KG PSP oraz właściwego zakresu modernizacji. Publiczny odczyt IoT Feed pozostaje otwarty. Możliwość zbudowania własnego czytnika feedu nie oznacza zgodności zakupowej ani dopuszczenia punktu alarmowego według tego załącznika.

**MUSI** oznacza warunek konieczny w wybranym zakresie. **POWINIEN** oznacza zalecenie, którego pominięcie należy uzasadnić w karcie. Braku wymaganej funkcji nie oznacza się jako „nie dotyczy”. Każde wymaganie ocenia się na rzeczywistej konfiguracji, z dowodem, bez automatycznego uznania modelu lub nazwy handlowej za zgodny.

Wspólną platformę opisuje [OrchestraOS i provisioning KG PSP](../PLATFORMA_KG_PSP.md). Nazwy OrchestraOS, Orchestra Manager, Orchestra SDN, Yocto i RAUC identyfikują wymagane środowisko współpracy. Sprzęt, BSP i wykonawcę dobiera się konkurencyjnie; kryteria równoważności oraz uzasadnienie wymagań ujmuje konkretne zamówienie. Aplikację alarmową zapewnia KG PSP, a wykonawca dostarcza kompatybilną platformę i interfejsy.

## Klasy zdolności i profil 1.5

| Oznaczenie | Zakres | Zastosowanie |
| --- | --- | --- |
| **I** | Wspólny rdzeń platformy, bezpieczeństwa i wykonania | Obowiązuje wszystkie zgodne sterowniki; nie wymaga automatycznie wyposażenia rozszerzonego. |
| **1.5** | Kompaktowy profil z lokalnym audio | Dodawany do I dla mniejszej liczby torów. Zachowuje wymagania jakości audio i ochrony; TTS nie jest obowiązkowy. |
| **II** | Rozszerzony profil z lokalnym audio | Dodawany do I, gdy potrzebna jest większa liczba portów i I/O. |
| **III** | Lokalna synteza mowy | Dodawana po zamówieniu TTS, także do konfiguracji 1.5. Wymaga większych zasobów, lecz sama nie zwiększa liczby I/O. |
| **D** | Kompletny zestaw i montaż | Zakres dostawy, nie klasa zdolności. |
| **P** | Wymagania wobec producenta syreny | Stosowane do właściwej części wykonawczej. |

Zestaw I + 1.5 nie musi mieć czterech Ethernetów ani sześciu styków. Wspólne wymagania I obowiązują w nim w całości, z liczbami portów określonymi poniżej. Funkcje audio oznaczone **1.5 / II** dotyczą obu profili. I + 1.5 + III ma zasoby TTS z W-F07/08, a liczbę I/O nadal dobiera się z profilu kompaktowego. Nie wprowadza się odrębnej klasy 2.5.

Klasa zdolności nie jest `deviceClass` w komendzie ani wersją profilu IoT. Oznaczenie 1.5 nie zmienia wartości `SIREN_CONTROLLER`, profilu `0.1` lub słownika publikowanego przez centralę. Profil elektroniczny/silnikowy i tryb AUDIO/PTT/API/stykowy są osobnymi osiami opisanymi w Z5.

### Macierz wyposażenia

| Element | I — rdzeń | I + 1.5 — kompaktowy | I + II — rozszerzony |
| --- | --- | --- | --- |
| OrchestraOS, Yocto, aplikacja KG PSP i provisioning | Wymagane | Wymagane | Wymagane |
| Ethernet | Minimum 1 | Minimum 1; bez obowiązku osobnego managed switch | Minimum 4 zarządzalne tory |
| LTE/IP, SMS MO/MT, SIM i antena | Wymagane | Wymagane | Wymagane |
| Wi-Fi, GNSS, LoRa/LoRaWAN | Zgodnie z W-D08/10/16 | Dostarczone wymagane moduły i anteny | Zgodnie z W-D08/10/16 |
| Styki bezpotencjałowe | Minimum 2 | Minimum 2; PTT może używać jednego | Minimum 6; PTT może używać jednego |
| GPI / GPO | Według karty | Minimum 2 / 2 | Minimum 6 / 6 |
| RS-232 / USB | Bilans torów i rozbudowy | Minimum 2 pełne RS-232 i 2 USB | Liczba według karty oraz planu rozbudowy |
| Lokalne audio | Gdy wybrano profil audio | Dwa kanały LINE OUT, osobne PTT i lokalny pakiet | Te same wymagania audio |
| Pamięć audio | Dla profilu audio | Minimum 32 MB i miejsce na dwie wersje pakietu | Tak samo |
| TTS | Po zamówieniu III | Niewymagany; po dodaniu III wymagania głosowe | Po zamówieniu III |
| Odcięcie, watchdog, historia i autoryzacja | Wymagane | Wymagane | Wymagane |

Minima portów, styków i GPI/GPO profilu 1.5 dotyczą także dostawy samego sterownika. Zakres D dodatkowo obejmuje kompletny zestaw i montaż. RS-232, USB, audio oraz interfejs terminala muszą być rzeczywiście dostępne z systemu. Wspólne złącze nie może zostać policzone jako dwa niezależne tory używane równocześnie. Wejście audio, dodatkowe I/O i kolejne moduły ujmuje się jawnie w karcie. Dla potrzeb wskazanych przez KG PSP opcja Audio IN ma być dostarczona i odebrana, a nie jedynie wymieniona jako możliwość przyszłego zakupu.

W profilu silnikowym zdolność audio platformy może pozostać niewykorzystana. Dźwięk tworzy silnik z wirnikiem; wymagania plików i TTS nie są sposobem jego sterowania. Dwa wyjścia mogą służyć funkcjom RUN/CYKL, lecz nazwy i parametry muszą zostać zmapowane na konkretny sprzęt.

## A. Weryfikacja polecenia

Droga komunikacji nie jest uprawnieniem do uruchomienia. IoT Feed wymaga podpisu i kwalifikacji całej koperty; SMS lub radio stosują własny, jawny kontrakt. Nowy kanał nie tworzy drugiej logiki alarmowania.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-A01 | MUSI | **I** | Zweryfikować podpis odebranej treści przed jakimkolwiek działaniem wykonawczym |
| W-A02 | MUSI | **I** | Odrzucić całą treść przy niepowodzeniu weryfikacji — nie wykonywać jej części |
| W-A03 | MUSI | **I** | Rozpoznawać identyfikator klucza i odrzucać treść podpisaną kluczem nieznanym |
| W-A04 | MUSI | **I** | Obsługiwać kontrolowaną zmianę zaufanych kluczy z oknem nakładania, zakresem ważności i możliwością odwołania. Sam nieznany identyfikator w feedzie nie upoważnia do zaufania nowemu kluczowi. |
| W-A05 | MUSI | **I** | Sprawdzić zgodność profilu, środowiska i wersji słowników |
| W-A06 | MUSI | **I** | Odrzucić treść po upływie jej terminu ważności, niezależnie od stanu łączności |
| W-A07 | MUSI | **I** | Wykonać wyłącznie polecenia skierowane do własnej klasy urządzenia |
| W-A08 | MUSI | **I** | Odrzucić kod sygnału, którego nie zna, **nie przerywając obsługi pozostałych poleceń** |
| W-A09 | MUSI | **I** | Rozpocząć emisję wyłącznie w oknie rozpoczęcia wskazanym w poleceniu |
| W-A10 | MUSI | **I** | Zapewnić, że to samo polecenie — odebrane ponownie, innym kanałem albo po restarcie — nie spowoduje drugiej emisji |
| W-A11 | MUSI | **I** | Zachować ochronę przed powtórzeniem po zaniku zasilania |
| W-A12 | MUSI | **I** | Traktować każdą wątpliwość jako powód niewykonania polecenia (fail-closed) |
| W-A13 | MUSI | **I** | Odmówić wykonania polecenia przy dryfie zegara przekraczającym **30 sekund** względem czasu odniesienia |
| W-A14 | POWINIEN | **I** | Zapisywać w rejestrze zdarzeń wynik każdej weryfikacji, także zakończonej odmową, wraz z przyczyną |
| W-A15 | MUSI | **I** | Utrzymywać wiarygodny czas z co najmniej dwóch źródeł wskazanych w profilu KG PSP, mieć zegar podtrzymywany, znać wiek synchronizacji i sygnalizować przekroczenie doby. Utrata wiarygodności czasu blokuje nowe wykonanie. |
| W-A16 | POWINIEN | **I** | Rozróżniać przyjęcie, start, zakończenie, błąd i niepewny wynik zgodnie z profilem odpowiedzi. Test bez emisji ma własny wynik; ACK nie zastępuje pomiaru efektu. |
| W-A17 | MUSI | **I** | Stosować udokumentowane limity rozmiaru odpowiedzi i polecenia, zgodne z kontraktem oraz zasobami. Przekroczenie jest błędem, nie pustą listą. Brak limitu w metadanych API wymaga uzupełnienia profilu integracji przed odbiorem. |

## B. Obszar działania

TERC określa administracyjnego adresata niezależnego toru. Nie jest obliczeniem akustycznego zasięgu syreny. Wiele geokodów polecenia porównuje się z przypisaniem danego toru.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-B01 | MUSI | **I** | Przypisać każdemu niezależnemu torowi wykonawczemu dokładnie jeden siedmiocyfrowy TERC gminy. Wiele torów wymaga jawnej mapy tor–TERC; zasięg akustyczny poza gminą nie tworzy dodatkowego adresata. |
| W-B02 | MUSI | **I** | Odrzucić konfigurację toru kodem dwucyfrowym albo czterocyfrowym lub oznaczyć błąd uniemożliwiający dopuszczenie toru do wykonania. |
| W-B03 | MUSI | **I** | Odrzucić kod sześciocyfrowy, bez cyfry rodzaju, jako niepełny |
| W-B04 | MUSI | **I** | Uwzględniać cyfrę rodzaju gminy: kod gminy miejsko-wiejskiej obejmuje jej miasto i jej obszar wiejski, a te dwa są względem siebie rozłączne |
| W-B05 | MUSI | **I** | Pomijać kody miejscowości i ulic — mają własną numerację i porównanie prefiksowe daje trafienia przypadkowe |
| W-B06 | MUSI | **I** | Uruchamiać wyłącznie tor, którego przypisany TERC jest objęty geokodem polecenia. Dopasowanie jednego toru nie uruchamia pozostałych torów urządzenia. |
| W-B07 | MUSI | **I** | Traktować kod nierozpoznany — o innej długości albo nienumeryczny — jako brak dopasowania; nigdy nie „naprawiać” go przez obcięcie ani dopełnienie |
| W-B08 | POWINIEN | **I** | Udostępniać skonfigurowany obszar do odczytu w rejestrze zdarzeń i w eksporcie konfiguracji |

## C. Sygnały i komunikaty

Nominalne sygnały określa katalog Z4. Lokalny pakiet audio i program silnikowy mają oddzielną postać. Wymagane zasoby muszą być gotowe przed przyjęciem polecenia, niezależnie od dostępności internetu.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-C01 | MUSI | **I** | Obsługiwać co najmniej ogłoszenie i odwołanie alarmu dla ludności; pozostałe funkcje katalogu zgodnie z profilem zastosowania i uprawnieniami. Zdolność lokalna nie potwierdza dostępności komendy centralnej. |
| W-C02 | MUSI | **1.5 / II** | Dla sygnałów alarmowych odtwarzać wyłącznie niezmodyfikowane pliki referencyjne; zatwierdzone nagrania słowne i TTS mają odrębny zakres. |
| W-C03 | MUSI | **I** | Przed instalacją i użyciem plików potwierdzać ich zgodność z zatwierdzonym pakietem i manifestem KG PSP. Dla profilu silnikowego weryfikować wersję programu wykonawczego; suma z przypadkowej kopii dokumentu nie jest kotwicą zaufania. |
| W-C04 | MUSI | **1.5 / II** | Obsługiwać zatwierdzony format pakietu audio, w tym WAV PCM 16 bit mono o próbkowaniu co najmniej 8 kHz. Plików nie przeliczać ani nie skracać samodzielnie. |
| W-C05 | MUSI | **I** | Zachowywać nominalny czas sygnału z katalogu. Metoda pomiaru, tolerancja i niepewność muszą być wskazane w zatwierdzonym profilu odbioru; nie zmieniają nominalnych 180 s lub 60 s. |
| W-C06 | MUSI | **I** | Zachować strukturę czasową sygnału — modulację oraz liczbę i długość przerw |
| W-C07 | MUSI | **1.5 / II** | Utrzymać poziom w granicach ±3 dB względem wzorca, bez przesterowania, w zadeklarowanym i udokumentowanym punkcie pomiarowym |
| W-C08 | MUSI | **I** | Kończyć funkcję lokalnie po właściwym czasie. Oddzielnie nadzorować odtwarzanie i zwolnienie PTT, a dla silnika okno programu i odcięcie napędu; nadzór nie może zależeć wyłącznie od procesu odbiornika poleceń. |
| W-C09 | MUSI | **I** | Traktować odwołanie alarmu jako **emisję sygnału**, a nie jako zaprzestanie emisji |
| W-C10 | MUSI | **1.5 / II** | Przechowywać zatwierdzony pakiet lokalnie w pamięci trwałej, z miejscem na dwie wersje i co najmniej 32 MB na audio. Wykonanie alarmu nie może wymagać pobrania ani strumieniowania pliku. |
| W-C11 | MUSI | **III** | Zapewniać pełną ścieżkę od zatwierdzonego tekstu do zrozumiałej polskiej mowy, z prawem użycia silnika i głosu, kontrolą długości oraz wersjonowaniem. Sam odtwarzacz nagrań nie jest TTS. |
| W-C12 | MUSI | **III** | Wykonywać zamówioną syntezę lokalnie, bez zależności od usługi zewnętrznej w chwili wykonania. |
| W-C13 | POWINIEN | **III** | Syntezować komunikat **do bufora przed rozpoczęciem odtwarzania**, nigdy w trakcie emisji |
| W-C14 | POWINIEN | **III** | Zapewniać powtarzalność: ten sam tekst przy tej samej wersji modelu daje ten sam dźwięk |
| W-C15 | POWINIEN | **III** | Przypinać i odnotowywać w rejestrze zdarzeń wersję modelu i głosu |
| W-C16 | POWINIEN | **III** | Umożliwiać nadpisanie wymowy nazw miejscowości, skrótów, jednostek, liczb, dat i godzin |
| W-C17 | MUSI | **III** | Zapewnić, że komunikat głosowy **nigdy nie opóźnia ani nie zastępuje** sygnału akustycznego z pliku referencyjnego |

## D. Kanały i łączność

W fazie 2026–2028 podstawowa łączność zestawu jest komórkowa GSM/LTE, a SMS jest zapasem. Ethernet i Wi-Fi mogą zapewniać dodatkową drogę IP. Po tej fazie TETRA ma być podstawowym kanałem poleceń, po odbiorze lokalizacji; GSM pozostaje aktywnym zapasem. Zmiana SIM i APN jest osobnym procesem od integracji TETRA.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-D01 | MUSI | **I** | W normalnej pracy pobierać podpisany wykaz co 30 s między początkami żądań, z rozłożeniem faz urządzeń. Odpowiedź 429, Retry-After i błąd uruchamiają kontrolowane odroczenie zgodnie z Z6. |
| W-D02 | MUSI | **I** | Stosować warunkowe pobranie przez ETag/If-None-Match; odpowiedź 304 nie odnawia podpisanej ważności zachowanej kopii. |
| W-D03 | MUSI | **I** | Honorować odpowiedź o przekroczeniu limitu zapytań wraz ze wskazanym czasem wstrzymania |
| W-D04 | MUSI | **I** | Stosować kontrolowane wycofanie po błędach i losowe rozproszenie momentu odpytania |
| W-D05 | MUSI | **I** | Utrzymywać cykliczne pobieranie **także wtedy**, gdy działa kanał niezwłocznego powiadomienia |
| W-D06 | MUSI | **I** | Umożliwiać podłączenie do sieci lokalnej obiektu przewodowo, bez modemu i bez karty abonenckiej |
| W-D07 | MUSI | **I** | Udostępniać co najmniej jeden zarządzalny interfejs Ethernet w rdzeniu I i profilu 1.5; dla rozszerzonego profilu II co najmniej cztery tory. Udokumentować stan, konfigurację i separację. Profil 1.5 nie wymaga osobnego przełącznika zarządzalnego. |
| W-D08 | MUSI | **I** | Zapewniać Wi-Fi z obsługą zabezpieczeń wskazanych w profilu KG PSP i samoczynnym powrotem do połączenia. Wymaganą opcję dostarczyć i uruchomić; nie zastępuje jej samo gniazdo rozszerzeń. |
| W-D09 | MUSI | **I** | Zapewniać udokumentowany interfejs danych dla stacji radiowej lub przyszłego terminala TETRA, niezależny funkcjonalnie od audio/PTT. Bilans portów i zgodny adapter określa karta; samo złącze nie potwierdza działania protokołu. |
| W-D10 | MUSI | **I** | Zapewniać LoRa/LoRaWAN jako urządzenie końcowe interoperacyjne z profilem serwera sieciowego wskazanym przez KG PSP. Bramka i jej onboarding są osobnym zakresem dostawy. |
| W-D11 | MUSI | **I** | Posiadać własny modem komórkowy LTE z transmisją IP oraz SMS przychodzącymi i wychodzącymi, anteną i obsługą SIM, bez blokady operatorskiej. Udostępniać aplikacji pełną treść i metadane. |
| W-D12 | MUSI | **I** | Umożliwiać wymianę karty abonenckiej oraz samodzielną konfigurację parametrów dostępu do sieci |
| W-D13 | MUSI | **I** | Dla SMS stosować walidację właściwego kontraktu, uprawnienia nadawców, kontrolę treści, historii i ważności oraz rejestrację bez ujawniania sekretów. Nowy profil aplikacji KG PSP wymaga kryptograficznej autentyczności i integralności treści. |
| W-D14 | MUSI | **I** | Nie wykonywać ponownie tej samej operacji odebranej przez SMS lub inny kanał. Wspólne ID i trwałą historię określa kontrakt; starego SMS bez ID nie uznawać za pełną deduplikację między kanałami. |
| W-D15 | MUSI | **I** | Przyjmować **konfigurowalny** adres punktu dostępu, adres kanału powiadomienia i numery uprawnione |
| W-D16 | MUSI | **I** | Posiadać wielokonstelacyjny moduł pozycjonowania satelitarnego z odczytem współrzędnych i statusu ustalenia pozycji |
| W-D17 | POWINIEN | **I** | Kontynuować pracę na kanale zapasowym przy utracie kanału podstawowego, bez zmiany zakresu weryfikacji |
| W-D18 | MUSI | **I** | Stosować indywidualne sekrety uwierzytelniające urządzenia. W starszym profilu z hasłem kod jest unikalny, lecz nie zastępuje podpisu/MAC; w nowym profilu sposób ochrony określa kontrakt aplikacji KG PSP. |
| W-D19 | MUSI | **I** | Rejestrować odrzucenia SMS wraz z przyczyną i metadanymi potrzebnymi do audytu, maskując hasła i inne sekrety także w zapisanej treści. |
| W-D20 | MUSI | **I** | Przyjąć bez wymiany sprzętu kartę abonencką i konfigurację sieci wydzielonej wprowadzane w fazie docelowej |
| W-D21 | MUSI | **D** | Posiadać gniazdo wymiennej karty abonenckiej **dostępne bez demontażu urządzenia z uchwytu**, z mocowaniem zabezpieczającym kartę przed wysunięciem przy drganiach; dokumentacja wskazuje, czy wymiana wymaga wyłączenia urządzenia |
| W-D22 | POWINIEN | **D** | Obsługiwać kartę klasy przemysłowej — o rozszerzonym zakresie temperatur pracy i podwyższonej wytrzymałości zapisu względem karty konsumenckiej |
| W-D23 | POWINIEN | **D** | Obsługiwać kartę zdalnie prowizjonowaną, w postaci wymiennej lub wlutowanej |
| W-D24 | MUSI | **I** | Udostępniać aplikacji pełne SMS i metadane części. Profil wykonawczy określa kodowanie, limit części, rozmiaru i czasu kompletowania; nie wykonywać fragmentu. Profil dopuszczający tylko jedną wiadomość odrzuca multipart. |
| W-D25 | MUSI | **I** | Weryfikować integralność i autentyczność całego nowego polecenia SMS, jego tożsamość operacji, adresata i ważność oraz trwałą ochronę przed odtworzeniem. Pola czasu i licznika bez uwierzytelnienia nie zapewniają tej ochrony. |
| W-D26 | MUSI | **I** | Przewidzieć rozbudowę o terminal TETRA: obsługiwany port, miejsce, moc i antenę oraz wersjonowany adapter. Docelową usługę i drogę centralną odbiera się oddzielnie, także przy odłączonym GSM i internecie obiektu. |

## E. Wysterowanie syreny

Dobiera się tor zgodny z funkcją i udokumentowanym wejściem syreny. AUDIO/PTT, API oraz sterowanie silnikiem nie są zamiennymi sposobami połączenia zacisków. Zasady zakończenia, odcięcia i arbitrażu zawiera Z5.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-E01 | MUSI | **I** | Zapewniać rozróżnialne wykonanie ogłoszenia i odwołania przez właściwy tor lokalny. Dwie funkcje nie oznaczają automatycznie dwóch osobnych metod integracji ani dwóch dodatkowych przekaźników. |
| W-E02 | MUSI | **1.5 / II** | Posiadać wyjście audio liniowe o poziomie nie niższym niż 1,0 V RMS, **z zadeklarowaną tolerancją** i **regulacją poziomu realizowaną programowo** — nie elementem regulacyjnym na płycie — o impedancji wyjściowej nie większej niż 50 Ω, stosunku sygnału do szumu nie gorszym niż 90 dB i zniekształceniach nie większych niż 0,1 %, z dwoma kanałami przypisywanymi programowo niezależnie |
| W-E03 | MUSI | **I** | Zapewniać co najmniej dwa niezależne bezpotencjałowe tory NO/NC/COM w rdzeniu I i profilu 1.5, a co najmniej sześć w rozszerzonym profilu II. Napięcie, prąd, izolację i trwałość dobrać do interfejsu oraz cyklu pracy; nie prowadzić prądu silnika przez styki sterownika. |
| W-E04 | MUSI | **I** | Zapewnić izolację torów sterowania od niebezpiecznych napięć i ochronę serwisową odpowiednią do zastosowania. Gdy obiekt wymaga 230 V, stosować właściwą izolowaną aparaturę wykonawczą; mały sterownik może pracować wyłącznie po stronie sygnałowej. |
| W-E05 | MUSI | **1.5 / II** | Sterować PTT osobno od audio, z udokumentowanymi parametrami. PTT może wykorzystywać jeden z już policzonych przekaźników; nie wymaga automatycznie trzeciego albo siódmego styku. |
| W-E06 | MUSI | **I** | Nie sterować obwodem mocy syreny silnikowej bezpośrednio z wyjść ogólnego przeznaczenia — wyłącznie przez certyfikowaną, izolowaną warstwę wykonawczą |
| W-E07 | MUSI | **I** | Ograniczać niezależnie od procesu aplikacji maksymalne okno zasilania napędu syreny silnikowej, z kontrolą programu i bez samoczynnego wznowienia po awarii. |
| W-E08 | MUSI | **I** | Posiadać lokalne, sprzętowe **odcięcie** toru wykonawczego, niezależne od łączności i od oprogramowania, mające pierwszeństwo przed poleceniem zdalnym |
| W-E09 | MUSI | **I** | Nie wznawiać samoczynnie przerwanej emisji po niekontrolowanym restarcie |
| W-E10 | MUSI | **1.5 / II** | Umożliwiać sterowanie syreną elektroniczną przez lokalne audio i osobne PTT. Wejście MIC wymaga właściwego dopasowania poziomu i izolacji; zgodność wynika z dokumentacji konkretnego interfejsu, nie kształtu gniazda. |
| W-E11 | POWINIEN | **I** | Wykrywać stan układu wykonawczego — obecność obciążenia, gotowość wzmacniacza, stan stycznika |
| W-E12 | POWINIEN | **I** | Rozróżniać w rejestrze zdarzeń przyjęcie polecenia, zaplanowanie akcji, aktywowanie wyjścia, wykrycie obciążenia i zakończenie emisji |
| W-E13 | MUSI | **I** | Izolować zwarcie lub przeciążenie obwodu obiektowego, zachowując pracę sterownika i pozostałych sprawnych torów. Uszkodzony tor zgłaszać jako błąd, bez deklarowania jego zdolności emisji. |
| W-E14 | MUSI | **I** | Wykrywać na wejściu uruchomienia lokalnego impuls o czasie trwania nie dłuższym niż **200 ms** i podać w dokumentacji częstotliwość próbkowania wejść |

## F. Platforma i cykl życia

KG PSP udostępnia na wniosek wersjonowane komponenty do budowy Yocto/OrchestraOS. Wykonawca buduje, utrzymuje i dokumentuje obraz dla swojej płyty, zapewnia integrację z Orchestra i lokalne interfejsy. KG PSP dostarcza aplikację alarmową. Szczegóły procesu opisuje dokument platformy.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-F01 | MUSI | **I** | Uruchamiać utrzymywany dla konkretnej płyty Linux oparty na Yocto Project i OrchestraOS wydania KG PSP. Zapewniać wersjonowane aktualizacje bezpieczeństwa oraz odtworzenie dopuszczonej wersji przez deklarowany okres wsparcia. |
| W-F02 | MUSI | **I** | Umożliwiać aktualizację **bez dostępu do publicznego Internetu**, z zachowaniem podpisów |
| W-F03 | MUSI | **I** | Utwardzić konfigurację: wyłączyć zbędne usługi i konta domyślne, ograniczyć porty i dostęp serwisowy/debugowy. Urządzenie eksploatowane nie może udostępniać trybu obchodzącego wymagane zabezpieczenia. |
| W-F04 | MUSI | **I** | Udostępniać zdalny dostęp administracyjny wyłącznie z uwierzytelnieniem kluczem; hasło nie może być jedynym mechanizmem |
| W-F05 | MUSI | **I** | Chronić indywidualne klucze prywatne i sekrety w nieeksportowalnym magazynie sprzętowym lub bezpiecznej enklawie. Odmawiać uruchomienia nieautoryzowanego obrazu, także po podmianie nośnika. Publiczne klucze weryfikacji mogą być wspólne. Model zagrożeń obejmuje również szynę procesor–radio: ochronę treści i kluczy przed odczytem, wstrzyknięciem oraz odtworzeniem. |
| W-F06 | MUSI | **I** | Posiadać sprzętowy układ nadzoru pracy, samoczynnie restartujący urządzenie przy zawieszeniu oprogramowania |
| W-F07 | MUSI | **III** | Mieć procesor 64-bitowy o co najmniej **czterech rdzeniach** i taktowaniu nie mniejszym niż **1,5 GHz** |
| W-F08 | MUSI | **III** | Mieć co najmniej **4 GB** pamięci operacyjnej i co najmniej **32 GB** pamięci trwałej klasy przemysłowej |
| W-F09 | MUSI | **I** | Rozdzielić buforowane i rotowane logi diagnostyczne od trwałego transakcyjnego zapisu historii poleceń. Stan decydujący o jednokrotnym wykonaniu zapisać przed aktywacją wyjścia; okresowa synchronizacja nie zastępuje tego zapisu. |
| W-F10 | MUSI | **I** | Obsługiwać podpisane RAUC bundle zgodne z instancją KG PSP, dwa zestawy partycji A/B i kontrolowany rollback. Zachować odrębne dane aplikacji, tożsamość i historię poleceń. Podpis aktualizacji nie zastępuje ochrony rozruchu. |
| W-F11 | MUSI | **I** | Zapewniać wersjonowany lokalny kontrakt sprzętowy dostępny z aplikacji KG PSP: metody, pola, jednostki, statusy, błędy i uprawnienia. Wykonawca dostarcza potrzebny adapter dla swojej płyty. |
| W-F12 | MUSI | **I** | Uruchamiać wskazany pakiet aplikacji KG PSP, z autostartem, nadzorem, trwałym obszarem danych i uprawnieniami do interfejsów, bez zmiany pakietu i bez obchodzenia zabezpieczeń. |
| W-F13 | MUSI | **D** | Zapewniać udokumentowane porty rozszerzeń i co najmniej 2 GPI oraz 2 GPO dla zestawu kompaktowego, a 6 GPI i 6 GPO dla zestawu rozszerzonego II. Liczyć oddzielnie styki, GPI/GPO i zajęcie PTT; klasa III sama nie zwiększa liczby I/O. |
| W-F14 | MUSI | **I** | Udostępnić **udokumentowaną procedurę przekazania właścicielowi zdolności podpisywania obrazów** albo depozyt kluczy podpisujących — tak, żeby weryfikacja rozruchu z W-F05 nie zamykała urządzenia trwale u producenta |
| W-F15 | MUSI | **I** | Budować obraz z komponentów Yocto/OrchestraOS udostępnionych przez KG PSP na wniosek, dla wskazanej płyty i BSP. Przekazać manifest, wersje, konfigurację, zmiany, artefakty i instrukcję odtworzenia budowy. |
| W-F16 | MUSI | **I** | Przeprowadzić chroniony provisioning indywidualnej tożsamości i rejestrację we właściwej instancji Orchestra KG PSP. Wykazać identyfikację, konfigurację, telemetrię, wersje, aktualizację i odwołanie dostępu. |
| W-F17 | MUSI | **I** | Zapewnić uwierzytelnione zarządzanie przed instalacją aplikacji KG PSP, z ograniczonymi rolami i bez publicznego panelu lub powłoki. Rozdzielić certyfikaty urządzenia, zaufanie feedu i klucze podpisywania obrazów. |
| W-F18 | MUSI | **I** | Powiązać model, rewizję, obraz, adaptery, pakiet aplikacji i egzemplarz z kartą obiektu. Flota aktualizacyjna nie zmienia samodzielnie TERC ani uprawnień do alarmowania. |
| W-F19 | MUSI | **1.5** | Zapewnić co najmniej 64-bitowy procesor o 2 rdzeniach, 2 GB RAM i 16 GB przemysłowej pamięci trwałej oraz działającą konfigurację z macierzy 1.5. Wykazać bilans OS A/B, aplikacji, danych i rezerwy; wyższe wymagania klasy III obowiązują przy jej zamówieniu. |

## G. Tryby pracy i dowody

Dziennik ma odróżniać przyjęcie, wykonanie lokalne, zmierzony efekt oraz brak dowodu. Utrata łączności zarządczej nie jest dowodem awarii syreny, a stan online nie potwierdza emisji.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-G01 | MUSI | **I** | Rozróżniać tryby: pracy operacyjnej, ćwiczebny, serwisowy, zablokowany, ograniczony i awaryjny |
| W-G02 | MUSI | **I** | Blokować zdalne wykonanie w trybie serwisowym i zablokowanym. Test lokalny w serwisie wymaga właściwych uprawnień; nie może omijać aktywnego odcięcia ani blokady bezpieczeństwa. |
| W-G03 | MUSI | **I** | **Nie przełączać się samoczynnie** z trybu serwisowego lub zablokowanego do operacyjnego po restarcie |
| W-G04 | MUSI | **I** | Odnotowywać zmianę trybu w rejestrze zdarzeń wraz z czasem i przyczyną |
| W-G05 | MUSI | **I** | Prowadzić lokalny rejestr zdarzeń obejmujący co najmniej: źródło polecenia, wynik weryfikacji, decyzję wykonania, zmianę stanu wyjścia, restart wraz z przyczyną, zmianę trybu, aktualizację i wymianę materiału kryptograficznego |
| W-G06 | MUSI | **I** | Udostępniać rejestr zdarzeń w formacie otwartym, możliwym do odczytu bez oprogramowania producenta |
| W-G07 | MUSI | **I** | Nie ujawniać w rejestrze kluczy prywatnych ani pełnych wartości sekretów |
| W-G08 | MUSI | **I** | Sygnalizować **bez otwierania obudowy i bez podłączania komputera** co najmniej: pracę z zasilania rezerwowego, niski stan magazynu energii, gotowość operacyjną oraz brak łączności |
| W-G08a | MUSI | **I** | Rozróżniać w sygnalizacji stan gotowości od stanu braku łączności — tak, żeby dało się je odróżnić bez odczytu rejestru |
| W-G09 | POWINIEN | **I** | Umożliwiać eksport pełnej konfiguracji urządzenia w formacie otwartym |
| W-G10 | POWINIEN | **I** | Umożliwiać wykonanie testu cichego, niepowodującego emisji zewnętrznej |
| W-G11 | MUSI | **I** | Zachować trwale i lokalnie historię decyzji oraz wyników, niezależnie od łączności. Restart nie usuwa niewysłanych zapisów potrzebnych do rozstrzygnięcia ponowienia. |
| W-G12 | MUSI | **I** | Zapewnić rejestrowi pojemność i okres przechowywania nie krótszy niż **dwanaście miesięcy** zwykłej eksploatacji, z nadpisywaniem najstarszych zapisów po jego wyczerpaniu |

## H. Zasilanie i warunki pracy

Bilans rozdziela sterownik, modem, bramkę, wzmacniacz i napęd. Podtrzymanie jednego elementu nie dowodzi gotowości całego punktu. Warunki obiektowe muszą mieścić się w deklarowanym zakresie lub wymagać odpowiedniej konfiguracji.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-H01 | MUSI | **D** | Zapewnić dla kompletnego zestawu sterowania i łączności minimum 10 h podtrzymania przy odbiorze i 8 h na końcu gwarancji, dla udokumentowanego profilu obciążenia obejmującego sterowanie emisją. Zasilanie wzmacniaczy i napędu ma osobny bilans; nie wynika z akumulatora sterownika. |
| W-H02 | MUSI | **D** | Określić model degradacji magazynu energii i przedłożyć świadectwo badania albo obliczenie dla profilu obciążenia z W-H01 |
| W-H03 | MUSI | **I** | Monitorować stan zasilania podstawowego i rezerwowego oraz odnotowywać jego zmiany |
| W-H04 | MUSI | **I** | Wykonać kontrolowane zamknięcie pracy przy wyczerpaniu zasilania rezerwowego |
| W-H05 | MUSI | **I** | Po powrocie zasilania odtworzyć stan trwały i **nie wykonywać polecenia, którego okno rozpoczęcia już minęło** |
| W-H06 | MUSI | **D** | Pracować w zakresie temperatur co najmniej od +10 °C do +40 °C przy wilgotności do 95 % bez kondensacji, w pomieszczeniu zamkniętym |
| W-H07 | POWINIEN | **D** | Udostępniać wykonanie o **rozszerzonym zakresie temperatur pracy**, co najmniej od −20 °C do +55 °C, dla zamawiających, u których warunki obiektowe nie mieszczą się w zakresie z W-H06 |
| W-H08 | POWINIEN | **I** | Sygnalizować przewidywany pozostały czas pracy na zasilaniu rezerwowym |
| W-H09 | MUSI | **I** | Określić i wykazać czas rozruchu platformy oraz uzyskania gotowości aplikacji dla wskazanej konfiguracji. Limit i warunki ustala się przed odbiorem; online w zarządzaniu nie jest dopuszczeniem syreny do emisji. |

## I. Interoperacyjność i prawa

Zgodność z Orchestra KG PSP nie oznacza zakupu sprzętu od jednego producenta. Warunki dostępu do komponentów, budowy, podpisywania, interfejsów i utrzymania muszą umożliwiać wykonanie zamówienia oraz późniejszą zmianę serwisu.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-I01 | MUSI | **I** | Zachować lokalne funkcje alarmowania przy niedostępności technicznego zarządzania Orchestra lub usługi producenta, jeśli polecenie dotarło właściwym kanałem i spełnia wszystkie warunki. Brak zarządzania nie tworzy nowego polecenia. |
| W-I02 | MUSI | **I** | Umożliwiać zmianę adresu punktu dostępu, kanału powiadomienia i punktu zaufania bez udziału producenta |
| W-I03 | MUSI | **I** | Umożliwiać wyłączenie i włączenie poszczególnych kanałów |
| W-I04 | MUSI | **I** | Umożliwiać wymianę karty abonenckiej bez utraty gwarancji i bez wizyty serwisu producenta |
| W-I05 | MUSI | **I** | Nie wymagać stałego abonamentu u producenta dla podstawowego alarmowania |
| W-I06 | MUSI | **I** | Nie współdzielić między egzemplarzami indywidualnych kluczy prywatnych ani sekretów urządzeń. Wspólne publiczne klucze weryfikacji feedu, aktualizacji i rozruchu są dopuszczalne i nie są tożsamością egzemplarza. |
| W-I07 | MUSI | **I** | Udostępniać procedurę wymiany i odwołania materiału kryptograficznego |
| W-I08 | MUSI | **I** | Dostarczyć dokumentację interfejsów elektrycznych, audio i integracyjnych **wraz ze schematem elektrycznym** w zakresie umożliwiającym samodzielny serwis |
| W-I09 | MUSI | **I** | Dostarczać SBOM dla wydania oraz proces zgłaszania podatności, okres wsparcia i terminy poprawek. Prawa i zależności muszą pozwalać KG PSP utrzymywać system oraz powierzyć obsługę innemu wykonawcy. |
| W-I10 | POWINIEN | **I** | Wykazać w odbiorze możliwość przełączenia urządzenia na alternatywny punkt dostępu |
| W-I15 | MUSI | **D** | Dostarczyć **deklarację zgodności**, wykaz zastosowanych norm zharmonizowanych oraz sprawozdania z badań kompatybilności elektromagnetycznej, badań radiowych i badań bezpieczeństwa |
| W-I11 | MUSI | **P** | Producent elektronicznej syreny udostępnia udokumentowany interfejs sterowania wraz z funkcjami, formatem komend, zasobami lokalnymi, statusami i parametrami. Dla syreny silnikowej dokumentuje się jej tor sterowania i wymagania napędu. |
| W-I12 | MUSI | **P** | **Producent syreny** — zrealizować ten interfejs na standardowej warstwie fizycznej: szeregowej, sieciowej, uniwersalnej albo na wejściach i wyjściach ogólnego przeznaczenia; złącza i protokoły autorskie bez opublikowanej specyfikacji nie spełniają wymagania |
| W-I13 | MUSI | **P** | **Producent syreny** — określić warunki licencyjne dopuszczające integrację przez podmiot trzeci, bez opłat za samo podłączenie i bez utraty gwarancji |
| W-I14 | MUSI | **P** | Producent nowej syreny elektronicznej zapewnia udokumentowane wejście audio i osobne PTT lub przyjęty równoważny profil integracji. Wymagania odtwarzania plików nie stosuje się do napędu syreny silnikowej. |

## J. Współistnienie i arbitraż

Zachowuje się wymagane dotychczasowe funkcje lokalne i radiowe. Wszystkie kanały mają wspólny arbitraż. „Odrzucono”, „odroczono”, „wykonano” i „wynik niepewny” nie są synonimami.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-J01 | MUSI | **I** | Nie wyłączać ani nie ograniczać dotychczasowych sposobów uruchomienia syreny — istniejącego systemu dyspozytorskiego, pulpitu lokalnego, przycisku ręcznego ani kanału radiowego |
| W-J02 | MUSI | **I** | Zachować możliwość **uruchomienia lokalnego**, działającego przy całkowitym braku łączności z SOiA |
| W-J03 | MUSI | **I** | Zapewniać współpracę z instalacją istniejącą bez utraty jej wymaganych funkcji i uprawnień gwarancyjnych. Niezbędne nastawy integracyjne dokumentować i uzgadniać; nie utożsamiać ich z wyłączeniem dotychczasowego systemu. |
| W-J04 | MUSI | **I** | Przy zbiegu poleceń stosować jedną wersjonowaną tabelę arbitrażu dla wszystkich torów. Rozróżniać końcowe odrzucenie, kontrolowane odroczenie i duplikat; bez automatycznej kolejnej emisji oraz bez niejawnego przerwania bieżącej. |
| W-J05 | MUSI | **I** | Zachować pierwszeństwo lokalnego odcięcia i trybu serwisowego **niezależnie od toru**, z którego przyszło polecenie |
| W-J06 | MUSI | **I** | Po dołączeniu kanału SOiA potwierdzić w odbiorze, że **dotychczasowy sposób uruchomienia nadal działa** |
| W-J07 | POWINIEN | **I** | Odnotowywać w rejestrze zdarzeń tor, z którego przyszło polecenie |
| W-J08 | MUSI | **I** | Po zakończeniu bieżącej funkcji ponownie kwalifikować wyłącznie operację świadomie odroczoną przez przyjęty profil: sprawdzić ważność, historię, adresata i stan toru. Odrzuconej końcowo albo wykonanej operacji nie ponawiać. |

## K. Zestaw i instalacja

Zakres D oznacza dostawę określoną kartą: może korzystać z istniejącej syreny, bramki i zasilania. Wykaz elementów rozdziela rzeczy dostarczane, powierzone i zapewniane przez instalatora. Nie przepisuje się konkretnego zestawu KPO do każdego małego urządzenia.

| ID | Moc | Klasa lub zakres | Wymaganie |
| --- | --- | --- | --- |
| W-K01 | MUSI | **D** | Dostarczać kompletny zestaw zgodny z kartą zakresu: sterownik, wymagane moduły, zasilanie, anteny i akcesoria. Osobna bramka oraz podział na część wewnętrzną i zewnętrzną wynikają z projektu, nie z samego oznaczenia 1.5. |
| W-K02 | MUSI | **D** | Zawierać **listę zawartości zestawu** umożliwiającą kontrolę kompletności dostawy przed montażem, z rozróżnieniem pozycji pakunkowych i elementów fabrycznie zabudowanych oraz z **procedurą postępowania przy stwierdzeniu niezgodności** |
| W-K03 | MUSI | **D** | Wskazywać w dokumentacji **elementy zapewniane przez instalatora** — okablowanie, puszki, dławnice, kotwy, konstrukcje wsporcze — żeby ich brak nie był mylony z niekompletnością dostawy |
| W-K04 | MUSI | **D** | Zapewnić częściom pracującym na zewnątrz ochronę środowiskową i temperatury odpowiednie do lokalizacji, określone przed zakupem. Parametry dla elementów wewnętrznych i zewnętrznych oceniać oddzielnie. |
| W-K05 | MUSI | **D** | Udokumentować połączenia i zasilanie części zestawu, w tym rzeczywistą drogę do bramki, jeżeli występuje. Nie wymagać osobnej bramki przy każdej syrenie bez uzasadnienia projektu sieci. |
| W-K20 | MUSI | **D** | Zawierać w zestawie **ochronniki przepięciowe** torów sygnałowego i zasilającego prowadzonych między częścią zewnętrzną a wewnętrzną |
| W-K21 | MUSI | **D** | Traktować część zewnętrzną jako element istotny dla bezpieczeństwa: podać sposób jej utwardzenia, ścieżkę aktualizacji jej oprogramowania, sposób uwierzytelnienia sterownika do jej interfejsów oraz sposób nadzoru jej zasilania |
| W-K22 | MUSI | **D** | Podać dopuszczalny **budżet napięciowy zasilania części zewnętrznej pod obciążeniem** oraz maksymalną długość trasy; wartość mierzy się przy odbiorze |
| W-K23 | MUSI | **D** | Zawierać w zestawie **fizyczny element uruchomienia lokalnego** wraz ze wskazaniem miejsca jego montażu |
| W-K24 | MUSI | **D** | Podać dla magazynu energii **datę produkcji i datę ostatniego ładowania odświeżającego**; napięcie mierzy się przed pierwszym uruchomieniem |
| W-K25 | MUSI | **D** | Zapewnić, że pierwsze załączenie **nie wyzwala zabezpieczenia obwodu obiektowego**, albo podać wymaganą charakterystykę tego zabezpieczenia |
| W-K26 | MUSI | **D** | Wskazać wymagane umiejscowienie anten części wewnętrznej i przewidzieć **zapis zmierzonej jakości toru radiowego** w dokumentacji odbiorowej |
| W-K06 | MUSI | **D** | Udostępniać **oznaczoną, ponumerowaną listwę przyłączeniową** dla wszystkich sygnałów obiektowych: zasilania, wejść dwustanowych, wyjść, torów stykowych i toru audio |
| W-K07 | MUSI | **D** | Dołączać do dokumentacji **mapę listwy** wiążącą numer zacisku z sygnałem i z oznaczeniem barwnym złączki, wraz z wymogiem oznaczenia obu końców przewodu obiektowego przez instalatora |
| W-K08 | MUSI | **D** | Umożliwiać podłączenie bez lutowania i bez narzędzi specjalistycznych producenta |
| W-K09 | MUSI | **D** | Zapewnić dostęp do gniazda karty abonenckiej i do magazynu energii **bez demontażu urządzenia z uchwytu** |
| W-K10 | POWINIEN | **D** | Umożliwiać otwarcie obudowy bez kolizji z instalacją obiektową |
| W-K11 | MUSI | **D** | Dla zestawu z obwodami sieciowymi zapewnić właściwą klasę ochronności i połączenia ochronne zgodnie z projektem oraz dokumentacją. Obowiązkowego PE nie przerywać; sam moduł zasilany bezpiecznym napięciem nie jest automatycznie urządzeniem I klasy ochronności. |
| W-K12 | MUSI | **D** | Zapewnić zabezpieczenia zasilania dobrane do prądu udarowego, obciążenia i warunków zwarciowych obiektu, z udokumentowanym miejscem montażu i dostępem serwisowym. |
| W-K13 | MUSI | **D** | Zapewnić **fizyczną przegrodę albo osłonę** oddzielającą obwody sieciowe od obwodów niskiego napięcia na listwie przyłączeniowej, chroniącą przed dotykiem podczas prac serwisowych |
| W-K14 | MUSI | **D** | Wymagać indywidualnego zaizolowania żył niewykorzystanych w przewodach wielożyłowych |
| W-K15 | MUSI | **D** | Zawierać w dokumentacji **listę kontrolną przed pierwszym załączeniem**, obejmującą kontrolę mechaniczną i elektryczną |
| W-K16 | MUSI | **D** | Dołączać **instrukcję instalacji** obejmującą kolejność prac, dobór mocowania do rodzaju podłoża, montaż magazynu energii, montaż anten i uruchomienie |
| W-K17 | MUSI | **D** | Wskazywać wymagane **kwalifikacje personelu** — osobno dla prac przy napięciu sieciowym, dla kotwienia obudowy o znacznej masie i dla prac na wysokości — wraz z wykazem środków ochrony indywidualnej i warunkami przerwania pracy |
| W-K18 | MUSI | **D** | Przewidywać przy pierwszym załączeniu **sprawdzenie bezprzerwowego przejścia na zasilanie rezerwowe** i powrotu do zasilania sieciowego |
| W-K19 | POWINIEN | **D** | Zawierać wzór protokołu przekazania instalacji |

## Stosowanie i odbiór

Wartości połączeń elektrycznych, konfiguracja sieci, role i sekrety nie są publikowane w wytycznych. Trafiają do karty modelu i egzemplarza. Wymagania dotyczące wskazanego profilu ocenia się z odpowiednimi scenariuszami [Z10](Z10-TESTY-I-ODBIOR.md). Dobór opisuje [profil 1.5](../PROFIL_1_5.md), a zakres zamówienia [Z11](Z11-ZAPISY-DO-OPZ.md).

Brak funkcji w bieżącym kontrakcie centrali oznacza zależność do zamknięcia przed odbiorem tej funkcji, a nie podstawę do mapowania innej komendy. Samo wpisanie numeru 1.5 lub 0.5 nie aktualizuje oprogramowania urządzeń.

## Zestawienie liczbowe

| Część | Wymagań | MUSI |
| --- | --- | --- |
| A — Weryfikacja polecenia | 17 | 15 |
| B — Obszar działania | 8 | 7 |
| C — Sygnały i komunikaty | 17 | 13 |
| D — Kanały i łączność | 26 | 23 |
| E — Wysterowanie syreny | 14 | 12 |
| F — Platforma i cykl życia | 19 | 19 |
| G — Tryby pracy i dowody | 13 | 11 |
| H — Zasilanie i warunki pracy | 9 | 7 |
| I — Interoperacyjność i prawa | 15 | 14 |
| J — Współistnienie i arbitraż | 8 | 7 |
| K — Zestaw i instalacja | 26 | 24 |
| **Razem** | **172** | **152** |

Identyfikatory 166 wymagań wydania 0.4 zachowano. Dodano W-D26 i W-F15–W-F19; zmiany zakresu są jawne i dotyczą nowego wydania dokumentacji, bez zmiany wcześniejszych umów lub protokołów odbioru.
