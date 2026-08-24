---
tytuł: "Załącznik nr 3 — Wymagania minimalne dla urządzenia"
dokument: "Podręcznik podłączania syren alarmowych i innych urządzeń do SOiA"
wersja: 0.4
data: 2026-08-23
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
źródło: "Wydzielono z PODRECZNIK_v2.md"
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 3 — Wymagania minimalne dla urządzenia


## Zakres i sposób stosowania załącznika

Załącznik określa zdolności wymagane do podłączenia urządzenia do SOiA i zapewnienia jego
przewidywalnego działania. Nie określa mocy akustycznej, zasięgu ani zasad doboru głośników;
zagadnienia te należą do projektu instalacji i pozostają w zakresie odpowiedzialności zamawiającego.

Każde wymaganie ma identyfikator, pod którym można je przywołać w opisie przedmiotu zamówienia
i w protokole odbioru.

**Moc wymagania.** **MUSI** oznacza warunek konieczny — urządzenie niespełniające go nie jest
urządzeniem zgodnym z SOiA. **POWINIEN** oznacza wymaganie zalecane, którego pominięcie wymaga
świadomej decyzji zamawiającego i którego nie należy pomijać milcząco.

**Klasa zdolności** określa funkcjonalny zakres stosowania wymagania:

| Klasa | Zakres | Warunek stosowania |
|---|---|---|
| **I** | rdzeń | zawsze, dla każdego urządzenia przyłączanego do SOiA |
| **II** | tor audio | gdy sterownik **sam odtwarza dźwięk**; nie dotyczy sterowania syreną cyfrową przez jej własny interfejs |
| **III** | profil głosowy | opcjonalnie, gdy urządzenie ma wypowiadać treść słowną |

Symbole **D** i **P** nie są klasami zdolności. Oznaczają zakres przedmiotu zamówienia lub adresata
wymagania:

| Symbol | Zakres | Warunek stosowania |
|---|---|---|
| **D** | dostawa i montaż | gdy przedmiotem zamówienia jest **kompletny zestaw**; nie stosuje się do dostawy samego sterownika |
| **P** | wobec producenta syreny | nie jest wymaganiem wobec sterownika — trafia do zamówienia na syrenę |

Zamawiający wskazuje w zamówieniu wymagane klasy zdolności oraz właściwe symbole zakresu. Klasa I
stanowi podstawowy i obowiązkowy zakres zgodności z SOiA. Sterowanie syreną cyfrową przez jej
udokumentowany interfejs wymaga klasy I; modernizacja, w której sterownik odtwarza dźwięk, wymaga
klas I i II; klasę III stosuje się wyłącznie po objęciu zamówieniem funkcji głosowych.

Podział na klasy zachowuje neutralność technologiczną. Weryfikacja podpisu i porównanie kodów gmin
mogą być realizowane na mikrokontrolerze; klasa I nie wymaga zastosowania komputera klasy
aplikacyjnej.

> [!note] Jak czytać tabelę wymagań
> Najpierw ustala się przedmiot dostawy, następnie wybiera klasy zdolności i symbole zakresu. `MUSI` oznacza warunek konieczny, a `POWINIEN` wymaga świadomej decyzji zamawiającego przy pominięciu. Klasy I–III opisują zdolności urządzenia, natomiast D i P wskazują zakres dostawy albo adresata. Na końcu wymaganie łączy się z właściwym scenariuszem odbiorowym; objaśnienie nie zastępuje tekstu wiersza W-*.

## Wyłączenia z zakresu załącznika

**Nazwy własne.** Załącznik nie wskazuje firm, marek, modeli ani oprogramowania, również przy opisie
stanu faktycznie osiągniętego. Elementy rozwiązania określa się przez funkcje i właściwości, aby
zachować neutralność technologiczną oraz zasadę interoperacyjności z § 1.

**Konstrukcja urządzenia.** Gabaryty, materiał obudowy, sposób montażu i rozmieszczenie podzespołów
nie są wymaganiami. Dobiera je wykonawca. Przedmiotem wymagań są funkcje, a wartości liczbowe
stosuje się wyłącznie w przypadkach, w których są konieczne do jednoznacznej weryfikacji funkcji.

Trzon wymagań pozostaje wyprowadzony ze **stanu faktycznie zrealizowanego**, a nie z wymagań
postawionych w postępowaniu: opisuje poziom, który rynek już dostarczył. Zestawienie tych wymagań
z dokumentacją dostarczonego zestawu prowadzone jest odrębnie, w dokumencie roboczym, który nie
stanowi części materiału przeznaczonego do rozpowszechniania.

**Rozróżnienie istotne przy zakupie.** Sterownik może być **platformą sprzętową,
a nie centralą alarmową**: wiele urządzeń tej klasy wprost wyłącza ze swojej dokumentacji logikę
alarmową, protokoły aplikacyjne i uwierzytelnianie. Wymagania z części A, B i C dotyczą więc
**oprogramowania**, a nie wyłącznie sprzętu. Dostawa samej platformy sprzętowej nie oznacza
spełnienia wymagań SOiA.

---

## A. Weryfikacja polecenia

Weryfikacja polecenia stanowi podstawowy mechanizm zapobiegający uruchomieniu syreny bez spełnienia
warunków wykonania. Poziom 0 nie wymaga rejestracji urządzenia, dlatego poprawność implementacji
tego mechanizmu musi zostać potwierdzona w ramach badań zgodności i odbioru.

Zasada nadrzędna brzmi: **sam fakt, że wiadomość dotarła zaufaną drogą, nie uprawnia do uruchomienia
syreny.** Uprawnia dopiero zweryfikowana treść. Dotyczy to każdego kanału bez wyjątku — sieci
wydzielonej, zamkniętej grupy abonenckiej, radiostacji i połączenia przewodowego tak samo jak
publicznego Internetu.

> [!important] SMS, IoT Feed i powiadomienie — trzy różne funkcje
> Wymagania podpisu oraz pól podpisanej treści w tej części opisują IoT Feed używany w torze danych. Kanał powiadomienia tylko informuje o zmianie Feedu i wyzwala jego pobranie. SMS jest odrębnym kanałem wykonawczym SYRENY.soia; jego profil i kontrole opisują część D oraz załącznik nr 8. Niezależnie od kanału urządzenie stosuje właściwą dla niego walidację, ochronę przed powtórzeniem, regułę obszaru, kontrolę czasu i zasadę fail-closed.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-A01 | MUSI | **I** | Zweryfikować podpis odebranej treści przed jakimkolwiek działaniem wykonawczym |
| W-A02 | MUSI | **I** | Odrzucić całą treść przy niepowodzeniu weryfikacji — nie wykonywać jej części |
| W-A03 | MUSI | **I** | Rozpoznawać identyfikator klucza i odrzucać treść podpisaną kluczem nieznanym |
| W-A04 | MUSI | **I** | Obsłużyć okres nakładania się klucza bieżącego i poprzedniego, żeby wymiana klucza nie przerywała pracy |
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
| W-A15 | MUSI | **I** | Utrzymywać czas z co najmniej **dwóch niezależnych źródeł**, posiadać zegar podtrzymywany na czas ich niedostępności, znać **wiek własnej ostatniej synchronizacji** i sygnalizować jego przekroczenie ponad dobę |
| W-A16 | POWINIEN | **I** | Na kanale umożliwiającym odpowiedź — potwierdzić **przyjęcie** polecenia, odrębnie od jego **wykonania** |
| W-A17 | MUSI | **I** | Odrzucić treść przekraczającą **ogłoszony limit rozmiaru** — wykazu jako całości i pojedynczego polecenia — traktując przekroczenie jako błąd, a nie jako brak poleceń |

Wymaganie W-A08 bywa pomijane, a jest krytyczne dla przyszłości: katalog sygnałów będzie się
rozszerzał, a urządzenie, które na nieznany kod reaguje zawieszeniem albo odrzuceniem całej treści,
przestanie działać w dniu rozszerzenia słownika.

### Uzasadnienie progu 30 sekund i znaczenie źródeł czasu

Ocena dopuszczalności rozpoczęcia emisji zależy od znacznika czasu w poleceniu i od zegara
urządzenia. Istotna rozbieżność czasu może spowodować odrzucenie prawidłowego polecenia.

Próg 30 sekund przyjęto jako wartość istotnie mniejszą od trzyminutowego okna rozpoczęcia.
Odpowiada on jednej szóstej długości tego okna i ogranicza wpływ dryfu na kwalifikację polecenia.

> [!note] Państwowe źródła czasu
> Zgodnie z przyjętym modelem urządzenie konfiguruje co najmniej dwa państwowe serwery NTP wskazane w obowiązującym profilu. Próg dryfu 30 sekund pozostaje bez zmian. Zegar podtrzymywany zachowuje ciągłość podczas niedostępności serwerów, ale nie zastępuje źródła odniesienia. Urządzenie zna wiek ostatniej synchronizacji i sygnalizuje jego przekroczenie zgodnie z W-A15.

