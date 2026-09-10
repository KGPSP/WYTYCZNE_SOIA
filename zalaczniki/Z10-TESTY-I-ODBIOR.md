---
tytuł: "Załącznik nr 10 — Scenariusze sprawdzeń i protokół odbioru"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 10 — Scenariusze sprawdzeń i protokół odbioru

## Zakres i metodyka

Próby dotyczą wskazanego modelu, rewizji, obrazu, aplikacji i profilu. Oddzielnie odbiera się platformę, egzemplarz, kanały oraz tor obiektu. Wszystkie właściwe wymagania MUSI mają wynik i dowód; „nie wykonano” nie oznacza zgodności.

Klasa I jest wspólna; próby **1.5 / II** obejmują lokalne audio obu profili; III dotyczy zamówionego TTS. D i P oznaczają właściwy zakres dostawy. Funkcji audio nie bada się na silniku, ale bada się właściwy program silnikowy. Zakresy warunkowe muszą być rozstrzygnięte przed próbą.

Przypadek negatywny różni się od poprawnego wyłącznie badanym warunkiem. Obcy TERC z jednocześnie błędnym podpisem nie testuje reguły terytorialnej. Przy każdej próbie zapisuje się konfigurację, dane kontrolne, czas, wynik oraz poziom dowodu: odbiór, stan wyjścia, odtwarzanie albo pomiar zewnętrzny.

Próby prowadzi się w uzgodnionym środowisku i zgodnie z właściwą procedurą. Nie należy wystawiać produkcyjnych poleceń tylko po to, aby sprawdzić parser. Dla funkcji jeszcze niewdrożonej w centrali wynik pozostaje niewykonany w tym kanale; test lokalny nie poświadcza pełnej integracji z centralą.

## Scenariusze istniejące z zachowaniem identyfikatorów

### 1.1. Weryfikacja treści

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-01 | **I** | Poprawny wykaz, polecenie dla własnej gminy | emisja |
| S-02 | **I** | Podpis niepoprawny | odrzucenie **całego** wykazu, brak emisji |
| S-03 | **I** | Treść zmodyfikowana po podpisaniu | odrzucenie całości |
| S-04 | **I** | Nieznany identyfikator klucza | odrzucenie, brak emisji |
| S-05 | **I** | Klucz z okna wymiany — poprzedni, wciąż ważny | poprawna weryfikacja, emisja |
| S-06 | **I** | Niezgodna wersja profilu albo środowiska | odrzucenie |
| S-07 | **I** | Wektory wzorcowe podpisu | zgodność co do bajtu |
| S-08 | **I** | Feed lub polecenie przekracza limit przyjętego kontraktu | Odrzucenie jako błąd; urządzenie pozostaje sprawne; brak deklaracji limitu API, którego API nie publikuje. |

### 1.2. Reguła obszaru

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-09 | **I** | Polecenie dla własnej gminy | emisja |
| S-10 | **I** | Polecenie dla powiatu obejmującego tę gminę | emisja |
| S-11 | **I** | Polecenie dla województwa obejmującego tę gminę | emisja |
| S-12 | **I** | Polecenie wielowojewódzkie obejmujące TERC badanego toru | Wykonanie właściwego toru; przy braku dopasowania brak wykonania. |
| S-13 | **I** | Polecenie dla obcej gminy | **brak emisji** |
| S-14 | **I** | Gmina miejsko-wiejska: polecenie dla całej gminy, urządzenie w mieście | emisja |
| S-15 | **I** | Gmina miejsko-wiejska: polecenie dla obszaru wiejskiego, urządzenie w mieście | **brak emisji** |
| S-16 | **I** | Kod sześciocyfrowy, bez cyfry rodzaju | odrzucenie kodu, brak emisji |
| S-17 | **I** | Kod miejscowości albo ulicy | pominięcie, brak emisji |
| S-18 | **I** | Konfiguracja toru kodem powiatu lub województwa | Odrzucenie lub błąd blokujący dopuszczenie toru; ostrzeżenie nie może pozwalać na wykonanie z błędnym TERC. |

