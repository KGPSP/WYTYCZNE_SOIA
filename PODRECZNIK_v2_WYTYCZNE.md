---
tytuł: "Wytyczne Komendanta Głównego PSP do SOiA"
wersja: 0.4
data: 2026-08-23
status: W TRAKCIE AKCEPTACJI
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
wariant_redakcyjny: v2-wytyczne
źródło: "Wydzielono z PODRECZNIK_v2.md"
---

# Wytyczne Komendanta Głównego Państwowej Straży Pożarnej

Poniżej przedstawiono **projekt części normatywnej**. Do czasu podpisania dokument nie obowiązuje.
Dalsza treść obejmuje załączniki ułożone według kolejności zalecanej do lektury, przy zachowaniu
numeracji wynikającej z odwołań zawartych w projekcie Wytycznych.


<div align="center">

**PROJEKT — DOKUMENT NIEPODPISANY**

**WYTYCZNE**

**Komendanta Głównego Państwowej Straży Pożarnej**

z dnia ………………… 2026 r.

**w sprawie podłączania syren alarmowych i innych urządzeń
do systemu ostrzegania i alarmowania (SOiA)**

</div>

*Projekt Wytycznych opracowano w oparciu o przepisy ustawy z dnia 5 grudnia 2024 r. o ochronie ludności
i obronie cywilnej (Dz. U. poz. 1907, z późn. zm.) oraz rozporządzenia Ministra Spraw Wewnętrznych
i Administracji z dnia 14 maja 2025 r. w sprawie alarmów i komunikatów ostrzegawczych
(Dz. U. poz. 645). Zgodnie z założeniem projektu dokument ma uzupełniać Wytyczne Komendanta Głównego
Państwowej Straży Pożarnej z dnia 28 maja 2025 r. w sprawie przygotowania, dystrybucji oraz
eksploatacji cyfrowych sygnałów alarmowych syren, bez ich uchylania ani zmiany.*

---

### § 1. Zasada interoperacyjności urządzeń i rozdzielenia ról

1. Rolą producenta jest dostarczenie syreny lub innego urządzenia sygnalizacyjnego zdolnego
   do współpracy z SOiA, natomiast rolą państwa jest prowadzenie systemu ostrzegania
   i alarmowania ludności.

2. Urządzenia różnych producentów podłącza się do SOiA według jednolitych zasad, a to samo
   polecenie powinno wywoływać na nich równoważne działanie. Zamówienie powinno dotyczyć urządzenia
   interoperacyjnego, a nie zamkniętego środowiska jednego dostawcy.

3. Wymagania określone w Wytycznych i załącznikach interpretuje się zgodnie z zasadą wyrażoną
   w ust. 1 i 2. Rozwiązanie powodujące, że urządzenie jednego producenta zachowuje się wobec tego
   samego polecenia inaczej niż urządzenie innego producenta, jest niezgodne z Wytycznymi.

### § 2. Charakter Wytycznych i zakres przedmiotowy

1. **Stosowanie Wytycznych jest dobrowolne.** Nie nakładają one na kogokolwiek obowiązku
   przyłączenia urządzenia do SOiA.

2. **Podmiot, który przyłącza urządzenie do SOiA, stosuje Wytyczne w całości.** Wymagania oznaczone
   słowem „MUSI” stanowią **warunek poprawnego działania urządzenia w systemie**, a nie obowiązek
   nałożony na podmiot. Częściowe spełnienie tych wymagań może prowadzić do niespójnego czasu lub
   sposobu wykonania polecenia przez urządzenia objęte tym samym alarmem.

3. **Momentem przystąpienia jest zgłoszenie urządzenia do rejestracji.** Do tej chwili urządzenie
   pobierające publiczny wykaz poleceń jest odbiorcą informacji udostępnianej powszechnie
   i Wytyczne go nie dotyczą. Kto uruchamia syrenę na podstawie polecenia z SOiA bez rejestracji,
   czyni to na własną odpowiedzialność i poza systemem.

4. Rejestracja przeznaczona jest dla **podmiotów publicznych** — jednostek samorządu terytorialnego,
   wojewodów oraz jednostek organizacyjnych Państwowej Straży Pożarnej. Dostęp do publicznego
   wykazu poleceń pozostaje otwarty dla wszystkich, na zasadach określonych w § 5 ust. 3.

