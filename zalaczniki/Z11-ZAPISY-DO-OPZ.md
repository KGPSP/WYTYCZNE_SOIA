---
tytuł: "Załącznik nr 11 — Wytyczne do opisu przedmiotu zamówienia"
dokument: "Podręcznik podłączania syren alarmowych i innych urządzeń do SOiA"
wersja: 0.4
data: 2026-08-23
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
źródło: "Wydzielono z PODRECZNIK_v2.md"
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 11 — Wytyczne do opisu przedmiotu zamówienia


## Zakres i sposób stosowania załącznika

> [!warning] Zakres zastosowania
> Załącznik nie stanowi kompletnego opisu przedmiotu zamówienia. Zawiera propozycję minimalnego
> zakresu funkcjonalnego, który zamawiający powinien zweryfikować, uszczegółowić i dostosować do
> potrzeb, przedmiotu oraz podstawy prawnej konkretnego postępowania.

> [!note] Trzy ścieżki przygotowania zamówienia
> Zamawiający wybiera najpierw jeden punkt wyjścia: nową instalację, integrację instalacji istniejącej albo zakup samej syreny. Następnie dobiera klasy zdolności oraz rozdziela wymagania wobec sterownika, syreny, montażu i odbioru. Załącznik nie jest gotowym OPZ — wymaga rozpoznania obiektu, dostosowania do postępowania oraz sprawdzenia aktualnego stanu prawnego opisanego w części VII.

W konkretnym postępowaniu podstawowym mechanizmem egzekwowania wymagań wobec wykonawcy jest ich
ujęcie w dokumentach zamówienia i umowie. Sam projekt Wytycznych nie ustanawia obowiązków po
stronie producenta sterownika ani producenta syreny.

Każdy zapis odsyła do identyfikatora wymagania z załącznika nr 3, co umożliwia jego jednoznaczne
wyjaśnienie i sprawdzenie przy odbiorze. Zmiana wymagań oznaczonych jako bezwzględne wymaga oceny
wpływu na zgodność urządzenia z SOiA i nie powinna wynikać wyłącznie ze skrócenia dokumentacji.

### Określenie wymaganych klas zdolności

Przed wyborem poszczególnych zapisów zamawiający określa wymagany zakres funkcjonalny:

| Klasa lub symbol | Warunek stosowania |
|---|---|
| **I — rdzeń** | zawsze, bez wyjątku; to jest cała zgodność z systemem |
| **II — tor audio** | gdy sterownik ma sam odtwarzać dźwięk — przy modernizacji instalacji istniejących i wszędzie, gdzie syrena pracuje jako nagłośnienie |
| **III — profil głosowy** | tylko gdy urządzenie ma wypowiadać treść słowną; podnosi wymagania sprzętowe i cenę |
| **D — dostawa i montaż** | symbol zakresu, stosowany, gdy przedmiotem zamówienia jest kompletny zestaw, a nie sam sterownik |

Sterowanie syreną cyfrową przez jej udokumentowany interfejs wymaga klasy I. Modernizacja, w której
sterownik odtwarza dźwięk, wymaga klas I i II. Klasa III dotyczy zdolności opcjonalnej; system
centralny nie przenosi obecnie treści głosowej.

**Wymagania kierowane do producenta syreny** — otwarty interfejs sterowania, standardowa warstwa
fizyczna, warunki licencyjne dopuszczające integrację przez podmiot trzeci oraz wejście liniowe
i wejście nadawania — należą do **zamówienia na syrenę**, nie na sterownik. Zamawiający, który
kupuje jedno i drugie w jednym postępowaniu, powinien je rozdzielić w opisie.

Rozdziały 1–3 zawierają propozycje zależne od przedmiotu zamówienia. Rozdział 4 obejmuje wymagania
horyzontalne dotyczące swobody wyboru dostawcy. Rozdział 5 wskazuje postanowienia, które mogą
powodować nieuzasadnione ograniczenie interoperacyjności lub konkurencji.

---

## 1. Nowa instalacja

### 1.1. Zgodność z systemem

> Dostarczone urządzenie musi odbierać i wykonywać polecenia wykonawcze systemu ostrzegania
> i alarmowania (SOiA) na poziomie otwartym, to jest przez pobieranie podpisanego wykazu poleceń
> z publicznego punktu dostępu, bez konieczności rejestracji urządzenia.
> *(W-D01, W-D05)*