### 1.3. Czas, źródła czasu i powtórzenia

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-19 | **I** | Wykaz po terminie ważności | brak emisji |
| S-20 | **I** | Okno rozpoczęcia już zamknięte | brak emisji |
| S-21 | **I** | Ten sam identyfikator polecenia po restarcie urządzenia | **brak drugiej emisji** |
| S-22 | **I** | Ten sam identyfikator po zaniku i powrocie zasilania | brak drugiej emisji |
| S-23 | **I** | To samo polecenie dwoma różnymi kanałami | dokładnie jedna emisja |
| S-24 | **I** | CANCEL_PENDING dla wskazanej znanej akcji oczekującej | Anulowanie tylko tej akcji, brak dźwięku odwołania. |
| S-25 | **I** | CANCEL_PENDING dla akcji rozpoczętej lub zakończonej | Zapis/no-op zgodnie z kontraktem; brak przerwania emisji i brak odwołania dźwiękowego. |
| S-26 | **I** | CANCEL_PENDING dla nieznanego lokalnie ID w profilu 0.1 | Brak działania; nie tworzy START ani nowej akcji z powiązań. |
| S-27 | **I** | Dryf zegara przekraczający 30 s | brak emisji, zapis przyczyny |
| S-28 | **I** | Utrata źródła podstawowego czasu | Użycie źródła kolejnego; wykonanie tylko przy zachowanej wiarygodności czasu. |
| S-29 | **I** | Brak synchronizacji dłuższy niż doba | Sygnalizacja wieku i ocena zegara; brak nowego wykonania po utracie wiarygodności. |

### 1.4. Katalog sygnałów

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-30 | **I** | Każdy sygnał wymagany przez profil — pomiar czasu | Nominalny przebieg Z4 oraz metoda, tolerancja i niepewność z zatwierdzonego pakietu odbiorowego. |
| S-31 | **I** | Każdy sygnał z katalogu — struktura | modulacja oraz liczba i długość przerw zgodne z wzorcem |
| S-32 | **1.5 / II** | Poziom w zadeklarowanym punkcie pomiarowym | w granicach ±3 dB względem wzorca, bez przesterowania |
| S-33 | **1.5 / II** | Regulacja poziomu | zmiana skuteczna, realizowana programowo |
| S-34 | **I** | Nieznany kod sygnału w wykazie | odrzucenie **tego** polecenia, obsługa pozostałych bez zakłóceń |
| S-35 | **1.5 / II** | Plik o skrócie niezgodnym z zatwierdzonym manifestem | Odmowa instalacji/użycia; brak zastąpienia zasobu innym plikiem o podobnej nazwie. |
| S-36 | **1.5 / II** | Pamięć i trwałość lokalnego pakietu audio | Minimum 32 MB oraz miejsce na dwie wersje rzeczywistego pakietu; zasoby dostępne po restarcie. |

### 1.5. Komunikat głosowy

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-37 | **III** | Synteza przy całkowitym braku łączności | komunikat wypowiedziany, zrozumiały |
| S-38 | **III** | Komunikat głosowy zbiegający się z sygnałem akustycznym | sygnał akustyczny **nieopóźniony i niezastąpiony** |
| S-39 | **III** | Ten sam tekst przy tej samej wersji modelu | ten sam dźwięk |

### 1.6. Kanały i odporność

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-40 | **I** | Kanał niezwłocznego powiadomienia wyłączony | wykrycie zmiany samym odpytywaniem |
| S-41 | **I** | Odpowiedź z pamięci pośredniej starsza niż oczekiwana | ponowienie żądania |
| S-42 | **I** | Przekroczenie limitu zapytań | wstrzymanie na wskazany czas |
| S-43 | **I** | Niedostępność publicznej usługi | Kontrolowane wycofanie; brak wykonania na przeterminowanych danych. Inne odebrane poprawne kanały ocenia się według ich profilu. |
| S-44 | **I** | Utrata kanału podstawowego | praca kanałem zapasowym, **pełny zakres weryfikacji** |
| S-45 | **I** | Polecenie tekstowe z nieuprawnionego numeru | odrzucenie i zapis zdarzenia |
| S-46 | **I** | SMS z błędnym uwierzytelnieniem właściwego profilu | Odrzucenie i zapis bez ujawniania sekretu. |
| S-47 | **I** | Powtórzone polecenie tekstowe w oknie blokady | odrzucenie i zapis |
| S-48 | **I** | Multipart wobec profilu dopuszczającego jedną wiadomość oraz wobec profilu dopuszczającego kompletowanie | W pierwszym odrzucenie; w drugim wykonanie wyłącznie kompletnej uwierzytelnionej wiadomości w limitach. Brak wykonania fragmentu. |
| S-102 | **I** | Powtórzenie uwierzytelnionego SMS oraz zmiana jego czasu/licznika bez ponownego uwierzytelnienia | Duplikat lub naruszenie integralności odrzucone; historia trwała, brak nowej emisji. |
| S-49 | **I** | Polecenie i test bez emisji na kanale ze zwrotkami | Oddzielne ID oraz statusy przyjęcia/startu/końca/błędu według kontraktu. Test bez emisji nie raportuje dźwięku. |