5. **SOiA służy ostrzeganiu i alarmowaniu ludności.** Wywoływanie jednostek ochrony przeciwpożarowej
   nie należy do obecnego zakresu systemu; dotychczasowe sposoby ich alarmowania pozostają
   niezmienione i nie podlegają niniejszym Wytycznym.

6. Wytyczne określają zasady:
   1) podłączania syren alarmowych i innych urządzeń sygnalizacyjnych do SOiA;
   2) weryfikacji poleceń wykonawczych przez urządzenie przed uruchomieniem sygnału;
   3) rejestracji urządzeń i dopuszczania ich do kanałów zamkniętych;
   4) odbioru instalacji oraz postępowania w przypadku stwierdzenia niezgodności.

7. Wytyczne **nie regulują** parametrów akustycznych syreny, doboru głośników, zasięgu ani projektu
   instalacji nagłośnieniowej. Zagadnienia te pozostają w gestii projektanta i zamawiającego.

8. Wytyczne nie zmieniają właściwości organów ochrony ludności w zakresie ogłaszania i odwoływania
   alarmów.

### § 3. Definicje

Znaczenie pojęć użytych w Wytycznych określa **załącznik nr 1 — Słownik pojęć**. W szczególności
rozróżnienia między poleceniem a alarmem, między **zatrzymaniem** emisji a jej **odcięciem**, między
emisją a jej zakończeniem oraz między odwołaniem akcji nierozpoczętej a odwołaniem alarmu są wiążące
dla wszystkich dokumentów i postępowań prowadzonych na podstawie niniejszych Wytycznych.

### § 4. Załączniki i materiały referencyjne

1. Integralnymi elementami Wytycznych są załączniki wymienione w § 14.

2. Aktualne wartości techniczne — adresy punktów dostępu, wersje słowników oraz identyfikator klucza
   podpisującego — publikowane są maszynowo pod adresem produkcyjnym SOiA i to one stanowią
   **źródło autorytatywne**. Wartości przytoczone w załącznikach mają charakter informacyjny
   i podlegają potwierdzeniu przed wdrożeniem.

3. **Pliki referencyjne sygnałów nie są przenoszone przez system.** Udostępnia się je do pobrania
   na stronie SOiA. Źródłem rozstrzygającym dla ich sum kontrolnych są Wytyczne z dnia 28 maja
   2025 r., a nie strona, z której plik pobrano.

### § 5. Poziomy podłączenia

1. Ustala się trzy poziomy podłączenia urządzenia do SOiA:
   1) **poziom 0** — pobieranie podpisanego wykazu poleceń z publicznego punktu dostępu,
      bez rejestracji urządzenia;
   2) **poziom 1** — poziom 0 uzupełniony o kanał niezwłocznego powiadomienia oraz indywidualną
      tożsamość kryptograficzną urządzenia;
   3) **poziom 2** — poziom 1 uzupełniony o pracę w wydzielonej sieci operatora oraz kanał
      wiadomości tekstowych.

2. Poziomy są **kumulatywne**. Poziom wyższy dokłada kanał i nie zwalnia z obowiązków poziomu
   niższego; w szczególności cykliczne pobieranie wykazu poleceń pozostaje obowiązkowe niezależnie
   od dostępności pozostałych kanałów.

3. Poziom 0 jest **otwarty**. Prawo do pobierania i wykorzystania publicznego wykazu poleceń nie
   jest uzależnione od rejestracji, przynależności organizacyjnej ani formy prawnej podmiotu.

4. Podłączenie na poziomie 0 nie wymaga zgody ani powiadomienia Komendy Głównej Państwowej Straży
   Pożarnej. Dopuszczenie do poziomu 1 albo 2 jest natomiast decyzją, o której mowa w § 8.

### § 6. Wymagania dla urządzenia

1. Urządzenie podłączane do SOiA MUSI, przed uruchomieniem sygnału, potwierdzić łącznie:
   1) poprawność podpisu odebranej treści oraz zgodność identyfikatora klucza;
   2) zgodność profilu, środowiska i wersji słowników;
   3) aktualność treści, to jest nieprzekroczenie terminu jej ważności;
   4) zgodność klasy urządzenia z klasą wskazaną w poleceniu;
   5) objęcie obszaru urządzenia przez obszar wskazany w poleceniu, zgodnie z regułą zawierania;
   6) mieszczenie się chwili bieżącej w oknie rozpoczęcia;
   7) brak wcześniejszego wykonania tego samego polecenia;
   8) dopuszczalność emisji według stanu technicznego i trybu pracy urządzenia.