Moduł pozycjonowania pozostaje wymaganiem urządzenia służącym między innymi ustaleniu położenia. W tym dokumencie nie jest przedstawiany jako podstawowe źródło czasu, ponieważ przyjętym źródłem odniesienia są państwowe serwery NTP.

### Uzasadnienie limitów rozmiaru danych

Rdzeń może być realizowany na mikrokontrolerze o ograniczonej pamięci. Brak ogłoszonej górnej
granicy rozmiaru wykazu stanowiłby jednocześnie ryzyko bezpieczeństwa i dostępności, ponieważ
odpowiedź przekraczająca zasoby urządzenia mogłaby przerwać jego działanie.

Dlatego limity są ogłaszane maszynowo pod adresem produkcyjnym, na zasadach z § 4 Wytycznych,
a urządzenie odrzuca treść, która je przekracza. Wartości proponowane do przyjęcia: **8 kB** dla
pojedynczego polecenia i **2 MB** dla całego wykazu — z zapasem na obszar obejmujący kilkaset gmin.

Z tego wynika też wskazówka konstrukcyjna, a nie wymaganie: urządzenie o małej pamięci powinno
weryfikować i przetwarzać wykaz **strumieniowo**, nie buforując go w całości.

**Kanał tekstowy ma odrębne ograniczenie.** Polecenie musi mieścić się w jednej wiadomości
— 160 znaków w podstawowym alfabecie. Składnia poleceń używa więc wyłącznie znaków tego alfabetu:
**polskie znaki diakrytyczne przełączają kodowanie i skracają wiadomość do 70 znaków**, co przy
dłuższym poleceniu wymusiłoby podział. Wiadomości wieloczęściowe są niedopuszczalne (W-D24), ponieważ wiadomość
wieloczęściowa potrafi dotrzeć niekompletna albo w innej kolejności, a polecenie sklejane
z fragmentów przestaje być poleceniem, którego treść dało się zweryfikować.

---

## B. Obszar działania

Reguła obszaru rozstrzyga, czy polecenie dotyczy tego konkretnego urządzenia. Błąd w tym miejscu
oznacza albo milczenie syreny podczas realnego zagrożenia, albo uruchomienie alarmu tam, gdzie
zagrożenia nie ma. Oba są poważne, ale drugi jest trudniejszy do odwrócenia.

Kod obszaru w poleceniu musi być równy kodowi urządzenia albo wobec niego nadrzędny. Zależność
w drugą stronę nie wystarcza: ostrzeżenie dla jednej gminy nie uruchamia syreny opisanej kodem
całego powiatu.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-B01 | MUSI | **I** | Przechowywać obszar działania jako listę **siedmiocyfrowych** kodów gmin |
| W-B02 | MUSI | **I** | Odrzucić albo zgłosić jako błąd konfigurację kodem dwucyfrowym lub czterocyfrowym |
| W-B03 | MUSI | **I** | Odrzucić kod sześciocyfrowy, bez cyfry rodzaju, jako niepełny |
| W-B04 | MUSI | **I** | Uwzględniać cyfrę rodzaju gminy: kod gminy miejsko-wiejskiej obejmuje jej miasto i jej obszar wiejski, a te dwa są względem siebie rozłączne |
| W-B05 | MUSI | **I** | Pomijać kody miejscowości i ulic — mają własną numerację i porównanie prefiksowe daje trafienia przypadkowe |
| W-B06 | MUSI | **I** | Uznać polecenie za dotyczące urządzenia, gdy pasuje co najmniej jeden kod obszaru |
| W-B07 | MUSI | **I** | Traktować kod nierozpoznany — o innej długości albo nienumeryczny — jako brak dopasowania; nigdy nie „naprawiać” go przez obcięcie ani dopełnienie |
| W-B08 | POWINIEN | **I** | Udostępniać skonfigurowany obszar do odczytu w rejestrze zdarzeń i w eksporcie konfiguracji |

Wymaganie W-B02 wynika z realnego ograniczenia systemu i nie jest formalnością. Dyżurny może zadać
obszar alertu, rysując kształt na mapie. Taki alert niesie kody wszystkich objętych **gmin**, a nie
kod powiatu — bo jawny kod jednostki oznaczałby całą jednostkę, także tam, gdzie kształt jej nie
objął. Urządzenie skonfigurowane kodem powiatu na taki alert **nie zareaguje**. Ciche przyjęcie
takiej konfiguracji jest błędem, który ujawni się dopiero podczas zagrożenia.

---

## C. Sygnały akustyczne i komunikaty

Urządzenie ma odtwarzać sygnał wzorcowy, a nie własną interpretację opisu słownego. Wzorcem są
pliki referencyjne zatwierdzone przez KG PSP; ich modyfikacja jest niedopuszczalna, a zgodność
sprawdza się sumą kontrolną, nie odsłuchem.

**System nie przenosi dźwięku.** Pliki udostępnia się do pobrania ze strony SOiA, a wgrywa
**przy instalacji** — dokładnie tak, jak robiono to dotychczas. W instalacji, w której pliki
znajdują się w pamięci samej syreny, sterownik nie przechowuje ich w ogóle i **nie podlega
wymaganiom klasy II**.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-C01 | MUSI | **I** | Umieć wyemitować **wszystkie cztery** sygnały akustyczne określone w rozporządzeniu, niezależnie od tego, które są w danym czasie wyzwalane centralnie |
| W-C02 | MUSI | **II** | Odtwarzać wyłącznie niezmodyfikowane pliki referencyjne |
| W-C03 | MUSI | **I** | Potwierdzić sumę kontrolną pliku przed jego instalacją, **względem wartości podanej w Wytycznych z dnia 28 maja 2025 r.** |
| W-C04 | MUSI | **II** | Obsługiwać format plików referencyjnych: WAV PCM 16 bit mono, próbkowanie nie mniejsze niż 8 kHz |
| W-C05 | MUSI | **I** | Zachować czas trwania sygnału w tolerancji ±5 % względem wzorca |
| W-C06 | MUSI | **I** | Zachować strukturę czasową sygnału — modulację oraz liczbę i długość przerw |
| W-C07 | MUSI | **II** | Utrzymać poziom w granicach ±3 dB względem wzorca, bez przesterowania, w zadeklarowanym i udokumentowanym punkcie pomiarowym |
| W-C08 | MUSI | **I** | Zakończyć emisję samoistnie po czasie właściwym dla sygnału, bez polecenia z zewnątrz |
| W-C09 | MUSI | **I** | Traktować odwołanie alarmu jako **emisję sygnału**, a nie jako zaprzestanie emisji |
| W-C10 | MUSI | **II** | Przechowywać komplet plików referencyjnych z zapasem na **dwie wersje pakietu** — co najmniej 32 MB pamięci trwałej przeznaczonej na pakiet dźwiękowy |
| W-C11 | POWINIEN | **III** | Umożliwiać odtworzenie komunikatu nagranego oraz komunikatu wygenerowanego z tekstu w języku polskim |
| W-C12 | POWINIEN | **III** | Wykonywać syntezę mowy **lokalnie na urządzeniu**, bez łączności z usługą zewnętrzną |
| W-C13 | POWINIEN | **III** | Syntezować komunikat **do bufora przed rozpoczęciem odtwarzania**, nigdy w trakcie emisji |
| W-C14 | POWINIEN | **III** | Zapewniać powtarzalność: ten sam tekst przy tej samej wersji modelu daje ten sam dźwięk |
| W-C15 | POWINIEN | **III** | Przypinać i odnotowywać w rejestrze zdarzeń wersję modelu i głosu |
| W-C16 | POWINIEN | **III** | Umożliwiać nadpisanie wymowy nazw miejscowości, skrótów, jednostek, liczb, dat i godzin |
| W-C17 | MUSI | **III** | Zapewnić, że komunikat głosowy **nigdy nie opóźnia ani nie zastępuje** sygnału akustycznego z pliku referencyjnego |

### Uzasadnienie pojemności określonej w wymaganiu W-C10

Cztery pliki o łącznym czasie 600 sekund, w formacie PCM 16 bitów przy 8 kHz mono, zajmują 9,6 MB.
Zapas na dwie wersje pakietu wymaga niespełna 20 MB. Minimalna pojemność 32 MB wynika z tego
obliczenia i zapewnia dodatkowy margines eksploatacyjny.

### Status wymagań klasy III

Kontrakt SOiA nie przenosi obecnie treści głosowej. Wymagania W-C11–W-C16 opisują zatem zdolność
opcjonalną, której system centralny obecnie nie uruchamia.