### 1.7. Współistnienie z systemem istniejącym

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-50 | **I** | Uruchomienie dotychczasowym sposobem po dołączeniu kanału SOiA | **działa bez zmian** |
| S-51 | **I** | Uruchomienie lokalne przy całkowitym braku łączności z SOiA | działa |
| S-52 | **I** | Drugie polecenie podczas zajęcia toru | Brak równoległego przejęcia. Wynik: odrzucenie albo jawne odroczenie według przyjętej przed próbą tabeli Z5. |
| S-53 | **I** | Jawnie odroczona operacja po zwolnieniu toru | Pełna ponowna kwalifikacja. Wykonanie tylko przy ważności i braku wcześniejszej realizacji; końcowo odrzucona operacja nie wraca. |
| S-54 | **I** | Odcięcie lokalne przy emisji uruchomionej z toru SOiA | odcięcie skuteczne |
| S-55 | **I** | Tryb serwisowy wobec polecenia z każdego toru | blokada zdalnego uruchomienia |
| S-56 | **I** | Nieuprawniona albo nieprzewidziana przez profil próba zdalnego STOP | Odrzucenie; nie mapuje się CANCEL_PENDING lub odwołania alarmu na STOP. |

### 1.8. Platforma, zasilanie i diagnostyka

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-57 | **I** | Zawieszenie oprogramowania podczas pracy toru | Niezależny nadzór ogranicza tor i restartuje aplikację/platformę; brak samoczynnego wznowienia emisji. |
| S-58 | **I** | Restart urządzenia z niewysłanymi zapisami rejestru | zapisy **zachowane**, nic nie ginie |
| S-59 | **I** | Odczyt rejestru bez oprogramowania producenta | format otwarty, czytelny |
| S-60 | **I** | Rozruch na docelowym obrazie i uzyskanie gotowości aplikacji | Osobne czasy i warunki, porównane z limitem karty przyjętym przed próbą. Online w Managerze nie zastępuje wyniku. |
| S-61 | **I** | Zwarcie lub przeciążenie jednego wyjścia obiektowego | Uszkodzony tor izolowany i zgłoszony; sterownik i pozostałe sprawne tory zachowują pracę. Brak fikcyjnego sukcesu uszkodzonego toru. |
| S-62 | **I** | Impuls 200 ms na wejściu uruchomienia lokalnego | wykryty |
| S-63 | **I** | Odczyt stanu przy zamkniętej obudowie | praca z rezerwy, niski stan energii, gotowość i brak łączności **rozróżnialne z zewnątrz** |
| S-64 | **I** | Nieudana aktualizacja, utrata zasilania przy zapisie i nieudany rozruch nowego obrazu | Kontrolowany rollback; tożsamość, dane aplikacji i historia zachowane; brak ponownej emisji. |
| S-65 | **I** | Przełączenie na alternatywny punkt dostępu i punkt zaufania | skuteczne, bez udziału producenta |

### 1.9. Sprawdzenia dokumentowe

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-66 | **D** | Deklaracja zgodności, wykaz norm zharmonizowanych, sprawozdania z badań | przedłożone i kompletne |
| S-103 | **I** | Dokumentacja interfejsów elektrycznych, audio i integracyjnych **wraz ze schematem elektrycznym** | przedłożona, w zakresie umożliwiającym samodzielny serwis |
| S-67 | **D** | Model degradacji magazynu energii i świadectwo dla profilu obciążenia obejmującego emisję | przedłożone |
| S-68 | **P** | Dokumentacja interfejsu właściwego rodzaju syreny | Zakres pozwala wykonać niezależną integrację API, audio albo toru silnikowego zgodnie z zamówieniem. |
| S-69 | **P** | Tor AUDIO/PTT zamawianej syreny elektronicznej | Interfejs i parametry udokumentowane albo przyjęty jawny wariant równoważny; nie dotyczy napędu silnikowego. |
| S-70 | **P** | Integracja przez niezależnego wykonawcę | Wykazana na dokumentacji i prawach objętych dostawą, dla właściwego toru. |