2. Niespełnienie któregokolwiek z warunków, o których mowa w ust. 1, oznacza **niewykonanie
   polecenia**. Zasada ta obowiązuje bez wyjątków i bez interpretacji rozszerzającej.

3. Obszar działania urządzenia konfiguruje się wyłącznie **siedmiocyfrowymi kodami gmin**.
   Konfiguracja kodem województwa lub powiatu jest niedopuszczalna; urządzenie MUSI ją odrzucić
   albo zgłosić jako błąd konfiguracji.

4. Rozpoczęta sekwencja sygnału **wykonuje się do końca**. Polecenie zatrzymania emisji nie istnieje
   i nie jest przenoszone przez żaden kanał. Urządzenie MUSI natomiast być wyposażone w **lokalne
   odcięcie** toru wykonawczego — czynność na obiekcie, niezależną od łączności i od oprogramowania,
   mającą pierwszeństwo przed poleceniem zdalnym.

5. **Dołączenie kanału SOiA nie może wyłączyć ani ograniczyć dotychczasowych sposobów uruchomienia
   syreny** — istniejącego systemu sterowania, pulpitu lokalnego, przycisku ręcznego ani kanału
   radiowego. Kanały działają równolegle. Niedopuszczalne jest warunkowanie podłączenia urządzenia
   wyłączeniem, przeprogramowaniem albo ograniczeniem systemu istniejącego, jak również uzależnianie
   od tego gwarancji lub serwisu.

6. Przy zbiegu poleceń pochodzących z różnych kanałów wykonaniu podlega polecenie, które jako
   pierwsze rozpoczęło sekwencję sygnału. Polecenie odebrane w trakcie emisji podlega odrzuceniu
   i odnotowaniu. Odrzucenie ma charakter odroczenia, a nie usunięcia polecenia: urządzenie ponawia
   polecenie po zakończeniu bieżącej emisji, dopóki jego okno rozpoczęcia pozostaje otwarte.

7. Wymagania dzielą się na **klasy zdolności**:
   1) **klasa I — rdzeń**: obowiązuje każde urządzenie przyłączane do SOiA, niezależnie
      od konstrukcji i sposobu sprzężenia z syreną;
   2) **klasa II — tor audio**: obowiązuje urządzenie, które **samo odtwarza dźwięk**; nie dotyczy
      urządzenia sterującego syreną cyfrową przez jej własny interfejs;
   3) **klasa III — profil głosowy**: stosowana wyłącznie wtedy, gdy urządzenie ma wypowiadać treść
      słowną.

   Zamawiający wskazuje w opisie przedmiotu zamówienia klasy, których wymaga. Klasa I jest
   niezbywalna; pominięcie klasy II albo III oznacza, że urządzenie nie będzie tych funkcji pełniło.

8. Szczegółowy zakres wymagań, wraz z przypisaniem każdego z nich do klasy zdolności oraz z wymaganiami
   dotyczącymi zasilania, trybów pracy, diagnostyki, rejestru zdarzeń, źródła czasu, współistnienia
   z systemem istniejącym i swobody wyboru dostawcy, określa **załącznik nr 3**.

### § 7. Sygnały akustyczne

1. Urządzenie podłączane do SOiA MUSI być zdolne do wyemitowania **wszystkich** sygnałów
   akustycznych określonych w załączniku do rozporządzenia, o którym mowa w preambule,
   z wykorzystaniem plików referencyjnych zatwierdzonych przez Komendę Główną Państwowej Straży
   Pożarnej.

2. Zdolność, o której mowa w ust. 1, jest **właściwością konstrukcyjną urządzenia**, a nie zakresem
   usługi świadczonej przez system. Zakres sygnałów wyzwalanych centralnie jest węższy, wynika
   z aktualnej wersji słownika publikowanej pod adresem produkcyjnym i obejmuje obecnie wyłącznie
   sygnały skierowane do ludności. Wymóg z ust. 1 wynika z tego, że urządzenie stoi w terenie
   kilkanaście lat, a katalog sygnałów będzie się rozszerzał.