Pominięcie klasy III nie ogranicza funkcji alarmowania akustycznego. Uwzględnienie tej klasy
oznacza przygotowanie urządzenia do przyszłej obsługi treści głosowej, a nie zakup aktualnie
dostępnej usługi centralnej.

**Drogą podstawową jest treść przygotowana wcześniej.** Dla syreny większość komunikatów jest znana
z góry — ostrzeżenia typowe, komunikaty ewakuacyjne, informacje porządkowe. Wygenerowanie ich raz,
na komputerze, i odtwarzanie z pamięci znosi całe wymaganie obliczeniowe: urządzenie potrzebuje
wtedy wyłącznie odtwarzacza, czyli klasy II. Synteza na urządzeniu jest potrzebna dokładnie tam,
gdzie treść jest zmienna: nazwa miejscowości, godzina, kierunek, numer sektora.

### Uzasadnienie lokalnego wykonywania syntezy mowy

Komunikat głosowy jest potrzebny dokładnie wtedy, kiedy najbardziej prawdopodobna jest awaria
łączności — podczas zdarzenia masowego, przy przeciążonej sieci albo przy zaniku zasilania
w okolicy. Synteza wykonywana zdalnie jest w takim przypadku zależna od dostępności usługi
i łączności. Synteza lokalna ogranicza tę zależność oraz potrzebę przekazywania treści do usługi
zewnętrznej.

**Poziom odniesienia sprzętowego dla klasy III.** Wymagania W-F07 i W-F08 podają poziom wyższy niż
sam próg wykonalności syntezy — bo wynikają ze **stanu faktycznie zrealizowanego**, a nie z minimum
obliczeniowego. Poniższe wartości opisują, gdzie leży sam próg. Synteza neuronowa wymaga systemu 64-bitowego,
czterordzeniowego procesora klasy aplikacyjnej, co najmniej 512 MB pamięci operacyjnej — praktycznie
1 GB — i co najmniej 512 MB wolnej pamięci masowej. Model powinien pozostawać załadowany w pamięci,
aby czas jego inicjalizacji nie opóźniał komunikatu alarmowego. Projekt nie wymaga akceleratora
sprzętowego — obliczenia mają wykonywać się na procesorze ogólnego
przeznaczenia, bo uzależnienie od układu neuronowego konkretnego producenta byłoby nowym
uzależnieniem.

**Kategorie rozwiązań.** Projekt nie wskazuje konkretnego narzędzia, lecz opisuje dwie kategorie
technologiczne.

*Synteza neuronowa*: model kilkudziesięciu megabajtów, uruchamiany na procesorze, syntezujący
szybciej niż w czasie rzeczywistym na sprzęcie opisanej klasy. Naturalność zbliżona do mowy ludzkiej.

*Synteza formantowa*: wielokrotnie mniejsza — dane dla języka polskiego mieszczą się w niecałym
megabajcie — i wielokrotnie szybsza, wykonalna nawet na mikrokontrolerze. Głos wyraźnie syntetyczny,
ale zrozumiały i praktycznie niezawodny. Dla komunikatu ostrzegawczego liczy się zrozumiałość, nie
naturalność, więc jest to rozwiązanie dopuszczalne, a nie tylko zapasowe.

**Licencja stanowi element wymagania.** W materiale źródłowym wskazano, że przegląd rynku
przeprowadzony w sierpniu 2026 r. wykazał ograniczoną dostępność polskich głosów o warunkach
licencyjnych odpowiednich do zamierzonego zastosowania. Wniosek ten wymaga udokumentowania
i ponownego potwierdzenia przed podpisaniem projektu.

Projekt przewiduje centralne zamówienie polskiego głosu przez KG PSP i jego publiczne
udostępnienie. Do czasu odrębnej realizacji zapis ten należy traktować jako działanie planowane.
Wykonawca może zastosować własne rozwiązanie, o ile wykaże odpowiednie prawa licencyjne.

**Aktualizacja modelu jest zmianą, nie poprawką.** Zmieniona wymowa nazwy miejscowości w komunikacie
alarmowym to realny problem — stąd wymóg przypięcia wersji z W-C15.

---

## D. Kanały i łączność

Uniwersalność sterownika polega na tym, że przyjmuje polecenia z wielu niezależnych źródeł
i traktuje je jednakowo. Kanał zmienia sposób dostarczenia, nigdy znaczenie polecenia ani zakres
weryfikacji z części A.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-D01 | MUSI | **I** | Pobierać wykaz poleceń z publicznego punktu dostępu nie rzadziej niż co 30 s |
| W-D02 | MUSI | **I** | Stosować warunkowe pobranie i obsługiwać odpowiedź „bez zmian” |
| W-D03 | MUSI | **I** | Honorować odpowiedź o przekroczeniu limitu zapytań wraz ze wskazanym czasem wstrzymania |
| W-D04 | MUSI | **I** | Stosować kontrolowane wycofanie po błędach i losowe rozproszenie momentu odpytania |
| W-D05 | MUSI | **I** | Utrzymywać cykliczne pobieranie **także wtedy**, gdy działa kanał niezwłocznego powiadomienia |
| W-D06 | MUSI | **I** | Umożliwiać podłączenie do sieci lokalnej obiektu przewodowo, bez modemu i bez karty abonenckiej |
| W-D07 | MUSI | **I** | Obsługiwać **co najmniej cztery niezależne tory sieciowe przewodowe**, zarządzalne z poziomu systemu: identyfikacja toru, odczyt stanu i parametrów łącza oraz administracyjne włączenie i wyłączenie każdego z nich |
| W-D08 | MUSI | **I** | Posiadać interfejs bezprzewodowy pracujący co najmniej w dwóch pasmach, z obsługą aktualnego standardu zabezpieczeń |
| W-D09 | MUSI | **I** | Posiadać **odrębny interfejs stacji radiowej** — port sieciowy albo szeregowy przeznaczony do podłączenia stacji dyspozytorskiej jako kolejnego źródła polecenia. Interfejs ten jest niezależny od toru audio i od sterowania nadawaniem |
| W-D10 | MUSI | **I** | Posiadać interfejs radiowy dalekiego zasięgu małej przepływności, interoperacyjny z serwerem sieciowym wskazanym przez zamawiającego |
| W-D11 | MUSI | **I** | Posiadać moduł komunikacji komórkowej z obsługą wiadomości tekstowych, **bez blokady operatorskiej karty abonenckiej** |
| W-D12 | MUSI | **I** | Umożliwiać wymianę karty abonenckiej oraz samodzielną konfigurację parametrów dostępu do sieci |
| W-D13 | MUSI | **I** | Przy odbiorze polecenia tekstowego stosować łącznie: wykaz numerów uprawnionych, walidację treści, rejestrację zdarzenia z numerem nadawcy, czasem, treścią polecenia i wynikiem oraz możliwość wyłączenia tej funkcji |
| W-D14 | MUSI | **I** | Nie wykonywać tego samego polecenia tekstowego powtórnie w zdefiniowanym oknie i odnotować odrzucenie |
| W-D15 | MUSI | **I** | Przyjmować **konfigurowalny** adres punktu dostępu, adres kanału powiadomienia i numery uprawnione |
| W-D16 | MUSI | **I** | Posiadać wielokonstelacyjny moduł pozycjonowania satelitarnego z odczytem współrzędnych i statusu ustalenia pozycji |
| W-D17 | POWINIEN | **I** | Kontynuować pracę na kanale zapasowym przy utracie kanału podstawowego, bez zmiany zakresu weryfikacji |
| W-D18 | MUSI | **I** | Stosować **hasło sterujące unikalne dla urządzenia**; hasło wspólne dla floty jest niedopuszczalne |
| W-D19 | MUSI | **I** | Rejestrować i sygnalizować **odrzucenie polecenia tekstowego** — nieznany numer, błędne hasło, polecenie spoza mapy — wraz z numerem nadawcy i czasem |
| W-D20 | MUSI | **I** | Przyjąć bez wymiany sprzętu kartę abonencką i konfigurację sieci wydzielonej wprowadzane w fazie docelowej |
| W-D21 | MUSI | **D** | Posiadać gniazdo wymiennej karty abonenckiej **dostępne bez demontażu urządzenia z uchwytu**, z mocowaniem zabezpieczającym kartę przed wysunięciem przy drganiach; dokumentacja wskazuje, czy wymiana wymaga wyłączenia urządzenia |
| W-D22 | POWINIEN | **D** | Obsługiwać kartę klasy przemysłowej — o rozszerzonym zakresie temperatur pracy i podwyższonej wytrzymałości zapisu względem karty konsumenckiej |
| W-D23 | POWINIEN | **D** | Obsługiwać kartę zdalnie prowizjonowaną, w postaci wymiennej lub wlutowanej |
| W-D24 | MUSI | **I** | Przyjmować polecenie tekstowe wyłącznie jako **pojedynczą wiadomość** — do 160 znaków podstawowego alfabetu, bez sklejania wiadomości wieloczęściowych — i odrzucać wszystko, co tego warunku nie spełnia |
| W-D25 | MUSI | **I** | Weryfikować w poleceniu tekstowym **znacznik czasu i monotoniczny licznik**; odrzucać wiadomość, której znacznik odbiega od czasu urządzenia bardziej niż o dopuszczalny margines albo której licznik nie jest wyższy od ostatnio przyjętego |