### 2.1. Dostawa i montaż

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-71 | **D** | Kompletność dostawy wobec listy zawartości zestawu | wszystkie pozycje obecne, brak uszkodzeń transportowych |
| S-72 | **D** | Data produkcji i ostatniego ładowania magazynu energii, pomiar napięcia przed uruchomieniem | odnotowane, napięcie w zakresie |
| S-73 | **D** | Kontrola mechaniczna: zamocowanie, otwarcie obudowy, stabilność magazynu energii i anten | zgodne z listą kontrolną producenta |
| S-74 | **D** | Kontrola elektryczna przed załączeniem, zasilanie wyłączone | Polaryzacja, izolacja i wymagane połączenia ochronne zgodne z klasą ochronności oraz projektem. |
| S-75 | **D** | Pierwsze załączenie | bez wyzwolenia zabezpieczenia obwodu obiektowego |
| S-76 | **D** | **Bezprzerwowe przejście na zasilanie rezerwowe** przy odłączeniu zasilania sieciowego | brak przerwy w pracy, sygnalizacja zmienia stan |
| S-77 | **D** | Powrót do zasilania sieciowego | praca sieciowa przywrócona, sygnalizacja zgodna |
| S-78 | **D** | Łącze między częścią wewnętrzną a zewnętrzną | aktywne, potwierdzone po obu stronach |
| S-79 | **D** | Napięcie zasilania części zewnętrznej **pod obciążeniem** | w zadeklarowanym budżecie |
| S-80 | **D** | Ochronniki przepięciowe torów między częścią zewnętrzną a wewnętrzną | zamontowane i podłączone |
| S-81 | **D** | Zgodność okablowania z mapą listwy przyłączeniowej | zgodne co do numeru zacisku, oba końce przewodu oznaczone |
| S-82 | **D** | Umiejscowienie anten części wewnętrznej i jakość toru radiowego | zgodne z dokumentacją, wartość zmierzona odnotowana |
| S-83 | **D** | Element uruchomienia lokalnego | zamontowany w miejscu wskazanym w dokumentacji, sprawny |

### 2.2. Konfiguracja

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-84 | **I** | Mapa TERC niezależnych torów | Jeden prawidłowy TERC na tor; dopasowanie jednego nie uruchamia wszystkich wyjść. |
| S-85 | **I** | Indywidualne uwierzytelnienie urządzenia i SMS | Sekrety właściwego profilu unikalne; brak kont i haseł domyślnych. |
| S-86 | **I** | Numery uprawnione | wprowadzone, zgodne z kartą konfiguracji |
| S-87 | **I** | Endpoint i zaufane klucze konfiguracji | Zgodne z zatwierdzonym profilem; nieznany klucz z samej odebranej treści nie zostaje automatycznie zaakceptowany. |
| S-88 | **1.5 / II** | Lokalne pliki i manifest pakietu | Zasoby wgrane, integralność i akceptacja potwierdzone, wersja zapisana. |

### 2.3. Uruchomienie

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-89 | **I** | Łączność | zasięg albo połączenie przewodowe potwierdzone |
| S-90 | **I** | Test łączności | przyjęcie potwierdzone, **bez emisji zewnętrznej** |
| S-91 | **I** | Ogłoszenie alarmu | przyjęcie i wykonanie potwierdzone |
| S-92 | **I** | Odwołanie alarmu | **emisja sygnału ciągłego, a nie cisza** |
| S-93 | **I** | Polecenie dla obcej gminy, poprawne pod każdym innym względem | brak reakcji |
| S-94 | **I** | Powtórzenie tego samego polecenia | brak drugiej emisji |
| S-95 | **I** | Odcięcie lokalne | skuteczne |
| S-96 | **I** | Zachowanie po restarcie | brak samoczynnego uruchomienia |
| S-97 | **D** | Podtrzymanie rzeczywistej kompletacji | Czasy W-H01 wykazane dla podanego obciążenia; osobna zdolność zasilania wzmacniacza lub silnika, jeśli wymagana. |
| S-98 | **I** | Zmierzony **czas od wydania polecenia do rozpoczęcia emisji** | odnotowany; **bez progu zaliczenia** |
| S-99 | **D** | Warunki obiektu wobec deklarowanych warunków pracy | Pomiar i ocena zakresu. Warunki poza deklaracją nie potwierdzają zgodności; pojedynczy pomiar nie dowodzi warunków całorocznych. |
| S-100 | **I** | Dotychczasowy sposób uruchomienia **po** dołączeniu kanału SOiA | działa bez zmian |
| S-101 | **I** | Uruchomienie lokalne przy odłączonej łączności | działa |