> Przed uruchomieniem sygnału urządzenie musi łącznie potwierdzić: poprawność podpisu odebranej
> treści i zgodność identyfikatora klucza, zgodność profilu i wersji słowników, aktualność treści,
> zgodność klasy urządzenia, objęcie obszaru urządzenia obszarem polecenia zgodnie z regułą
> zawierania, mieszczenie się w oknie rozpoczęcia oraz brak wcześniejszego wykonania tego samego
> polecenia. Niespełnienie któregokolwiek warunku oznacza niewykonanie polecenia.
> *(W-A01…W-A12)*

> Ochrona przed powtórnym wykonaniem polecenia musi przetrwać zanik zasilania i restart urządzenia.
> *(W-A10, W-A11)*

### 1.2. Obszar

> Obszar działania urządzenia konfiguruje się wyłącznie siedmiocyfrowymi kodami gmin. Urządzenie
> musi odrzucić albo zgłosić jako błąd konfigurację kodem dwucyfrowym lub czterocyfrowym oraz
> odrzucić kod sześciocyfrowy jako niepełny. Cyfra rodzaju gminy jest znacząca.
> *(W-B01…W-B07)*

### 1.3. Sygnały

> Urządzenie musi być zdolne wyemitować wszystkie cztery sygnały akustyczne określone
> w rozporządzeniu Ministra Spraw Wewnętrznych i Administracji z dnia 14 maja 2025 r. w sprawie
> alarmów i komunikatów ostrzegawczych, z wykorzystaniem plików referencyjnych zatwierdzonych przez
> Komendę Główną Państwowej Straży Pożarnej, z zachowaniem czasu trwania w tolerancji ±5 %
> oraz struktury czasowej sygnału. Wymóg utrzymania poziomu w granicach ±3 dB względem wzorca,
> w zadeklarowanym punkcie pomiarowym, dotyczy urządzeń klasy II.
> *(W-C01…W-C07)*

> Urządzenie musi potwierdzić zgodność sumy kontrolnej pliku przed jego instalacją oraz odrzucić kod
> sygnału, którego nie zna, bez przerywania obsługi pozostałych poleceń.
> *(W-C03, W-A08)*

### 1.4. Kanały i łączność

> Urządzenie musi umożliwiać podłączenie do sieci lokalnej obiektu przewodowo, bez modemu i bez
> karty abonenckiej, oraz obsługiwać co najmniej cztery niezależne, zarządzalne tory sieciowe
> przewodowe.
> *(W-D06, W-D07)*

> Urządzenie musi posiadać odrębny interfejs stacji radiowej — port sieciowy albo szeregowy — przeznaczony
> do podłączenia stacji dyspozytorskiej jako źródła polecenia, niezależny od toru audio
> i od sterowania nadawaniem.
> *(W-D09)*

> Urządzenie musi posiadać moduł komunikacji komórkowej bez blokady operatorskiej karty
> abonenckiej, z gniazdem karty dostępnym serwisowo bez demontażu urządzenia z uchwytu.
> *(W-D11, W-D21)*

> Urządzenie musi stosować hasło sterujące unikalne dla egzemplarza; hasło wspólne dla wielu
> urządzeń jest niedopuszczalne. Odrzucenie polecenia tekstowego — z nieznanego numeru, z błędnym
> hasłem albo spoza mapy poleceń — musi być rejestrowane i sygnalizowane.
> *(W-D18, W-D19)*

*Zalecane dodatkowo:* obsługa karty klasy przemysłowej — o rozszerzonym zakresie temperatur pracy
i podwyższonej wytrzymałości zapisu — oraz karty zdalnie prowizjonowanej, umożliwiającej zmianę
operatora bez wymiany karty *(W-D22, W-D23)*. Przy większych wdrożeniach warto
policzyć koszt pominięcia: jest to koszt jednego wyjazdu serwisowego pomnożony przez liczbę
zainstalowanych urządzeń.

### 1.5. Wysterowanie syreny

> Urządzenie musi zapewniać co najmniej dwa niezależne sposoby wysterowania syreny: wyjście audio
> liniowe oraz co najmniej sześć niezależnych, bezpotencjałowych wyjść przekaźnikowych w układzie
> NO/NC/COM, w tym co najmniej jedno do obwodu 230 V z izolacją galwaniczną nie mniejszą niż 4 kV
> oraz co najmniej jedno realizujące niezależne sterowanie nadawaniem.
> *(W-E01…W-E05)*