### Wymagania dotyczące kart abonenckich

Karta abonencka jest eksploatowana przez wiele lat w urządzeniu narażonym na zmiany temperatury
i drgania. Jej fizyczna wymiana wymaga obsługi w miejscu instalacji, co ma wpływ na koszty
i organizację utrzymania.

**Klasa przemysłowa.** Istnieje osobna norma dla kart maszynowych, obejmująca formaty wlutowane
oraz klasy temperaturowe wykraczające poza zakres kart konsumenckich, wraz z podwyższoną
wytrzymałością zapisu. Dla urządzenia pracującego w nieogrzewanym obiekcie ma to znaczenie
praktyczne.

**Możliwość zdalnej zmiany operatora.** Waga tego wymagania ujawnia się dopiero przy skali
docelowej. Przejście z kart własnych jednostek samorządu na karty KG PSP w sieci wydzielonej
oznacza — przy karcie zwykłej — **fizyczną wymianę karty w każdym urządzeniu**, czyli ogólnokrajową
kampanię terenową przy około dwudziestu trzech tysiącach lokalizacji. Karta zdalnie prowizjonowana
zamienia tę kampanię w operację wykonywaną zdalnie.

Wymaganie jest zalecane, a nie bezwzględne, bo dostępność takich kart u operatorów bywa różna
i podlega negocjacji handlowej. Zamawiający powinien jednak policzyć koszt jego pominięcia: jest to
koszt jednego wyjazdu serwisowego pomnożony przez liczbę zainstalowanych urządzeń.

**Dostępność gniazda.** Wymaganie W-D21 wygląda na oczywiste, dopóki nie okaże się, że wymiana karty
wymaga zdjęcia szafki ze ściany albo — co bywa równie kłopotliwe — pełnego wyłączenia instalacji
z eksploatacji. Dlatego dokumentacja ma tę drugą okoliczność wskazać wprost.

Wymaganie W-D06 zasługuje na komentarz, bo bywa pomijane przy projektowaniu. Wiele syren stoi na
obiektach, które mają już sieć — remiza, urząd gminy albo szkoła. Połączenie przewodowe może w takim
przypadku stanowić stabilny tor podstawowy, a łączność komórkowa — tor zapasowy. Wymóg użycia karty
abonenckiej nie powinien wykluczać możliwości pracy przez istniejącą sieć lokalną.

### Zasady funkcjonowania kanału tekstowego w okresie przejściowym 2026–2027

Projekt zakłada, że w okresie przejściowym 2026–2027 jednostki samorządu terytorialnego korzystają
z kart abonenckich własnych operatorów, a nie z kart KG PSP w sieci wydzielonej. Zamknięta grupa
abonencka nie jest wówczas dostępna, a kanał tekstowy zabezpieczają reguły konfigurowane
na urządzeniu, hasło sterujące, znacznik czasu i licznik.

Brak zamkniętej grupy zmienia rozkład ryzyka, ponieważ sieć nie ogranicza możliwości wysłania
wiadomości do numeru urządzenia wyłącznie do uczestników grupy. Ze względu na możliwość podszycia
się pod numer nadawcy na niektórych trasach sama lista numerów uprawnionych nie jest wystarczająca.
Wymaganie W-D18 przewiduje zatem hasło unikalne dla każdego urządzenia, aby kompromitacja jednego
sekretu nie obejmowała całej floty.

W okresie przejściowym, jeżeli dostępny jest tor IP, kanał tekstowy powinien mieć charakter
uzupełniający. Odrzucone polecenie z nieznanego numeru stanowi zdarzenie bezpieczeństwa i podlega
rejestracji zgodnie z W-D19.

Przejście do fazy docelowej nie zmienia składni poleceń ani kontraktu. Zmienia się karta abonencka
i numery uprawnione, dlatego W-D20 wymaga, żeby urządzenie kupione dziś przyjęło konfigurację fazy
docelowej bez wymiany sprzętu.

### Zakres funkcjonalny interfejsu stacji radiowej

Wymaganie W-D09 opisuje **punkt wpięcia**, a nie protokół konkretnego producenta. Stacja radiowa
dostarcza polecenie, sterownik weryfikuje je tak samo jak polecenie z każdego innego kanału.
Adapter stacji deklaruje, jakie funkcje obsługuje i jak mapuje sygnały; nie tworzy własnej
semantyki alarmu. Interfejs ten ma być otwarty dla niezależnego wykonawcy — ograniczenie go do
jednej, zamkniętej funkcji aplikacyjnej producenta jest sprzeczne z częścią I — Swobodą wyboru dostawcy.

Interfejsu stacji radiowej **nie wolno mylić z torem audio i sterowaniem nadawaniem syreny**
(W-E02 i W-E05). Pierwszy służy do przyjęcia polecenia z zewnątrz, drugie — do wysterowania
syreny. Są to osobne funkcje na osobnych złączach i urządzenie musi mieć oba.

---

## E. Wysterowanie syreny

Sterownik obsługuje oba profile wykonawcze, bo o tym, który zostanie użyty, decyduje instalacja,
a nie model urządzenia. Wymagania elektryczne są tu wiążące, bo od nich zależy zgodność brzmienia
z wzorcem i bezpieczeństwo pracy.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-E01 | MUSI | **I** | Zapewniać co najmniej dwa niezależne sposoby wysterowania syreny |
| W-E02 | MUSI | **II** | Posiadać wyjście audio liniowe o poziomie nie niższym niż 1,0 V RMS, **z zadeklarowaną tolerancją** i **regulacją poziomu realizowaną programowo** — nie elementem regulacyjnym na płycie — o impedancji wyjściowej nie większej niż 50 Ω, stosunku sygnału do szumu nie gorszym niż 90 dB i zniekształceniach nie większych niż 0,1 %, z dwoma kanałami przypisywanymi programowo niezależnie |
| W-E03 | MUSI | **I** | Zapewniać co najmniej **sześć niezależnych torów stykowych** bezpotencjałowych w układzie NO/NC/COM, o obciążalności nie mniejszej niż 8 A przy 250 V AC i trwałości łączeniowej nie mniejszej niż milion cykli |
| W-E04 | MUSI | **I** | Zapewnić co najmniej jedno wyjście do obwodu 230 V z izolacją galwaniczną nie mniejszą niż **4 kV** między obwodem sterowania a torem mocy oraz fizyczną izolację chroniącą przed porażeniem podczas prac serwisowych |
| W-E05 | MUSI | **II** | Zapewnić **niezależne sterowanie nadawaniem** — zwarciowe wejście nadawania syreny — działające równolegle z wyjściem audio i sterowane osobno od niego, z udokumentowanymi parametrami elektrycznymi |
| W-E06 | MUSI | **I** | Nie sterować obwodem mocy syreny silnikowej bezpośrednio z wyjść ogólnego przeznaczenia — wyłącznie przez certyfikowaną, izolowaną warstwę wykonawczą |
| W-E07 | MUSI | **I** | Ograniczać maksymalny czas ciągłego zasilania układu wykonawczego syreny silnikowej |
| W-E08 | MUSI | **I** | Posiadać lokalne, sprzętowe **odcięcie** toru wykonawczego, niezależne od łączności i od oprogramowania, mające pierwszeństwo przed poleceniem zdalnym |
| W-E09 | MUSI | **I** | Nie wznawiać samoczynnie przerwanej emisji po niekontrolowanym restarcie |
| W-E10 | MUSI | **II** | Umożliwiać wysterowanie istniejącej syreny **jako systemu nagłośnieniowego** — przez podanie sygnału liniowego na jej wejście audio przy jednoczesnym zwarciu jej wejścia nadawania — bez korzystania z jakiegokolwiek interfejsu programowego producenta syreny |
| W-E11 | POWINIEN | **I** | Wykrywać stan układu wykonawczego — obecność obciążenia, gotowość wzmacniacza, stan stycznika |
| W-E12 | POWINIEN | **I** | Rozróżniać w rejestrze zdarzeń przyjęcie polecenia, zaplanowanie akcji, aktywowanie wyjścia, wykrycie obciążenia i zakończenie emisji |
| W-E13 | MUSI | **I** | Zapewnić, że **pojedyncze uszkodzenie obwodu obiektowego** — zwarcie albo przeciążenie wyjścia — nie wyłącza urządzenia ani nie uniemożliwia pracy toru wykonawczego |
| W-E14 | MUSI | **I** | Wykrywać na wejściu uruchomienia lokalnego impuls o czasie trwania nie dłuższym niż **200 ms** i podać w dokumentacji częstotliwość próbkowania wejść |