## Próby platformy i profilu kompaktowego

| Nr | Klasa lub zakres | Scenariusz | Oczekiwany wynik |
| --- | --- | --- | --- |
| S-104 | **I** | Odtworzenie budowy Yocto/OrchestraOS dla płyty z przekazanego manifestu | Wynik uruchamia się na wskazanym modelu; źródła, BSP i zależności są identyfikowalne. |
| S-105 | **I** | Provisioning i pierwsza rejestracja egzemplarza | Właściwa instancja Orchestra i indywidualna tożsamość; brak samoczynnej emisji. |
| S-106 | **I** | Uprawniony dostęp, próba obcego dostępu i cofnięcie uprawnień | Uprawniona operacja działa, pozostałe odrzucone i odnotowane; zarządzanie przed instalacją aplikacji. |
| S-107 | **I** | Zły podpis RAUC i nieautoryzowany obraz/nośnik rozruchowy | Odmowa aktualizacji lub rozruchu; osobno wykazana ochrona obu mechanizmów. |
| S-108 | **1.5** | Rzeczywiste porty, opcje i bilans profilu kompaktowego | Macierz Z3 i W-F19 spełnione; PTT policzone jako funkcja istniejącego styku, bez podwójnego liczenia. |
| S-109 | **I** | Aplikacja KG PSP na dostarczonej platformie i interfejsach | Pakiet działa bez zmiany logiki i obejścia zabezpieczeń; autostart, trwały zapis i lokalny kontrakt działają. |
| S-110 | **I** | Awaria po trwałym zapisie zamiaru lub podczas aktywacji wyjścia | Wynik przerwany lub niepewny zostaje zachowany; brak automatycznego ponowienia po restarcie. |
| S-111 | **1.5 / II** | ALARM i ODWOLANIE bez internetu oraz awaria odtwarzacza | Właściwe lokalne pliki, pełny nominalny przebieg i osobny nadzór PTT; brak zależności od pobrania audio. |
| S-112 | **I** | Syrena silnikowa, program, odcięcie i wybieg — gdy zastosowano | Właściwe sterowanie izolowaną aparaturą i niezależny limit; odcięcie napędu nie jest deklarowane jako natychmiastowe zatrzymanie wirnika. |
| S-113 | **I** | HTTP 304 przy wygasłej kopii oraz przyszłe polecenie | 304 nie odnawia ważności; przyszła akcja wymaga ponownej kwalifikacji na ważnej treści. |
| S-114 | **I** | Zmiana floty aktualizacyjnej i wymiana SIM | Tożsamość egzemplarza i TERC nie zmieniają się samoczynnie; właściwe atrybuty ewidencji zaktualizowane. |
| S-115 | **I** | Rezerwa TETRA, a w etapie migracji terminal i integracja | Teraz: port/moc/miejsce/obsługa. Docelowo: polecenie działa bez GSM i internetu obiektu, a zapas GSM zachowuje właściwe reguły. |
| S-116 | **I** | Techniczne STOP objęte przyjętym profilem | Wyłącznie uprawniona funkcja i właściwy zakres; wynik przerwania zapisany, bez mylenia z odwołaniem dźwiękowym. |
| S-117 | **I** | Ochrona sekretów, toru procesor–radio i dostępu serwisowego według modelu zagrożeń | Próby odczytu klucza, zapisu/wstrzyknięcia/powtórzenia na szynie i nieuprawnionego debugowania nie omijają ochrony. Brak sekretów w logach; domeny zaufania rozdzielone. |
| S-118 | **I** | SBOM, wsparcie, prawa, komponenty i procedura odtworzenia | Komplet dla wydania; możliwość utrzymania i przejęcia serwisu; zależności i warunki podpisywania jawne. |
| S-119 | **III** | TTS na konfiguracji kompaktowej lub rozszerzonej | Zasoby III i pełny lokalny polski TTS z prawami użycia; liczba I/O odpowiada zamówionemu profilowi, nie samej nazwie III. |
| S-120 | **I** | Przyłączenie LoRaWAN i ewentualnej bramki w zakresie zamówienia | Node działa z właściwym LNS; onboarding/CUPS bramki potwierdzone, jeśli bramka jest objęta dostawą. |