> Urządzenie musi posiadać lokalne, sprzętowe odcięcie toru wykonawczego, niezależne od łączności
> i od oprogramowania, mające pierwszeństwo przed poleceniem zdalnym, oraz nie może samoczynnie
> wznawiać przerwanej emisji po niekontrolowanym restarcie.
> *(W-E08, W-E09)*

### 1.6. Zasilanie i warunki pracy

> Zestaw jako całość musi zachować ciągłość pracy przez co najmniej 10 godzin od zaniku zasilania
> sieciowego, z określonym modelem degradacji magazynu energii i wynikającym z niego czasem
> podtrzymania na koniec okresu gwarancji.
> *(W-H01, W-H02)*

> Po powrocie zasilania urządzenie musi odtworzyć stan trwały i nie wykonywać polecenia, którego
> okno rozpoczęcia już minęło.
> *(W-H05)*

### 1.7. Zestaw, przyłącza i montaż

> Przedmiotem dostawy jest kompletny zestaw gotowy do zamocowania, obejmujący część wewnętrzną,
> część zewnętrzną, magazyn energii, komplet anten i akcesoria montażowe, wraz z listą zawartości
> umożliwiającą kontrolę kompletności przed montażem oraz jawnym wskazaniem elementów zapewnianych
> przez instalatora.
> *(W-K01, W-K02, W-K03)*

> Część zewnętrzna zestawu musi posiadać stopień ochrony nie gorszy niż IP67 i zakres temperatur
> pracy co najmniej od −40 °C do +70 °C.
> *(W-K04)*

> Urządzenie musi udostępniać oznaczoną, ponumerowaną listwę przyłączeniową dla wszystkich sygnałów
> obiektowych, wraz z dołączoną do dokumentacji mapą wiążącą numer zacisku z sygnałem i oznaczeniem
> barwnym złączki, wraz z wymogiem oznaczenia obu końców przewodu. Podłączenie nie może wymagać
> narzędzi specjalistycznych producenta.
> *(W-K06, W-K07, W-K08)*

> Urządzenie musi być urządzeniem I klasy ochronności z obowiązkowym przewodem ochronnym, zawierać
> zabezpieczenie nadprądowe wewnątrz obudowy oraz fizyczną izolację obwodów sieciowych chroniącą
> przed dotykiem podczas prac serwisowych.
> *(W-K11, W-K12, W-K13)*

> Wykonawca dostarczy instrukcję instalacji obejmującą kolejność prac, dobór mocowania do rodzaju
> podłoża, montaż magazynu energii i anten, listę kontrolną przed pierwszym załączeniem oraz
> wymagane kwalifikacje personelu — osobno dla prac przy napięciu sieciowym, kotwienia obudowy
> o znacznej masie i prac na wysokości.
> *(W-K15, W-K16, W-K17)*

> Uruchomienie obejmuje sprawdzenie bezprzerwowego przejścia na zasilanie rezerwowe i powrotu
> do zasilania sieciowego.
> *(W-K18)*

**Warunek obiektowy do sprawdzenia przed zamówieniem.** Część wewnętrzna zestawu pracuje
w pomieszczeniu o stabilnej temperaturze. Zamawiający powinien **sprawdzić, czy pomieszczenie
przewidziane pod montaż utrzymuje zakres deklarowany przez producenta** — nieogrzewana remiza
zimą schodzi poniżej progu. Jeżeli nie utrzymuje, do wyboru są dwie drogi: zapewnienie ogrzewania
albo postawienie wymagania rozszerzonego zakresu temperatur.

*Do rozważenia przy lokalizacjach nieogrzewanych i nieklimatyzowanych:* rozszerzony zakres
temperatur pracy, co najmniej od −20 °C do +55 °C. Standardowo dostarczane zestawy deklarują zakres
węższy, właściwy dla pomieszczeń o stabilnej temperaturze — jeżeli remiza albo obiekt takiej
temperatury nie zapewnia, wymaganie trzeba postawić wprost *(W-H06, W-H07)*.

---

## 2. Integracja kanału SOiA z instalacją istniejącą