Rozróżnienie określone w W-E12 ma znaczenie przy ustalaniu przyczyny braku emisji.
Potwierdzenie, że wyjście zostało aktywowane, **nie jest dowodem słyszalności** — i żaden zapis
w tym załączniku takiego dowodu nie zastępuje.

Wymagania W-E13 i W-E14 wynikają z obserwacji rzeczywistej konstrukcji. Brak indywidualnego
zabezpieczenia wyjść może spowodować, że pojedynczy błąd okablowania albo uszkodzenie izolacji
wyłączy cały sterownik. Zbyt mała częstotliwość próbkowania wejścia może natomiast uniemożliwić
wykrycie krótkiego impulsu uruchomienia lokalnego.

### Tryby sprzężenia sterownika z syreną

Sposób, w jaki sterownik uruchamia syrenę, zależy od tego, co syrena potrafi. Wytyczne uznają trzy
tryby za równoprawne — każdy musi wystarczać do pełnego alarmowania, a zamawiający wybiera stosownie
do instalacji.

**Tryb cyfrowy — przez interfejs syreny.** Syrena ma własny odtwarzacz i sloty dźwiękowe, a sterownik
wywołuje jej udokumentowane polecenia: odtwórz wskazany slot, podaj stan. Połączenie realizowane
jest standardową warstwą fizyczną — szeregową, sieciową, uniwersalną albo wejściami i wyjściami ogólnego
przeznaczenia — a nie złączem autorskim. Warunkiem stosowania tego trybu jest otwarta dokumentacja
producenta syreny (W-I11 do W-I14). **W tym trybie sterownik nie odtwarza dźwięku i nie podlega
klasie II.**

**Tryb audio — syrena jako system nagłośnieniowy.** Sterownik sam odtwarza plik referencyjny i podaje
sygnał liniowy na wejście audio syreny, jednocześnie zwierając jej wejście nadawania. Syrena pełni
wtedy rolę wzmacniacza z przetwornikiem i nie musi wiedzieć nic o SOiA, o slotach ani o katalogu
sygnałów. **Ten tryb wymaga klasy II.**

Tryb audio ogranicza zależność od nieudokumentowanego interfejsu programowego producenta. Wymaga
dwóch fizycznych punktów integracji: wejścia liniowego i sterowania nadawaniem. Jego zastosowanie
podlega ocenie zgodności z dokumentacją, warunkami gwarancji i wymaganiami bezpieczeństwa.
Wierność sygnału zapewnia w tym wariancie sterownik odtwarzający zweryfikowany plik referencyjny.

**Tryb stykowy — syrena silnikowa.** Sterownik zamyka obwód przez tor stykowy, a modulację realizuje
programem sterującym układem wykonawczym. Wymaga certyfikowanej, izolowanej warstwy mocy
i ograniczenia czasu pracy ciągłej.

Kryteria odbioru sprawdzają **tryb faktycznie zastosowany w danej instalacji**, a nie deklarowany
w ofercie.

### Zasada niepodzielności emisji

Zgodnie z przyjętym wymaganiem rozpoczęta sekwencja sygnału jest wykonywana do końca. Jedno
zakwalifikowane polecenie oznacza jedną pełną emisję, a jej rozpoczęciu można zapobiec wyłącznie
przed wejściem urządzenia w stan `EMITTING`.

Urządzenie MUSI dokończyć rozpoczętą sekwencję i MUSI odrzucić próbę jej przerwania poleceniem
zdalnym. Jednolite zachowanie urządzeń jest warunkiem interoperacyjności określonej w § 1.

**Odcięcie z W-E08 to co innego niż zatrzymanie.** Jest czynnością na obwodzie wykonawczym —
przerwaniem zasilania wzmacniacza albo układu rozruchowego — a nie poleceniem przerwania sekwencji.
Dla syreny silnikowej oznacza zatrzymanie wirnika pracującego pod obciążeniem, ze wszystkimi tego
skutkami mechanicznymi, więc jest środkiem awaryjnym, a nie zwykłą operacją.

Jeżeli alarm ogłoszono omyłkowo po rozpoczęciu emisji, sekwencja trwa przez pełny czas właściwy
dla danego sygnału. Działaniem operacyjnym jest odwołanie alarmu, stanowiące odrębny sygnał ciągły
trwający trzy minuty.

---

## F. Platforma sterownika

Wymagania platformowe wynikają z tego, że urządzenie ma pracować kilkanaście lat i przyjmować
aktualizacje. **Rdzeń nie wymaga komputera** — mieści się na mikrokontrolerze. Komputera wymaga
dopiero profil głosowy, i dlatego wartości liczbowe opisujące platformę występują wyłącznie
w klasie III — poza pojemnością pakietu dźwiękowego z W-C10, która jest wyliczeniem, a nie parametrem
platformy.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-F01 | MUSI | **I** | Posiadać **udokumentowaną ścieżkę aktualizacji bezpieczeństwa przez cały deklarowany okres wsparcia**: z podpisem, wersjonowaniem i możliwością odtworzenia dowolnej wydanej wersji |
| W-F02 | MUSI | **I** | Umożliwiać aktualizację **bez dostępu do publicznego Internetu**, z zachowaniem podpisów |
| W-F03 | MUSI | **I** | Mieć konfigurację utwardzoną: wyłączone zbędne usługi, ograniczone porty, lokalną zaporę, brak kont i haseł domyślnych |
| W-F04 | MUSI | **I** | Udostępniać zdalny dostęp administracyjny wyłącznie z uwierzytelnieniem kluczem; hasło nie może być jedynym mechanizmem |
| W-F05 | MUSI | **I** | Przechowywać klucze w sposób **nieeksportowalny** — w układzie dyskretnym albo bezpiecznej enklawie procesora — oraz weryfikować integralność rozruchu |
| W-F06 | MUSI | **I** | Posiadać sprzętowy układ nadzoru pracy, samoczynnie restartujący urządzenie przy zawieszeniu oprogramowania |
| W-F07 | MUSI | **III** | Mieć procesor 64-bitowy o co najmniej **czterech rdzeniach** i taktowaniu nie mniejszym niż **1,5 GHz** |
| W-F08 | MUSI | **III** | Mieć co najmniej **4 GB** pamięci operacyjnej i co najmniej **32 GB** pamięci trwałej klasy przemysłowej |
| W-F09 | MUSI | **I** | Prowadzić zapis logów bieżących w pamięci ulotnej z cykliczną synchronizacją i rotacją, żeby nie zużyć przedwcześnie pamięci trwałej — **przy zachowaniu trwałości wymaganej w W-G11** |
| W-F10 | MUSI | **I** | Przyjmować podpisane aktualizacje w układzie dwóch obrazów, z automatycznym powrotem do poprzedniej wersji przy nieudanej aktualizacji i **z zachowaniem materiału kryptograficznego** |
| W-F11 | POWINIEN | **I** | Udostępniać udokumentowany lokalny interfejs integracyjny do sterowania funkcjami urządzenia |
| W-F12 | POWINIEN | **I** | Umożliwiać właścicielowi uruchamianie własnych komponentów jako usług systemowych albo w kontenerach |
| W-F13 | MUSI | **D** | Udostępniać w zestawie porty rozszerzeń ogólnego przeznaczenia oraz **co najmniej sześć wejść dwustanowych i sześć wyjść** ogólnego przeznaczenia, z podaniem parametrów elektrycznych i przepustowości portów |
| W-F14 | MUSI | **I** | Udostępnić **udokumentowaną procedurę przekazania właścicielowi zdolności podpisywania obrazów** albo depozyt kluczy podpisujących — tak, żeby weryfikacja rozruchu z W-F05 nie zamykała urządzenia trwale u producenta |

### Uzasadnienie neutralności technologicznej wymagania W-F01

Wcześniejsza wersja tego wymagania żądała systemu z repozytoriami bezpieczeństwa i menedżerem
pakietów. Był to opis **jednego ze sposobów**, a nie wymaganie wynikowe — i wykluczał rozwiązania
oparte na wymianie całego obrazu systemu, które dla urządzenia stojącego bez obsługi kilkanaście lat
są **lepsze**, bo nie pozostawiają miejsca na częściową, przerwaną aktualizację.

Liczy się skutek: że w piątym i dziesiątym roku eksploatacji istnieje droga wgrania poprawki
bezpieczeństwa, że poprawka jest podpisana i że da się wrócić do wersji poprzedniej.

### Relacja wymagań W-F05 i W-F14 do zasady swobody wyboru dostawcy