## Powiązanie z wymaganiami

| Obszar Z3 | Główne scenariusze |
| --- | --- |
| A — podpis, ważność i historia | S-01–S-08, S-19–S-29, S-110, S-113, S-117 |
| B — obszar | S-09–S-18, S-84, S-93, S-114 |
| C — sygnały i mowa | S-30–S-39, S-88, S-91–S-92, S-111, S-119 |
| D — kanały | S-40–S-49, S-85–S-87, S-89–S-90, S-102, S-113–S-115, S-120 |
| E — tor wykonawczy | S-32–S-33, S-54–S-57, S-61–S-62, S-68–S-70, S-95, S-108, S-110–S-112, S-116 |
| F — platforma | S-57–S-65, S-103–S-110, S-114, S-117–S-119 |
| G — stan i dziennik | S-49, S-55, S-58–S-59, S-63, S-96, S-106, S-110, S-117 |
| H — zasilanie i środowisko | S-60, S-67, S-72, S-76–S-77, S-96–S-99 |
| I — interoperacyjność i prawa | S-65–S-70, S-103–S-109, S-117–S-118 |
| J — współistnienie | S-50–S-56, S-100–S-101, S-110, S-116 |
| K — dostawa i instalacja | S-66–S-67, S-71–S-83, S-97, S-99, S-108, S-115 |

Macierz porządkuje grupy. W karcie odbioru każde właściwe wymaganie musi zostać powiązane z konkretnym dowodem; samo zaliczenie jednej próby w grupie nie poświadcza wszystkich wymagań tej grupy.

## Protokół i wynik

**Obiekt / ID sterownika / ID syreny / rewizja karty:** …

**Model / OS/BSP / aplikacja / profil zdolności i wykonania:** …

**Wykonawca / przedstawiciel właściciela / data:** …

| Grupa odbioru | Scenariusze właściwe | Dowód | Wynik |
| --- | --- | --- | --- |
| Konfiguracja modelu i platforma | | | |
| Wyposażenie 1.5 lub rozszerzone | | | |
| Provisioning i Orchestra | | | |
| Aplikacja i kanały | | | |
| Syrena i fizyczny efekt | | | |
| Odmowy, arbitraż i restart | | | |
| Zasilanie i warunki obiektu | | | |
| Dokumentacja i utrzymanie | | | |

Wynik: pozytywny, negatywny, nie wykonano albo nie dotyczy z uzasadnieniem. Protokół podaje niezgodności, zakres gotowości, działania i rozstrzygnięcie. Niezgodności wykluczającej wymaganą bezpieczną funkcję nie usuwa zapis „z uwagami”.

Czas od publikacji do emisji mierzy się osobno od czasu rozruchu i od czasu dźwięku. Ocenia się go według przyjętych warunków i wymogu niezwłoczności; 30 s pollingu nie jest gwarancją końcowej latencji. Warunki środowiskowe porównuje się z deklaracją, bez uznawania jednego pomiaru za dowód warunków całorocznych.

## Sprawdzenia okresowe i po zmianie

Plan utrzymania określa częstotliwość, zakres, metodę i uprawnienia, uwzględniając DTR, właściwe wytyczne i stan obiektu. Zmiana SIM, firmware, pakietu, interfejsu lub profilu wymaga ponowienia odpowiednich prób. Próby zewnętrznej emisji organizuje się zgodnie z właściwą procedurą; ta publikacja nie zleca ich uruchomienia.

Dokument opisuje 120 scenariuszy: zachowane S-01–S-103 oraz nowe S-104–S-120. Nie jest raportem ich wykonania na urządzeniach.