Wariant zachowujący dotychczasowy system sterowania i dodający kanał SOiA jako tor równoległy.

> Przedmiotem zamówienia jest dołączenie kanału systemu ostrzegania i alarmowania (SOiA)
> do istniejącej instalacji syreny, z zachowaniem dotychczasowego sposobu sterowania.

> Dołączenie może zostać zrealizowane przez wykorzystanie udokumentowanego interfejsu sterowania
> istniejącej syreny albo przez podanie sygnału liniowego na jej wejście audio z jednoczesnym
> sterowaniem nadawaniem. Wykonawca wskazuje zastosowany tryb w projekcie wykonawczym.
> *(W-E10, załącznik nr 5)*

> Dołączenie kanału nie zmniejsza zakresu sprawdzeń wykonywanych przed uruchomieniem sygnału.
> Weryfikacja podpisu, reguła obszaru, okno rozpoczęcia, ochrona przed powtórzeniem oraz lokalne
> odcięcie awaryjne obowiązują w pełnym zakresie.
> *(załącznik nr 3, części A, B, E)*

> Dołączenie kanału SOiA nie może wyłączyć ani ograniczyć dotychczasowych sposobów uruchomienia
> syreny — istniejącego systemu dyspozytorskiego, pulpitu lokalnego, przycisku ręcznego ani kanału
> radiowego. Wykonawca nie może warunkować realizacji przedmiotu zamówienia wyłączeniem,
> przeprogramowaniem ani ograniczeniem istniejącego systemu, ani uzależniać od tego gwarancji
> i serwisu. Oba tory pracują równolegle.
> *(W-J01, W-J03)*

> Instalacja musi zachować możliwość uruchomienia lokalnego, działającego przy całkowitym braku
> łączności z systemem.
> *(W-J02)*

> Przy zbiegu poleceń z dwóch torów wykonaniu podlega wyłącznie polecenie, które pierwsze rozpoczęło
> sekwencję. Polecenie odebrane w trakcie emisji podlega odrzuceniu i odnotowaniu, bez kolejkowania
> i bez powodowania kolejnej emisji. Odrzucenie ma charakter odroczenia, a nie usunięcia polecenia:
> urządzenie ponawia je po zakończeniu bieżącej emisji, jeżeli jego okno rozpoczęcia pozostaje
> otwarte.
> *(W-J04, W-J08)*

> Odbiór obejmuje potwierdzenie, że po dołączeniu kanału SOiA dotychczasowy sposób uruchomienia
> syreny nadal działa.
> *(W-J06)*

> [!note] Ocena wariantu audio
> Jeżeli producent zainstalowanej syreny nie udostępnia dokumentacji interfejsu sterowania, należy
> przeanalizować wariant audio. Jego zastosowanie wymaga potwierdzenia zgodności z dokumentacją,
> bezpieczeństwem technicznym, warunkami gwarancji, licencjami i postanowieniami umowy.

---

## 3. Zakup syreny

Zapisy kierowane do producenta syreny, nie sterownika.

> Dostarczona syrena musi posiadać otwarty, udokumentowany interfejs sterowania, obejmujący wykaz
> poleceń wraz ze składnią, mapę slotów dźwiękowych, format i sposób wgrania plików, kody odpowiedzi
> i błędów, sposób odczytu stanu oraz parametry elektryczne złącza. Dokumentacja musi być
> wystarczająca do samodzielnego wykonania integracji przez podmiot trzeci, bez udziału producenta.
> *(W-I11)*

> Interfejs musi być zrealizowany na standardowej warstwie fizycznej: port sieciowy, szeregowy albo złącze uniwersalne.
> *(W-I12)*

> Warunki licencyjne muszą dopuszczać integrację przez podmiot trzeci, bez opłat za samo podłączenie
> i bez utraty gwarancji.
> *(W-I13)*

> Syrena musi udostępniać wejście liniowe audio oraz zwarciowe wejście nadawania, umożliwiające jej
> wysterowanie niezależnie od interfejsu programowego producenta.
> *(W-I14)*

Wymaganie dotyczące wejścia liniowego i wejścia nadawania stanowi niezależny wariant integracyjny
i powinno być rozważane również wtedy, gdy producent deklaruje dostępność interfejsu programowego.

---

## 4. Wymagania zapewniające swobodę wyboru dostawcy