Wymaganie W-F05 żąda sprzętowej ochrony kluczy i weryfikacji rozruchu. Wymagania W-I02 i W-I07
żądają, żeby właściciel mógł zmienić punkt zaufania i wymienić materiał kryptograficzny **bez
udziału producenta**. W praktyce spotykanej na rynku te dwa oczekiwania bywają sprzeczne: kotwica
zaufania zapisywana jest w bezpiecznikach jednorazowych, po czym urządzenie zostaje trwale zamknięte
i właściciel nie może uruchomić własnego obrazu **nigdy**.

W-F14 ma pogodzić sprzętową weryfikację rozruchu z możliwością zmiany punktu zaufania przez
właściciela. Wykonawca przedkłada procedurę przekazania zdolności podpisywania albo składa klucze
do depozytu. Wybrany sposób musi zapewniać właścicielowi możliwość utrzymania urządzenia bez
trwałej zależności od producenta.

Brak realizacji W-F14 może uniemożliwić praktyczne wykonanie W-I02 i zmianę punktu zaufania
przez cały okres eksploatacji.

---

## G. Tryby pracy, diagnostyka i rejestr zdarzeń

Urządzenie musi jednoznacznie określać i sygnalizować swój stan. Pozostawienie trybu serwisowego
po zakończeniu prac konserwacyjnych może uniemożliwić wykonanie późniejszego polecenia zdalnego.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-G01 | MUSI | **I** | Rozróżniać tryby: pracy operacyjnej, ćwiczebny, serwisowy, zablokowany, ograniczony i awaryjny |
| W-G02 | MUSI | **I** | Blokować w trybie serwisowym i zablokowanym wykonanie polecenia zdalnego, zachowując możliwość testu lokalnego |
| W-G03 | MUSI | **I** | **Nie przełączać się samoczynnie** z trybu serwisowego lub zablokowanego do operacyjnego po restarcie |
| W-G04 | MUSI | **I** | Odnotowywać zmianę trybu w rejestrze zdarzeń wraz z czasem i przyczyną |
| W-G05 | MUSI | **I** | Prowadzić lokalny rejestr zdarzeń obejmujący co najmniej: źródło polecenia, wynik weryfikacji, decyzję wykonania, zmianę stanu wyjścia, restart wraz z przyczyną, zmianę trybu, aktualizację i wymianę materiału kryptograficznego |
| W-G06 | MUSI | **I** | Udostępniać rejestr zdarzeń w formacie otwartym, możliwym do odczytu bez oprogramowania producenta |
| W-G07 | MUSI | **I** | Nie ujawniać w rejestrze kluczy prywatnych ani pełnych wartości sekretów |
| W-G08 | MUSI | **I** | Sygnalizować **bez otwierania obudowy i bez podłączania komputera** co najmniej: pracę z zasilania rezerwowego, niski stan magazynu energii, gotowość operacyjną oraz brak łączności |
| W-G08a | MUSI | **I** | Rozróżniać w sygnalizacji stan gotowości od stanu braku łączności — tak, żeby dało się je odróżnić bez odczytu rejestru |
| W-G09 | POWINIEN | **I** | Umożliwiać eksport pełnej konfiguracji urządzenia w formacie otwartym |
| W-G10 | POWINIEN | **I** | Umożliwiać wykonanie testu cichego, niepowodującego emisji zewnętrznej |
| W-G11 | MUSI | **I** | Zachować rejestr zdarzeń **trwale, lokalnie i niezależnie od łączności**; restart urządzenia nie może usuwać zapisów, których nie zdążono wysłać |
| W-G12 | MUSI | **I** | Zapewnić rejestrowi pojemność i okres przechowywania nie krótszy niż **dwanaście miesięcy** zwykłej eksploatacji, z nadpisywaniem najstarszych zapisów po jego wyczerpaniu |

### Uzasadnienie zewnętrznej sygnalizacji stanu urządzenia

Wcześniejsze brzmienie W-G08 dopuszczało umieszczenie wszystkich wskaźników wewnątrz szafy
z obwodem 230 V. Odczyt stanu wymagał wówczas otwarcia szafy przez osobę posiadającą odpowiednie
kwalifikacje. Wymóg sygnalizacji zewnętrznej usuwa tę barierę.

Kanał publiczny nie zapewnia obecnie informacji zwrotnej o obecności urządzenia. Widoczna
z zewnątrz sygnalizacja umożliwia personelowi obiektu wykrycie długotrwałego braku łączności
bez otwierania obudowy i bez podłączania komputera.

Wymagania W-G11 i W-G12 wynikają z tej samej obserwacji. Rejestr utrzymywany wyłącznie w pamięci
ulotnej, którego niewysłane zapisy znikają po restarcie, nie jest rejestrem — a urządzenie odcięte
od łączności traci wtedy zdolność do udowodnienia, co się stało. Oszczędzanie pamięci trwałej,
o którym mówi W-F09, jest słuszne, ale oznacza **cykliczną synchronizację**, a nie rezygnację
z trwałości.

---

## H. Zasilanie i warunki środowiskowe

Wymagania z tej części dotyczą **całego zestawu** zainstalowanego w obiekcie. Zanik zasilania jest
jednym z najczęstszych scenariuszy towarzyszących zagrożeniu, więc podtrzymanie nie jest dodatkiem,
lecz warunkiem sensowności całej instalacji.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-H01 | MUSI | **D** | Zapewnić ciągłość pracy zestawu przez co najmniej **10 godzin** od zaniku zasilania sieciowego **w chwili odbioru** oraz co najmniej **8 godzin na koniec deklarowanego okresu gwarancji**; profil obciążenia przyjęty do wyznaczenia tych wartości obejmuje ciągłą emisję sygnału |
| W-H02 | MUSI | **D** | Określić model degradacji magazynu energii i przedłożyć świadectwo badania albo obliczenie dla profilu obciążenia z W-H01 |
| W-H03 | MUSI | **I** | Monitorować stan zasilania podstawowego i rezerwowego oraz odnotowywać jego zmiany |
| W-H04 | MUSI | **I** | Wykonać kontrolowane zamknięcie pracy przy wyczerpaniu zasilania rezerwowego |
| W-H05 | MUSI | **I** | Po powrocie zasilania odtworzyć stan trwały i **nie wykonywać polecenia, którego okno rozpoczęcia już minęło** |
| W-H06 | MUSI | **D** | Pracować w zakresie temperatur co najmniej od +10 °C do +40 °C przy wilgotności do 95 % bez kondensacji, w pomieszczeniu zamkniętym |
| W-H07 | POWINIEN | **D** | Udostępniać wykonanie o **rozszerzonym zakresie temperatur pracy**, co najmniej od −20 °C do +55 °C, dla zamawiających, u których warunki obiektowe nie mieszczą się w zakresie z W-H06 |
| W-H08 | POWINIEN | **I** | Sygnalizować przewidywany pozostały czas pracy na zasilaniu rezerwowym |
| W-H09 | MUSI | **I** | Osiągać gotowość operacyjną nie później niż **60 sekund** od załączenia zasilania oraz po zakończonej aktualizacji |

### Uzasadnienie wymagań W-H01 i W-H09

Wymaganie W-H01 określa minimalny czas podtrzymania zarówno w chwili odbioru, jak i na koniec
okresu gwarancji. Profil obciążenia przyjęty do obliczeń musi obejmować emisję, a nie wyłącznie
stan czuwania.

Wymaganie W-H09 ustanawia maksymalny czas przywrócenia gotowości operacyjnej po załączeniu
zasilania lub zakończeniu aktualizacji, aby ograniczyć ryzyko pominięcia polecenia w okresie
rozruchu urządzenia.

### Zakres odpowiedzialności za warunki obiektowe

Wytyczne **nie wchodzą w obszar warunków obiektowych**. Nie nakazują ogrzewania remizy, nie stawiają
wymagań budynkowi i nie rozstrzygają, kto ma za to zapłacić.

Urządzenie **deklaruje zakres, w którym pracuje** — i to jest wymaganie. Zapewnienie warunków
mieszczących się w tym zakresie, albo zamówienie wykonania o zakresie szerszym (W-H07), należy
do właściciela obiektu i projektanta instalacji. Przy odbiorze odnotowuje się zmierzoną temperaturę
pomieszczenia, ale jest to **zapis stanu**, a nie warunek dopuszczenia — protokół dokumentuje,
w jakich warunkach urządzenie postawiono, i tyle.

---

## I. Swoboda wyboru dostawcy