3. Pliki referencyjne wraz z sumami kontrolnymi udostępniane są:
   1) w trybie określonym w § 4 Wytycznych z dnia 28 maja 2025 r. — podmiotom tam wskazanym;
   2) publicznie, do pobrania ze strony SOiA — wszystkim pozostałym.

4. Przed instalacją pliku urządzenie albo instalator MUSI potwierdzić zgodność jego sumy kontrolnej
   **z wartością podaną w Wytycznych z dnia 28 maja 2025 r.** Wymóg § 4 ust. 3 tych Wytycznych
   pozostaje w mocy. Zgodność potwierdza się podpisem w karcie konfiguracji.

5. Odwołanie alarmu jest **sygnałem akustycznym**, a nie zaprzestaniem emisji. Zakończenie emisji
   następuje samoistnie po upływie czasu właściwego dla danego sygnału.

6. Katalog sygnałów, ich powiązanie z plikami referencyjnymi oraz kodami stosowanymi w kanałach
   SOiA określa **załącznik nr 4**.

### § 8. Rejestracja urządzeń

1. Podmiot publiczny ubiegający się o podłączenie urządzenia na poziomie 1 albo 2 składa zgłoszenie
   w postaci formularza udostępnionego przez Komendę Główną Państwowej Straży Pożarnej. Jednostce
   samorządu terytorialnego zakłada się **profil**, w którym rejestruje ona własne urządzenia.

2. O dopuszczeniu **każdego urządzenia z osobna** rozstrzyga administrator SOiA. Złożenie zgłoszenia
   nie tworzy uprawnienia do dostępu do kanałów poziomu 1 i 2. Profil porządkuje wnioski, lecz nie
   zastępuje decyzji.

3. Dopuszczenie obejmuje nadanie urządzeniu indywidualnej tożsamości kryptograficznej oraz —
   w przypadku poziomu 2 — przydział karty abonenckiej i numeru.

4. Rejestracja **nie jest warunkiem działania urządzenia**. Instalacja wykonuje polecenia
   na poziomie 0 od chwili uruchomienia, również w okresie oczekiwania na rozstrzygnięcie.

5. Tożsamość kryptograficzna jest indywidualna dla urządzenia. Współdzielenie jednej tożsamości
   przez większą liczbę urządzeń jest niedopuszczalne. Klucz podpisujący treść wydawaną przez system
   jest natomiast **jeden** i pozostaje po stronie Komendy Głównej Państwowej Straży Pożarnej.

6. Tryb postępowania, stany rejestracji oraz zasady zawieszenia i odwołania dopuszczenia określa
   **załącznik nr 7**.

### § 9. Łączność i synchronizacja czasu

1. Karty abonenckie dla urządzeń jednostek samorządu terytorialnego zapewnia docelowo Komenda
   Główna Państwowej Straży Pożarnej. Łączność nie stanowi przedmiotu zamówienia jednostki
   samorządu terytorialnego.

2. Urządzenie MUSI umożliwiać wymianę karty abonenckiej oraz samodzielną konfigurację parametrów
   łączności, numerów uprawnionych i hasła sterującego.

3. Uzależnienie działania urządzenia od usługi świadczonej przez producenta, w szczególności od
   dostępności jego platformy sieciowej, jest niedopuszczalne.

4. **Pierwszym źródłem czasu są państwowe serwery czasu**, wskazane w rozporządzeniu wydanym
   na podstawie ustawy o czasie urzędowym. Urządzenie MUSI korzystać z co najmniej dwóch
   niezależnych źródeł i odmówić wykonania polecenia przy dryfie przekraczającym próg określony
   w załączniku nr 3. Nawigacja satelitarna nie jest źródłem pierwszym.

### § 10. Obowiązki komendantów wojewódzkich i powiatowych (miejskich)

1. Komendanci wojewódzcy Państwowej Straży Pożarnej udostępniają niniejsze Wytyczne wraz
   z załącznikami podmiotom wskazanym w § 4 ust. 1 Wytycznych z dnia 28 maja 2025 r.

2. Komendanci powiatowi (miejscy) Państwowej Straży Pożarnej, w zakresie ustaleń dokonywanych
   ze starostą na podstawie § 7 ust. 1 rozporządzenia, o którym mowa w preambule, uwzględniają
   stan podłączenia syren do SOiA na obszarze powiatu.

3. Komendanci, o których mowa w ust. 1 i 2, prowadzą ewidencję zgłoszonych i dopuszczonych
   urządzeń na obszarze swojej właściwości.