> Urządzenie musi działać w pełnym zakresie funkcji alarmowania bez połączenia z platformą
> producenta. Podstawowe alarmowanie nie może wymagać abonamentu ani usługi świadczonej przez
> producenta.
> *(W-I01, W-I05)*

> Zamawiający musi mieć możliwość zmiany adresu punktu dostępu, kanału powiadomienia i punktu
> zaufania, wyłączenia i włączenia poszczególnych kanałów oraz wymiany karty abonenckiej — bez
> udziału producenta, bez utraty gwarancji i bez ponownej licencji.
> *(W-I02, W-I03, W-I04)*

> Materiał kryptograficzny nie może być współdzielony między urządzeniami. Wykonawca dostarczy
> procedurę wymiany i odwołania materiału kryptograficznego.
> *(W-I06, W-I07)*

> Wykonawca dostarczy dokumentację interfejsów elektrycznych, audio i integracyjnych w zakresie
> umożliwiającym samodzielny serwis, a także umożliwi eksport pełnej konfiguracji i dziennika
> zdarzeń w formacie otwartym, możliwym do odczytu bez oprogramowania producenta.
> *(W-I08, W-G06, W-G09)*

> W ramach odbioru wykonawca wykaże możliwość przełączenia urządzenia na alternatywny punkt dostępu.
> *(W-I10)*

---

## 5. Postanowienia niezalecane w opisie przedmiotu zamówienia

Poniższe zestawienie wskazuje rodzaje postanowień, które mogą prowadzić do nieuzasadnionej
zależności od dostawcy albo utrudniać odbiór. Ich zastosowanie należy każdorazowo ocenić w świetle
przedmiotu zamówienia i przepisów o zamówieniach publicznych.

| Ryzykowne postanowienie lub brak | Zalecany sposób ujęcia |
|---|---|
| wymaganie konkretnego systemu dyspozytorskiego albo „kompatybilności z systemem X” | opisać wymagane funkcje, interfejsy i zgodność z SOiA oraz dopuścić rozwiązania równoważne zgodnie z właściwymi przepisami |
| zakup odrębnego „pakietu dźwięków alarmowych” | wymagać instalacji właściwych plików referencyjnych i potwierdzenia ich sum kontrolnych |
| ujęcie łączności bez sprawdzenia świadczeń zapewnianych centralnie | zweryfikować stan organizacyjny na dzień wszczęcia postępowania i wymagać możliwości późniejszej zmiany karty oraz konfiguracji bez wymiany sprzętu |
| uzależnienie podstawowego alarmowania od platformy producenta | wymagać pełnego działania podstawowych funkcji bez połączenia z usługą producenta |
| ogólna deklaracja „interfejs dostępny dla partnerów” | wymagać opublikowanej specyfikacji protokołu, warunków licencyjnych i sprawdzalnego testu zgodności |
| brak zasobów dla funkcji objętych zamówieniem i przewidywanego okresu eksploatacji | określić zasoby odpowiednio do zamówionych klas zdolności, planowanych rozszerzeń i okresu wsparcia |
| wyłączenie dotychczasowego systemu jako warunek dołączenia SOiA | wymagać równoległej pracy torów oraz sprawdzenia zachowania istniejących sposobów uruchomienia |
| brak kryteriów odbioru odpowiadających wymaganiom | przypisać wymaganiom konkretne scenariusze sprawdzeń i wynik oczekiwany zgodnie z załącznikiem nr 10 |

---

## 6. Proponowane postanowienia umowne dotyczące odbioru

> Odbiór instalacji następuje po wykonaniu i udokumentowaniu sprawdzeń określonych w załączniku
> nr 10 do Wytycznych Komendanta Głównego Państwowej Straży Pożarnej w sprawie podłączania syren
> alarmowych do SOiA, potwierdzonych protokołem odbioru oraz wypełnioną kartą konfiguracji
> urządzenia.

> Instalacja, która uruchamia sygnał mimo niespełnienia warunków weryfikacji — w szczególności poza
> własnym obszarem, poza oknem rozpoczęcia albo przy niepoprawnym podpisie — nie podlega odbiorowi
> do czasu usunięcia przyczyny.

Drugie postanowienie wymaga od wykonawcy wykazania poprawności implementacji w zakresie warunków
bezpiecznego wykonania polecenia.


---