Urządzenie kupowane jest raz, a eksploatowane kilkanaście lat, w czasie których zmieni się operator
łączności, dostawca serwisu, a być może i system centralny. Wymagania z tej części chronią
właściciela przed sytuacją, w której każda taka zmiana wymaga zgody producenta.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-I01 | MUSI | **I** | Działać w pełnym zakresie funkcji alarmowania **bez połączenia z platformą producenta** |
| W-I02 | MUSI | **I** | Umożliwiać zmianę adresu punktu dostępu, kanału powiadomienia i punktu zaufania bez udziału producenta |
| W-I03 | MUSI | **I** | Umożliwiać wyłączenie i włączenie poszczególnych kanałów |
| W-I04 | MUSI | **I** | Umożliwiać wymianę karty abonenckiej bez utraty gwarancji i bez wizyty serwisu producenta |
| W-I05 | MUSI | **I** | Nie wymagać stałego abonamentu u producenta dla podstawowego alarmowania |
| W-I06 | MUSI | **I** | Nie stosować materiału kryptograficznego współdzielonego między urządzeniami |
| W-I07 | MUSI | **I** | Udostępniać procedurę wymiany i odwołania materiału kryptograficznego |
| W-I08 | MUSI | **I** | Dostarczyć dokumentację interfejsów elektrycznych, audio i integracyjnych **wraz ze schematem elektrycznym** w zakresie umożliwiającym samodzielny serwis |
| W-I09 | POWINIEN | **I** | Dostarczyć wykaz składników oprogramowania oraz zasady zgłaszania i usuwania podatności |
| W-I10 | POWINIEN | **I** | Wykazać w odbiorze możliwość przełączenia urządzenia na alternatywny punkt dostępu |
| W-I15 | MUSI | **D** | Dostarczyć **deklarację zgodności**, wykaz zastosowanych norm zharmonizowanych oraz sprawozdania z badań kompatybilności elektromagnetycznej, badań radiowych i badań bezpieczeństwa |
| W-I11 | MUSI | **P** | **Producent syreny** — udostępnić otwarty, udokumentowany interfejs sterowania: wykaz poleceń wraz ze składnią, mapę slotów, format i sposób wgrania plików dźwiękowych, kody odpowiedzi i błędów, sposób odczytu stanu oraz parametry elektryczne złącza |
| W-I12 | MUSI | **P** | **Producent syreny** — zrealizować ten interfejs na standardowej warstwie fizycznej: szeregowej, sieciowej, uniwersalnej albo na wejściach i wyjściach ogólnego przeznaczenia; złącza i protokoły autorskie bez opublikowanej specyfikacji nie spełniają wymagania |
| W-I13 | MUSI | **P** | **Producent syreny** — określić warunki licencyjne dopuszczające integrację przez podmiot trzeci, bez opłat za samo podłączenie i bez utraty gwarancji |
| W-I14 | MUSI | **P** | **Producent syreny** — udostępnić wejście liniowe audio oraz zwarciowe wejście nadawania, umożliwiające wysterowanie syreny w trybie audio niezależnie od jej interfejsu programowego |

Wymaganie W-I01 oznacza, że zakończenie działalności producenta albo wyłączenie jego usługi nie może
pozbawić instalacji zdolności alarmowania. Wszystkie elementy niezbędne do podstawowego działania
muszą znajdować się w urządzeniu i w dokumentacji przekazanej właścicielowi.

Wymaganie W-I15 dopisano po stwierdzeniu, że dokumentacja produktu odebranego w liczbie kilku
tysięcy sztuk zawierała **puste rubryki** w miejscach: dyrektywy, normy zharmonizowane, badania
kompatybilności elektromagnetycznej, badania radiowe i deklaracja zgodności. Formalnie niczego nie
naruszono, bo żadne wymaganie tych dokumentów nie żądało. Teraz żąda.

### Granica integracyjna między sterownikiem a syreną

Wymagania W-I11–W-I14 są skierowane do producenta syreny, a nie do producenta sterownika.
Interoperacyjność systemu centralnego nie jest wystarczająca, jeżeli granica między sterownikiem
a syreną pozostaje zamknięta.

Wiele syren ma wbudowany odtwarzacz, pamięć slotów i własną automatykę. Brak udokumentowanego
sposobu ich wywołania tworzy długotrwałą zależność od jednego dostawcy. Dokumentacja powinna być
wystarczająca do wykonania integracji przez niezależnego wykonawcę; sama deklaracja dostępności
interfejsu, bez specyfikacji protokołu, warunków licencyjnych i testu zgodności, nie jest
wystarczająca.

W postępowaniu zakupowym podstawowym mechanizmem egzekwowania tych wymagań wobec wykonawcy jest
umowa zawierana przez zamawiającego. Niniejszy projekt nie tworzy samodzielnie obowiązków po
stronie producenta syreny; dlatego wymagania te ujęto również w załączniku nr 11.

Wymaganie W-I14 jest zabezpieczeniem na wypadek, gdy pozostałe zawiodą. Nawet syrena o całkowicie
zamkniętym oprogramowaniu daje się podłączyć do SOiA, jeżeli ma wejście liniowe i wejście nadawania —
sterownik wykorzystuje ją wtedy po prostu jako system audio.

---

## J. Współistnienie z systemem istniejącym

Dołączenie kanału SOiA **nie może wyłączyć ani ograniczyć tego, co działa dzisiaj**. Zasada dotyczy
przede wszystkim instalacji istniejących, ale nie tylko ich — także nowa instalacja musi zachować
możliwość uruchomienia lokalnego, niezależną od jakiejkolwiek łączności.

Prace przy instalacji nie mogą powodować okresowej utraty zdolności alarmowania. W razie błędnej
konfiguracji, braku zasięgu albo awarii nowego kanału dotychczasowy tor powinien pozostać dostępny.
Uruchomienie lokalne musi być niezależne od dostępności sieci.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-J01 | MUSI | **I** | Nie wyłączać ani nie ograniczać dotychczasowych sposobów uruchomienia syreny — istniejącego systemu dyspozytorskiego, pulpitu lokalnego, przycisku ręcznego ani kanału radiowego |
| W-J02 | MUSI | **I** | Zachować możliwość **uruchomienia lokalnego**, działającego przy całkowitym braku łączności z SOiA |
| W-J03 | MUSI | **I** | Nie warunkować dołączenia kanału SOiA wyłączeniem, przeprogramowaniem ani utratą gwarancji istniejącego systemu |
| W-J04 | MUSI | **I** | Przy zbiegu poleceń wykonać do końca **wyłącznie to, które pierwsze rozpoczęło sekwencję**; polecenie odebrane w trakcie emisji odrzucić i odnotować, bez kolejkowania i bez drugiej emisji |
| W-J05 | MUSI | **I** | Zachować pierwszeństwo lokalnego odcięcia i trybu serwisowego **niezależnie od toru**, z którego przyszło polecenie |
| W-J06 | MUSI | **I** | Po dołączeniu kanału SOiA potwierdzić w odbiorze, że **dotychczasowy sposób uruchomienia nadal działa** |
| W-J07 | POWINIEN | **I** | Odnotowywać w rejestrze zdarzeń tor, z którego przyszło polecenie |
| W-J08 | MUSI | **I** | **Ponowić** polecenie odrzucone na podstawie W-J04 po zakończeniu bieżącej emisji, jeżeli jego okno rozpoczęcia pozostaje otwarte, i odnotować zarówno odroczenie, jak i ponowienie |

Wymaganie W-J04 ogranicza ryzyko automatycznego wykonania kolejnej emisji w trakcie trwania
poprzedniej. Zakolejkowanie dwóch niezależnych poleceń mogłoby utworzyć sześciominutową sekwencję
niezgodną ze strukturą sygnałów określoną w przepisach.

Wymaganie W-J08 dotyczy sytuacji, w której podczas emisji z toru istniejącego zostaje odebrane
odwołanie alarmu z SOiA. Materiał źródłowy określa takie polecenie jako odrzucone bez kolejkowania,
a jednocześnie nakazuje jego ponowienie po zakończeniu emisji, jeżeli okno pozostaje otwarte.

> [!caution] Wymaga decyzji przed akceptacją — W-J04 i W-J08
> Przed podpisaniem projektu należy jednoznacznie zdefiniować relację między odrzuceniem,
> odroczeniem, zakazem kolejkowania i ponowieniem polecenia w W-J04 oraz W-J08. Redakcja V2
> zachowuje brzmienie i intencję materiału źródłowego, ale nie rozstrzyga modelu wykonawczego.

Wymaganie W-J06 przenosi zasadę z deklaracji do odbioru. Bez sprawdzenia, że stary tor nadal działa,
zapis W-J01 pozostałby obietnicą.

---

## K. Zestaw instalacyjny

Wymagania z poprzednich części dotyczą **funkcji**. Ta część opisuje, co wchodzi w skład dostawy
i czego wymaga montaż — bo przedmiotem zamówienia bywa nie sam sterownik, tylko kompletny zestaw
gotowy do zamocowania na obiekcie. Nie opisuje natomiast **konstrukcji**: gabaryty, materiał
obudowy i rozmieszczenie podzespołów dobiera wykonawca.