### § 11. Odbiór instalacji oraz sprawdzenia okresowe

1. Uruchomienie instalacji potwierdza się protokołem odbioru, obejmującym scenariusze sprawdzeń
   określone w **załączniku nr 10**, w zakresie odpowiadającym zamówionym klasom zdolności.

2. Czas od wydania polecenia do **rozpoczęcia emisji** mierzy się i wpisuje do protokołu.
   Obowiązującą miarą jest **niezwłoczność** — najszybciej, jak jest to technicznie możliwe.
   Progu czasowego nie ustanawia się, ponieważ nie istnieje norma, z której można by go wyprowadzić;
   wynik pomiaru nie stanowi kryterium odrzucenia, a jego rażące odstępstwo od pozostałych jest
   przesłanką do sprawdzenia instalacji.

3. Sprawdzenie okresowe wykonuje się w trybie i z częstotliwością określoną w § 6 Wytycznych
   z dnia 28 maja 2025 r.; protokół testu odsłuchowego uzupełnia się o potwierdzenie poprawnej
   weryfikacji polecenia i reguły obszaru.

4. Protokoły przechowuje jednostka eksploatująca urządzenie przez okres wskazany w Wytycznych
   z dnia 28 maja 2025 r.

### § 12. Postępowanie w przypadku niezgodności

1. Stwierdzenie, że urządzenie uruchamia sygnał mimo niespełnienia warunków z § 6 ust. 1,
   w szczególności poza własnym obszarem albo poza oknem rozpoczęcia, skutkuje **wyłączeniem
   urządzenia z eksploatacji** do czasu usunięcia przyczyny.

2. Niezgodność zgłasza się niezwłocznie właściwemu komendantowi powiatowemu (miejskiemu)
   Państwowej Straży Pożarnej.

3. W przypadku urządzenia dopuszczonego do poziomu 1 albo 2 administrator SOiA może zawiesić
   jego tożsamość kryptograficzną. Zawieszenie nie ogranicza dostępu do publicznego punktu dostępu.

4. Niezgodność w rozumieniu niniejszych Wytycznych oznacza brak zgodności technicznej lub
   funkcjonalnej z SOiA. Ocena skutków prawnych stwierdzonej niezgodności wymaga każdorazowo
   odniesienia do właściwych przepisów, warunków umowy i okoliczności danego przypadku.

### § 13. Zamówienia publiczne

1. Załącznik nr 11 zawiera **wytyczne do opisu przedmiotu zamówienia**: minimum funkcjonalne i obraz
   zdolności, które muszą się w zamówieniu znaleźć, żeby urządzenie dało się obsłużyć w ramach SOiA.

2. Zamawiający, zgodnie z przepisami o zamówieniach publicznych, uszczegóławia wymagania i dostosowuje
   je do potrzeb jednostki oraz przedmiotu postępowania. Odpowiedzialność za opis przedmiotu zamówienia pozostaje po jego
   stronie.

3. Wymagania formułuje się przez wskazanie **funkcji**, nie przez opis konkretnego wyrobu. Wartości
   liczbowe opisujące platformę występują wyłącznie tam, gdzie funkcji nie da się sprawdzić inaczej.

### § 14. Załączniki

| Nr | Tytuł |
|---|---|
| 1 | Słownik pojęć |
| 2 | Informacja dla organów ochrony ludności i jednostek samorządu terytorialnego |
| 3 | Wymagania minimalne dla urządzenia |
| 4 | Katalog sygnałów i plików referencyjnych |
| 5 | Profile sterownika i maszyna stanów |
| 6 | Podłączenie na poziomie 0 — publiczny wykaz poleceń |
| 7 | Podłączenie na poziomie 1 — rejestracja i kanał powiadomienia |
| 8 | Podłączenie na poziomie 2 — sieć wydzielona i kanał wiadomości tekstowych |
| 9 | Karta konfiguracji urządzenia |
| 10 | Scenariusze sprawdzeń i protokół odbioru |
| 11 | Wytyczne do opisu przedmiotu zamówienia |
| 12 | Podstawa prawna |

### § 15. Wejście w życie

Wytyczne wchodzą w życie z dniem ………………… 2026 r.

<br>

<div align="right">

**Miejsce na podpis**

…………………………………………

Zastępca Komendanta Głównego
Państwowej Straży Pożarnej

</div>
