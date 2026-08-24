---
tytuł: "Załącznik nr 8 — Poziom 2: sieć wydzielona i kanał wiadomości tekstowych"
dokument: "Podręcznik podłączania syren alarmowych i innych urządzeń do SOiA"
wersja: 0.4
data: 2026-08-23
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
źródło: "Wydzielono z PODRECZNIK_v2.md"
---

[← Powrót do podręcznika](../PODRECZNIK_v2.md#spis-treści)

# Załącznik nr 8 — Poziom 2: sieć wydzielona i kanał wiadomości tekstowych


## Zakres funkcjonalny poziomu 2

Poziom 2 dodaje dwie zdolności: pracę w wydzielonej sieci operatora, podlegającej kontroli dostępu,
oraz kanał wiadomości tekstowych przeznaczony dla lokalizacji, w których transmisja danych jest
niestabilna albo niedostępna.

Kanał wiadomości tekstowych jest dwukierunkowy. Urządzenie może przekazywać odrębne potwierdzenia
przyjęcia i wykonania polecenia; żadne z nich nie stanowi potwierdzenia słyszalności sygnału.

---

## 1. Dostęp do usług SOiA z sieci wydzielonej

Punkt dostępu SOiA oraz usługa powiadomień są osiągalne **równolegle z sieci wydzielonej
i z publicznego internetu**. Urządzenie pracujące w sieci wydzielonej używa **tego samego adresu**
i tej samej ścieżki co urządzenie na poziomie otwartym — zmienia się droga, nie kontrakt.

Obecność warstwy pośredniczącej nie narusza podpisu, jeżeli podpisane bajty pozostają niezmienione.
Warstwa ta nie może jednak modyfikować podpisanego dokumentu, interpretować poleceń ani stosować
własnej reguły obszaru. Treść objęta podpisem musi zostać przekazana bez zmian.

Sieć wydzielona ogranicza, **dokąd** urządzenie może się połączyć. Nie zmienia zakresu weryfikacji
polecenia: praca w sieci zaufanej nie jest podstawą do uruchomienia syreny.

---

## 2. Profil komunikacji za pośrednictwem wiadomości tekstowych

Profil jest **wersjonowany i będzie się zmieniał** wraz z profilami kolejnych producentów. Poniżej
opisano jego strukturę; obowiązujące dla danej instalacji wartości zapisuje się w karcie
konfiguracji, o której mowa w załączniku nr 9.

### Identyfikator urządzenia

Trzy człony: **numer kolejny nadany przez system**, **typ syreny** oraz **kod jednostki
terytorialnej**. Katalog typów obejmuje cztery wartości: **syrena elektroniczna**, **syrena
silnikowa**, **instalacja modernizowana (retrofit)** oraz **inne urządzenie sygnalizacyjne**.

Człon terytorialny identyfikatora służy do **rozpoznania urządzenia** i nie jest jego obszarem
działania. Obszar konfiguruje się osobno, listą siedmiocyfrowych kodów gmin. Te dwie wartości mogą
się różnić i różnica jest poprawna, nie błędna.

### Polecenie

Wiadomość składa się z **hasła sterującego**, **kodu polecenia** oraz — od wersji profilu
wprowadzanej wraz z niniejszymi Wytycznymi — **znacznika czasu i licznika**. Katalog poleceń
obejmuje test łączności niepowodujący emisji, sygnały akustyczne z katalogu oraz polecenie
awaryjnego wygaszenia wyjścia. Powiązanie kodów poleceń z sygnałami zawiera załącznik nr 4.

Materiał źródłowy określa polecenie awaryjnego wygaszenia jako odcięcie toru wykonawczego.

> [!caution] Wymaga decyzji przed akceptacją — semantyka awaryjnego wygaszenia
> Słownik zastrzega „odcięcie lokalne” dla czynności wykonywanej na obiekcie i wyklucza zdalne
> zatrzymanie rozpoczętej emisji. Przed podpisaniem należy określić semantykę awaryjnego wygaszenia
> wyjścia oraz jego relację do zasady niepodzielności emisji. Redakcja V2 nie rozstrzyga tej
> sprzeczności materiału źródłowego.

### Granice wiadomości

Polecenie musi zmieścić się w **jednej wiadomości: do 160 znaków** podstawowego alfabetu.
Urządzenie **odrzuca wiadomości wieloczęściowe** i nie podejmuje próby ich sklejania — wiadomość
złożona z fragmentów potrafi dotrzeć niekompletna albo w innej kolejności, a polecenie sklejone
z części przestaje być poleceniem, którego treść dało się zweryfikować.

Z tego wynika ograniczenie składni: **wyłącznie znaki podstawowego alfabetu, bez polskich znaków
diakrytycznych**. Ich użycie przełącza kodowanie i skraca wiadomość do 70 znaków, co przy dłuższym
poleceniu wymusiłoby podział — a podziału nie dopuszczamy.

### Ochrona przed powtórzeniem polecenia

W fazie przejściowej, gdy nie ma zamkniętej grupy abonenckiej, realnym zabezpieczeniem pozostaje
hasło i lista numerów uprawnionych. Obie te warstwy są bezradne wobec **powtórzenia przechwyconej
wiadomości**: ta sama treść, wysłana drugi raz, jest nie do odróżnienia od oryginału.

Dlatego polecenie niesie znacznik czasu i licznik, a urządzenie odrzuca wiadomość, której znacznik
odbiega od jego czasu bardziej niż o dopuszczalny margines albo której licznik nie jest wyższy
od ostatnio przyjętego. Kosztuje to kilkanaście znaków i nie wymaga zmiany sprzętu — a usuwa
najprostszy z możliwych ataków w fazie, w której brakuje trzech pozostałych warstw.

### Potwierdzenia

Poprawne polecenie daje **dwa potwierdzenia**, i to rozróżnienie jest istotne:

**Przyjęcie polecenia** — urządzenie odebrało wiadomość, zweryfikowało ją i uznało za swoją.
**Wykonanie** — wyjście zostało uruchomione, sygnał ruszył.

Pierwsze bez drugiego oznacza „przyjęto, uruchomienie niepotwierdzone” i jest stanem wymagającym
reakcji, a nie sukcesem. Żadne z nich **nie jest dowodem słyszalności**.

Potwierdzenia trafiają wyłącznie na numery uprawnione. Pełny katalog kodów potwierdzeń i błędów
oraz sposób odczytania odpowiedzi urządzenia utrzymywany jest w wersjonowanym profilu protokołu,
a nie w tym dokumencie.

---

## 3. Model zabezpieczeń kanału wiadomości tekstowych

Kanał tekstowy **nie ma podpisu kryptograficznego**. Zamiast niego stosuje się obronę w głąb,
w której każda warstwa odcina inną drogę wejścia:

| Warstwa | Co kontroluje | Co odcina |
|---|---|---|
| Karta abonencka wydana centralnie | kto dysponuje nadajnikiem w systemie | podmioty spoza systemu |
| Zamknięta grupa abonencka | ruch wyłącznie wewnątrz grupy | wiadomość z zewnątrz sieci |
| Hasło sterujące na urządzeniu | treść każdego polecenia | wiadomość wysłaną omyłkowo wewnątrz grupy |
| Wykaz numerów uprawnionych | kto może wydać polecenie temu urządzeniu | uczestnika grupy bez uprawnienia |

Komplet czterech warstw tworzy model wielowarstwowej kontroli dostępu do kanału. Nie stanowi on
podpisu kryptograficznego treści. Żadna z warstw stosowana samodzielnie nie jest wystarczająca:
zamknięta grupa nie zastępuje hasła, a hasło nie zastępuje wykazu numerów.

> [!important] Stan przejściowy i docelowy kanału SMS
> W okresie przejściowym urządzenie może korzystać z karty innego operatora, ale nadal stosuje pełną walidację profilu SMS: numery uprawnione, unikalne hasło, składnię, znacznik czasu, licznik i ochronę przed powtórzeniem. W stanie docelowym KG PSP zapewnia kartę SIM w zamkniętej grupie użytkowników (CUG) oraz zarządza warstwą operatorską i listami numerów uprawnionych. CUG ogranicza dostęp do sieci, lecz nie zastępuje kontroli wykonywanych przez urządzenie.

### Planowany okres przejściowy 2026–2027

Projekt zakłada, że w okresie przejściowym jednostki samorządu terytorialnego korzystają z kart
własnych operatorów. Zamknięta grupa abonencka nie jest wówczas dostępna, co usuwa warstwę
ograniczającą ruch do uczestników grupy.

W okresie docelowym ruch spoza grupy jest ograniczany na poziomie sieci. W okresie przejściowym
ochrona opiera się na wykazie numerów uprawnionych, haśle sterującym, znaczniku czasu i liczniku.
Ze względu na możliwość podszycia się pod numer nadawcy na niektórych trasach samo sprawdzenie
numeru nie jest wystarczające.

Stąd wymagania bezwzględne na czas tej fazy: **hasło unikalne dla urządzenia** — wspólne hasło floty
zamienia kompromitację jednej karty konfiguracyjnej w zdarzenie krajowe zamiast lokalnego — oraz
**rejestrowanie i sygnalizowanie odrzuconych poleceń**, bo polecenie odrzucone z nieznanego numeru
jest sygnałem bezpieczeństwa, a nie szumem.

Zalecenie operacyjne: **tam, gdzie dostępny jest tor danych, kanał tekstowy powinien pozostać
uzupełniający, a nie jedyny.** Wpięcie przewodem do sieci obiektu jest w tej fazie wyraźnie
bezpieczniejszą drogą.

Przejście do fazy docelowej **nie zmienia składni poleceń ani kontraktu** — zmienia kartę abonencką
i numery w wykazie uprawnionych. Urządzenie kupione dziś musi je przyjąć bez wymiany sprzętu.

### Ryzyka rezydualne i środki ograniczające

Ryzyko powtórzenia przechwyconej wiadomości jest ograniczane przez znacznik czasu i licznik
określone w W-D25 oraz przez mechanizm niewykonywania tego samego polecenia ponownie w określonym
oknie (W-D14). Skuteczność wymaga trwałego przechowywania licznika, wiarygodnego czasu i ochrony
stanu urządzenia.

Pozostaje ryzyko **podszycia się pod numer nadawcy**, na które w fazie przejściowej nie ma
odpowiedzi technicznej po stronie sieci. Realnym zabezpieczeniem jest wtedy **hasło unikalne
dla urządzenia** — i dlatego jest ono w tej fazie zabezpieczeniem podstawowym, a nie uzupełniającym.

Potwierdzenia wysyłane na numery uprawnione zwiększają wykrywalność nieprawidłowego uruchomienia,
lecz nie gwarantują jego natychmiastowego wykrycia, ponieważ kanał potwierdzeń również może być
niedostępny lub opóźniony.

---

## 4. Ograniczenia skalowalności kanału wiadomości tekstowych

Kanał tekstowy nie jest przeznaczony do samodzielnej obsługi alarmu krajowego. Jego przepustowość
należy potwierdzić przed wdrożeniem i okresowo weryfikować.

Bramka wielokartowa nadaje rzędu jednej wiadomości na sekundę na kartę. Przy ośmiu kartach daje to
około ośmiu wiadomości na sekundę — czyli **blisko godziny na powiadomienie floty rzędu dwudziestu
trzech tysięcy urządzeń**. Przy czterech takich bramkach nadal kilkanaście minut. Tymczasem **okno
rozpoczęcia emisji trwa trzy minuty**, a urządzenie, do którego polecenie dotrze po jego zamknięciu,
zgodnie z zasadą fail-closed nie rozpocznie emisji.

Kanał wiadomości tekstowych należy traktować jako kanał obszarowy i zapasowy, przeznaczony dla
pojedynczych gmin, lokalizacji bez transmisji danych oraz sytuacji awaryjnych. Podstawowym kanałem
o większej skali pozostaje tor danych z niezwłocznym powiadomieniem.

Podane wartości są szacunkiem rzędu wielkości i wymagają potwierdzenia pomiarem u operatora przed
wszczęciem postępowania. Jeżeli zmierzona przepustowość nie zapewni obsługi zakładanego obszaru
w wymaganym czasie, należy zwiększyć liczbę bramek, zmienić założenia dotyczące okna dla tego
kanału albo ograniczyć jego planowany zasięg.

---

## 5. Obsługa stanów awaryjnych

Rozróżnienie, które musi być widoczne dla operatora: **brak potwierdzenia nie jest awarią syreny**.
Może oznaczać awarię bramki, brak zasięgu modemu, problem karty abonenckiej, przeciążenie kolejki
albo opóźnienie w sieci operatora — i każda z tych sytuacji wymaga innej reakcji niż wyjazd
do syreny.

Zasady postępowania. Bramka bez odpowiedzi — wstrzymanie pobierania z kolejki z zachowaniem zleceń,
nie ich porzucenie. Brak zasięgu — wstrzymanie realizacji, nie lawinowe ponawianie. Odrzucenie
polecenia przez bramkę — ponowienie transportowe z kontrolowanym wycofaniem. Brak potwierdzenia
wykonania mimo potwierdzenia przyjęcia — **brak automatycznego uznania sukcesu** i eskalacja.
Odpowiedź spóźniona — zapis i uzgodnienie stanu bez kasowania historii. Odpowiedź niejednoznaczna
albo od nieznanego nadawcy — kwarantanna i zdarzenie bezpieczeństwa. Przeciążenie kolejki —
pierwszeństwo dla poleceń krytycznych i widoczne dla operatora spowolnienie.

Wynik zbiorczy dla obszaru **nie może ukrywać niepowodzeń częściowych**. Operator ma widzieć liczby:
ile urządzeń potwierdziło przyjęcie, ile wykonanie, ile nie odpowiedziało — a nie jeden komunikat
„wysłano”.

---

## 6. Ochrona i przechowywanie wartości operacyjnych

Numery abonenckie, hasła sterujące, wykazy numerów uprawnionych, nazwy sektorów i parametry sieci
**nie są częścią tego dokumentu**. Zapisuje się je w karcie konfiguracji urządzenia, przekazywanej
instalatorowi poza obiegiem publikowanym — wzór karty zawiera załącznik nr 9.

Podręcznik określa struktury danych, natomiast wartości właściwe dla konkretnej instalacji są
przechowywane w karcie konfiguracji.


---