### Topologia zestawu instalacyjnego

Zestaw pracuje zwykle w dwóch częściach, w różnych warunkach, i to rozdzielenie jest **celowe**.
Część wewnętrzna — sterownik wraz z zasilaniem buforowym i magazynem energii — pracuje
w pomieszczeniu zamkniętym. Część zewnętrzna — urządzenie radiowe wraz z antenami — pracuje
na elewacji albo na maszcie, w pełnej ekspozycji atmosferycznej. Pozwala to trzymać elektronikę
i akumulator w łagodnych warunkach, a na zewnątrz wystawiać wyłącznie urządzenie do tego
przeznaczone.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-K01 | MUSI | **D** | Być dostarczany jako **kompletny zestaw** gotowy do zamocowania: część wewnętrzna, część zewnętrzna, magazyn energii, komplet anten i akcesoria montażowe |
| W-K02 | MUSI | **D** | Zawierać **listę zawartości zestawu** umożliwiającą kontrolę kompletności dostawy przed montażem, z rozróżnieniem pozycji pakunkowych i elementów fabrycznie zabudowanych oraz z **procedurą postępowania przy stwierdzeniu niezgodności** |
| W-K03 | MUSI | **D** | Wskazywać w dokumentacji **elementy zapewniane przez instalatora** — okablowanie, puszki, dławnice, kotwy, konstrukcje wsporcze — żeby ich brak nie był mylony z niekompletnością dostawy |
| W-K04 | MUSI | **D** | Zapewnić części zewnętrznej stopień ochrony i zakres temperatur właściwy dla pracy na wolnym powietrzu, nie gorszy niż **IP67** oraz **−40 °C do +70 °C** |
| W-K05 | MUSI | **D** | Zapewnić łączność między częścią wewnętrzną a zewnętrzną przewodem sieciowym oraz zasilanie części zewnętrznej z części wewnętrznej |
| W-K20 | MUSI | **D** | Zawierać w zestawie **ochronniki przepięciowe** torów sygnałowego i zasilającego prowadzonych między częścią zewnętrzną a wewnętrzną |
| W-K21 | MUSI | **D** | Traktować część zewnętrzną jako element istotny dla bezpieczeństwa: podać sposób jej utwardzenia, ścieżkę aktualizacji jej oprogramowania, sposób uwierzytelnienia sterownika do jej interfejsów oraz sposób nadzoru jej zasilania |
| W-K22 | MUSI | **D** | Podać dopuszczalny **budżet napięciowy zasilania części zewnętrznej pod obciążeniem** oraz maksymalną długość trasy; wartość mierzy się przy odbiorze |
| W-K23 | MUSI | **D** | Zawierać w zestawie **fizyczny element uruchomienia lokalnego** wraz ze wskazaniem miejsca jego montażu |
| W-K24 | MUSI | **D** | Podać dla magazynu energii **datę produkcji i datę ostatniego ładowania odświeżającego**; napięcie mierzy się przed pierwszym uruchomieniem |
| W-K25 | MUSI | **D** | Zapewnić, że pierwsze załączenie **nie wyzwala zabezpieczenia obwodu obiektowego**, albo podać wymaganą charakterystykę tego zabezpieczenia |
| W-K26 | MUSI | **D** | Wskazać wymagane umiejscowienie anten części wewnętrznej i przewidzieć **zapis zmierzonej jakości toru radiowego** w dokumentacji odbiorowej |

### Przyłącza

Sposób, w jaki instalator podłącza się do urządzenia, decyduje o tym, czy instalację da się
później serwisować bez producenta.

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-K06 | MUSI | **D** | Udostępniać **oznaczoną, ponumerowaną listwę przyłączeniową** dla wszystkich sygnałów obiektowych: zasilania, wejść dwustanowych, wyjść, torów stykowych i toru audio |
| W-K07 | MUSI | **D** | Dołączać do dokumentacji **mapę listwy** wiążącą numer zacisku z sygnałem i z oznaczeniem barwnym złączki, wraz z wymogiem oznaczenia obu końców przewodu obiektowego przez instalatora |
| W-K08 | MUSI | **D** | Umożliwiać podłączenie bez lutowania i bez narzędzi specjalistycznych producenta |
| W-K09 | MUSI | **D** | Zapewnić dostęp do gniazda karty abonenckiej i do magazynu energii **bez demontażu urządzenia z uchwytu** |
| W-K10 | POWINIEN | **D** | Umożliwiać otwarcie obudowy bez kolizji z instalacją obiektową |

Wymaganie W-K07 jest tym, które w praktyce najbardziej się liczy. Mapa zacisków w dokumentacji
oznacza, że każdy elektryk z uprawnieniami podłączy instalację i każdy serwisant ją później
odczyta. Jej brak zamienia prostą czynność w zależność od jednej firmy. Wcześniejsza wersja żądała
oznaczenia barwnego **przewodu** — było to niewykonalne, bo przewody obiektowe dobiera instalator;
producent oznacza złączkę, instalator oba końce przewodu.

### Bezpieczeństwo elektryczne

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-K11 | MUSI | **D** | Być urządzeniem **I klasy ochronności** z obowiązkowym przewodem ochronnym, podłączanym przed przewodami roboczymi |
| W-K12 | MUSI | **D** | Zawierać wewnątrz obudowy **zabezpieczenie nadprądowe** obwodu zasilającego o charakterystyce dobranej do prądu udarowego i zdolności zwarciowej nie mniejszej niż **6 kA**, dostępne bez narzędzi specjalistycznych |
| W-K13 | MUSI | **D** | Zapewnić **fizyczną przegrodę albo osłonę** oddzielającą obwody sieciowe od obwodów niskiego napięcia na listwie przyłączeniowej, chroniącą przed dotykiem podczas prac serwisowych |
| W-K14 | MUSI | **D** | Wymagać indywidualnego zaizolowania żył niewykorzystanych w przewodach wielożyłowych |
| W-K15 | MUSI | **D** | Zawierać w dokumentacji **listę kontrolną przed pierwszym załączeniem**, obejmującą kontrolę mechaniczną i elektryczną |

Wymaganie W-K13 zaostrzono po stwierdzeniu, że zaciski z napięciem sieciowym i zaciski
niskonapięciowe potrafią leżeć na jednej listwie, bez żadnej przegrody. Serwisant podłączający tor
audio pracuje wtedy na tej samej listwie, na której jest faza.

### Instalacja

| ID | Moc | Klasa zdolności | Wymaganie |
|---|---|---|---|
| W-K16 | MUSI | **D** | Dołączać **instrukcję instalacji** obejmującą kolejność prac, dobór mocowania do rodzaju podłoża, montaż magazynu energii, montaż anten i uruchomienie |
| W-K17 | MUSI | **D** | Wskazywać wymagane **kwalifikacje personelu** — osobno dla prac przy napięciu sieciowym, dla kotwienia obudowy o znacznej masie i dla prac na wysokości — wraz z wykazem środków ochrony indywidualnej i warunkami przerwania pracy |
| W-K18 | MUSI | **D** | Przewidywać przy pierwszym załączeniu **sprawdzenie bezprzerwowego przejścia na zasilanie rezerwowe** i powrotu do zasilania sieciowego |
| W-K19 | POWINIEN | **D** | Zawierać wzór protokołu przekazania instalacji |

---

## Zestawienie liczbowe

| Część | Wymagań | z tego MUSI |
|---|---|---|
| A — weryfikacja polecenia | 17 | 15 |
| B — obszar działania | 8 | 7 |
| C — sygnały i komunikaty | 17 | 11 |
| D — kanały i łączność | 25 | 22 |
| E — wysterowanie syreny | 14 | 12 |
| F — platforma sterownika | 14 | 12 |
| G — tryby i diagnostyka | 13 | 11 |
| H — zasilanie i środowisko | 9 | 7 |
| I — swoboda wyboru dostawcy | 15 | 13 |
| J — współistnienie | 8 | 7 |
| K — zestaw instalacyjny | 26 | 24 |
| **Razem** | **166** | **141** |

Rozkład według klas zdolności: **I — 111**, **II — 7**, **III — 9**; znaki adresata: **D — 35**, **P — 4**.

W porównaniu z wersją 0.2 dodano osiemnaście wymagań: szesnaście na podstawie zestawienia
dotychczasowych zapisów z dokumentacją faktycznie dostarczonego produktu oraz dwa w związku
z określeniem granic rozmiaru polecenia. Dziewięć wymagań przeredagowano z powodu niewykonalności,
sprzeczności wewnętrznych lub możliwości ich formalnego spełnienia bez realizacji celu. Siedem
wymagań dostosowano do poziomu rozwiązań dostępnych na rynku.


---
