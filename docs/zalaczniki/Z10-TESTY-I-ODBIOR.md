---
title: "Załącznik nr 10 — Scenariusze sprawdzeń i protokół odbioru"
---

[← Powrót do podręcznika](../index.md#spis-tresci)

# Załącznik nr 10 — Scenariusze sprawdzeń i protokół odbioru


## Rola sprawdzeń w procesie dopuszczenia instalacji

Poziom 0 nie wymaga rejestracji i nie zawiera centralnej bramki dopuszczającej implementację.
Poprawność mechanizmu weryfikacji musi zatem zostać potwierdzona w badaniach zgodności modelu oraz
podczas odbioru konkretnej instalacji.

Sprawdzenia powinny obejmować przede wszystkim przypadki negatywne, w których urządzenie ma odmówić
wykonania polecenia. Pozytywny test emisji nie potwierdza samodzielnie poprawności reguły obszaru,
ważności treści ani podpisu. Z tego względu wymagane są również próby z poleceniem dla obcej gminy,
treścią przeterminowaną i niepoprawnym podpisem.

## Zakres sprawdzeń zgodny z przedmiotem zamówienia

Każdy scenariusz ma przypisaną **klasę zdolności** — tę samą, która w załączniku nr 3 rozstrzyga,
kiedy wymaganie obowiązuje. Instalacja, w której sterownik steruje syreną cyfrową przez jej własny
interfejs, nie podlega sprawdzeniom klasy II, bo nie odtwarza dźwięku. Instalacja bez profilu
głosowego nie podlega sprawdzeniom klasy III.

| Znak | Zakres |
|---|---|
| **I** | rdzeń — zawsze |
| **II** | tor audio — gdy sterownik sam odtwarza dźwięk |
| **III** | profil głosowy — gdy zamówiono |
| **D** | dostawa i montaż — gdy przedmiotem zamówienia jest kompletny zestaw |
| **P** | wobec producenta syreny — sprawdzenie dokumentowe |

## Metodyka sprawdzeń negatywnych

Sprawdzenie negatywne — „urządzenie ma **nie** zareagować” — jest wiarygodne tylko wtedy, gdy
polecenie próbne różni się od poprawnego **wyłącznie tym jednym elementem**, który badamy.

Najgroźniejszy przypadek to test reguły obszaru. Polecenie wystawione w środowisku testowym
zostanie odrzucone już na kontroli środowiska (`W-A05`), zanim dojdzie do porównania kodów gmin.
Wynik będzie pozytywny — i **nie odróżni urządzenia z działającą regułą obszaru od urządzenia,
które tej reguły nie ma w ogóle**.

Dlatego polecenie próbne do sprawdzeń negatywnych musi być **poprawne pod każdym innym względem**:
to samo środowisko, ten sam profil, ten sam klucz, ważny termin i otwarte okno rozpoczęcia.
Wystawianie takich poleceń jest funkcją systemu, a nie czynnością instalatora — opisano ją
w wymaganiach produktowych po stronie SOiA.

Sprawdzenia dzielą się na trzy grupy: **zgodności modelu**, wykonywane raz dla modelu i wersji
oprogramowania; **odbiorowe**, wykonywane dla każdej instalacji; oraz **okresowe**, powtarzane
w eksploatacji.

!!! note "Ciągłość identyfikatorów scenariuszy"

    Identyfikatory S-102 i S-103 dodano w późniejszym etapie redakcji. Zachowano ich numery, aby nie
    unieważniać istniejących odwołań; kolejność prezentacji odpowiada zakresowi tematycznemu, a nie
    kolejności numerów.

---

## 1. Sprawdzenia zgodności modelu

Wykonywane jednorazowo dla danego modelu i wersji oprogramowania, przez producenta albo wykonawcę,
przed pierwszym wdrożeniem. Wynik dotyczy modelu, nie egzemplarza.

### 1.1. Weryfikacja treści

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-01 | **I** | Poprawny wykaz, polecenie dla własnej gminy | emisja |
| S-02 | **I** | Podpis niepoprawny | odrzucenie **całego** wykazu, brak emisji |
| S-03 | **I** | Treść zmodyfikowana po podpisaniu | odrzucenie całości |
| S-04 | **I** | Nieznany identyfikator klucza | odrzucenie, brak emisji |
| S-05 | **I** | Klucz z okna wymiany — poprzedni, wciąż ważny | poprawna weryfikacja, emisja |
| S-06 | **I** | Niezgodna wersja profilu albo środowiska | odrzucenie |
| S-07 | **I** | Wektory wzorcowe podpisu | zgodność co do bajtu |
| S-08 | **I** | Wykaz i polecenie przekraczające ogłoszony limit rozmiaru | odrzucenie jako **błąd**, nie jako brak poleceń; urządzenie pozostaje sprawne |

### 1.2. Reguła obszaru

Wszystkie sprawdzenia negatywne w tej grupie wykonuje się poleceniem poprawnym pod każdym innym
względem — zgodnie z uwagą metodyczną powyżej.

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-09 | **I** | Polecenie dla własnej gminy | emisja |
| S-10 | **I** | Polecenie dla powiatu obejmującego tę gminę | emisja |
| S-11 | **I** | Polecenie dla województwa obejmującego tę gminę | emisja |
| S-12 | **I** | Polecenie dla obszaru obejmującego wiele województw | emisja |
| S-13 | **I** | Polecenie dla obcej gminy | **brak emisji** |
| S-14 | **I** | Gmina miejsko-wiejska: polecenie dla całej gminy, urządzenie w mieście | emisja |
| S-15 | **I** | Gmina miejsko-wiejska: polecenie dla obszaru wiejskiego, urządzenie w mieście | **brak emisji** |
| S-16 | **I** | Kod sześciocyfrowy, bez cyfry rodzaju | odrzucenie kodu, brak emisji |
| S-17 | **I** | Kod miejscowości albo ulicy | pominięcie, brak emisji |
| S-18 | **I** | Konfiguracja urządzenia kodem powiatu | **odrzucenie konfiguracji albo ostrzeżenie** |

### 1.3. Czas, źródła czasu i powtórzenia

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-19 | **I** | Wykaz po terminie ważności | brak emisji |
| S-20 | **I** | Okno rozpoczęcia już zamknięte | brak emisji |
| S-21 | **I** | Ten sam identyfikator polecenia po restarcie urządzenia | **brak drugiej emisji** |
| S-22 | **I** | Ten sam identyfikator po zaniku i powrocie zasilania | brak drugiej emisji |
| S-23 | **I** | To samo polecenie dwoma różnymi kanałami | dokładnie jedna emisja |
| S-24 | **I** | Odwołanie akcji przed jej rozpoczęciem | brak emisji |
| S-25 | **I** | Odwołanie akcji po jej zakończeniu | zapis zdarzenia, brak działania |
| S-26 | **I** | Odwołanie akcji, której urządzenie nigdy nie widziało | trwały znacznik, brak emisji przy późniejszym odtworzeniu |
| S-27 | **I** | Dryf zegara przekraczający 30 s | brak emisji, zapis przyczyny |
| S-28 | **I** | Utrata źródła podstawowego czasu | przejście na źródło kolejne z hierarchii, praca bez przerwy |
| S-29 | **I** | Brak synchronizacji dłuższy niż doba | sygnalizacja stanu, praca na zegarze podtrzymywanym |

### 1.4. Katalog sygnałów

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-30 | **I** | Każdy sygnał z katalogu — czas trwania | zgodność w tolerancji ±5 % |
| S-31 | **I** | Każdy sygnał z katalogu — struktura | modulacja oraz liczba i długość przerw zgodne z wzorcem |
| S-32 | **II** | Poziom w zadeklarowanym punkcie pomiarowym | w granicach ±3 dB względem wzorca, bez przesterowania |
| S-33 | **II** | Regulacja poziomu | zmiana skuteczna, realizowana programowo |
| S-34 | **I** | Nieznany kod sygnału w wykazie | odrzucenie **tego** polecenia, obsługa pozostałych bez zakłóceń |
| S-35 | **II** | Plik o niezgodnej sumie kontrolnej | odmowa instalacji |
| S-36 | **II** | Pojemność pamięci na pakiet dźwiękowy | mieści komplet plików w dwóch wersjach |

### 1.5. Komunikat głosowy

Wykonywane wyłącznie wtedy, gdy zamówiono profil głosowy.

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-37 | **III** | Synteza przy całkowitym braku łączności | komunikat wypowiedziany, zrozumiały |
| S-38 | **III** | Komunikat głosowy zbiegający się z sygnałem akustycznym | sygnał akustyczny **nieopóźniony i niezastąpiony** |
| S-39 | **III** | Ten sam tekst przy tej samej wersji modelu | ten sam dźwięk |

### 1.6. Kanały i odporność

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-40 | **I** | Kanał niezwłocznego powiadomienia wyłączony | wykrycie zmiany samym odpytywaniem |
| S-41 | **I** | Odpowiedź z pamięci pośredniej starsza niż oczekiwana | ponowienie żądania |
| S-42 | **I** | Przekroczenie limitu zapytań | wstrzymanie na wskazany czas |
| S-43 | **I** | Usługa niedostępna | brak emisji, kontrolowane wycofanie |
| S-44 | **I** | Utrata kanału podstawowego | praca kanałem zapasowym, **pełny zakres weryfikacji** |
| S-45 | **I** | Polecenie tekstowe z nieuprawnionego numeru | odrzucenie i zapis zdarzenia |
| S-46 | **I** | Polecenie tekstowe z błędnym hasłem | odrzucenie i zapis zdarzenia |
| S-47 | **I** | Powtórzone polecenie tekstowe w oknie blokady | odrzucenie i zapis |
| S-48 | **I** | Polecenie tekstowe podzielone na wiele wiadomości | **odrzucenie**, bez próby sklejania |
| S-102 | **I** | Powtórzenie przechwyconego polecenia tekstowego z tym samym znacznikiem i licznikiem | **odrzucenie** i zapis zdarzenia |
| S-49 | **I** | Polecenie przyjęte kanałem umożliwiającym odpowiedź | potwierdzenie **przyjęcia** odrębne od potwierdzenia wykonania |

### 1.7. Współistnienie z systemem istniejącym

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-50 | **I** | Uruchomienie dotychczasowym sposobem po dołączeniu kanału SOiA | **działa bez zmian** |
| S-51 | **I** | Uruchomienie lokalne przy całkowitym braku łączności z SOiA | działa |
| S-52 | **I** | Polecenie z drugiego toru w trakcie trwającej emisji | odrzucenie i zapis, **bez kolejkowania i bez drugiej emisji** |
| S-53 | **I** | Polecenie odroczone z S-52, którego okno rozpoczęcia nadal trwa | **ponowienie po zakończeniu bieżącej emisji**, zapis odroczenia i ponowienia |
| S-54 | **I** | Odcięcie lokalne przy emisji uruchomionej z toru SOiA | odcięcie skuteczne |
| S-55 | **I** | Tryb serwisowy wobec polecenia z każdego toru | blokada zdalnego uruchomienia |
| S-56 | **I** | Próba zatrzymania trwającej emisji poleceniem zdalnym | **odrzucenie**, emisja dokończona |

### 1.8. Platforma, zasilanie i diagnostyka

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-57 | **I** | Zawieszenie oprogramowania | samoczynny restart przez układ nadzoru |
| S-58 | **I** | Restart urządzenia z niewysłanymi zapisami rejestru | zapisy **zachowane**, nic nie ginie |
| S-59 | **I** | Odczyt rejestru bez oprogramowania producenta | format otwarty, czytelny |
| S-60 | **I** | Czas od załączenia zasilania do gotowości operacyjnej | nie dłuższy niż 60 s |
| S-61 | **I** | Zwarcie na wyjściu obiektowym | urządzenie pracuje dalej, tor wykonawczy sprawny |
| S-62 | **I** | Impuls 200 ms na wejściu uruchomienia lokalnego | wykryty |
| S-63 | **I** | Odczyt stanu przy zamkniętej obudowie | praca z rezerwy, niski stan energii, gotowość i brak łączności **rozróżnialne z zewnątrz** |
| S-64 | **I** | Nieudana aktualizacja | powrót do poprzedniej wersji, materiał kryptograficzny zachowany |
| S-65 | **I** | Przełączenie na alternatywny punkt dostępu i punkt zaufania | skuteczne, bez udziału producenta |

### 1.9. Sprawdzenia dokumentowe

Wykonywane przez przegląd dokumentacji, nie na stanowisku.

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-66 | **D** | Deklaracja zgodności, wykaz norm zharmonizowanych, sprawozdania z badań | przedłożone i kompletne |
| S-103 | **I** | Dokumentacja interfejsów elektrycznych, audio i integracyjnych **wraz ze schematem elektrycznym** | przedłożona, w zakresie umożliwiającym samodzielny serwis |
| S-67 | **D** | Model degradacji magazynu energii i świadectwo dla profilu obciążenia obejmującego emisję | przedłożone |
| S-68 | **P** | Specyfikacja interfejsu sterowania syreną | opublikowana, kompletna, z warunkami licencyjnymi dopuszczającymi integrację przez podmiot trzeci |
| S-69 | **P** | Wejście liniowe audio i zwarciowe wejście nadawania syreny | udokumentowane wraz z parametrami elektrycznymi |
| S-70 | **P** | Integracja wykonana przez podmiot trzeci, bez udziału producenta syreny | wykazana |

---

## 2. Sprawdzenia odbiorowe instalacji

Wykonywane dla **każdej** instalacji, przy uruchomieniu, i dokumentowane w karcie konfiguracji.
Zakres zależy od zamówionych klas zdolności.

### 2.1. Dostawa i montaż

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-71 | **D** | Kompletność dostawy wobec listy zawartości zestawu | wszystkie pozycje obecne, brak uszkodzeń transportowych |
| S-72 | **D** | Data produkcji i ostatniego ładowania magazynu energii, pomiar napięcia przed uruchomieniem | odnotowane, napięcie w zakresie |
| S-73 | **D** | Kontrola mechaniczna: zamocowanie, otwarcie obudowy, stabilność magazynu energii i anten | zgodne z listą kontrolną producenta |
| S-74 | **D** | Kontrola elektryczna przed załączeniem: obwód wyłączony, ciągłość ochronna, polaryzacja, izolacja żył niewykorzystanych | zgodne z listą kontrolną producenta |
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

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-84 | **I** | Obszar wpisany kodami gmin | bez kodu powiatu i województwa, zgodny z rejestrem podziału terytorialnego |
| S-85 | **I** | Hasło sterujące | zmienione z domyślnego i **unikalne dla urządzenia** |
| S-86 | **I** | Numery uprawnione | wprowadzone, zgodne z kartą konfiguracji |
| S-87 | **I** | Adres punktu dostępu i identyfikator klucza | zgodne z aktualnymi wartościami publikowanymi |
| S-88 | **II** | Pliki referencyjne | wgrane, sumy kontrolne potwierdzone wobec Wytycznych z 28 maja 2025 r., wersja pakietu odnotowana |

### 2.3. Uruchomienie

| Nr | Klasa zdolności | Scenariusz | Oczekiwany wynik |
|---|---|---|---|
| S-89 | **I** | Łączność | zasięg albo połączenie przewodowe potwierdzone |
| S-90 | **I** | Test łączności | przyjęcie potwierdzone, **bez emisji zewnętrznej** |
| S-91 | **I** | Ogłoszenie alarmu | przyjęcie i wykonanie potwierdzone |
| S-92 | **I** | Odwołanie alarmu | **emisja sygnału ciągłego, a nie cisza** |
| S-93 | **I** | Polecenie dla obcej gminy, poprawne pod każdym innym względem | brak reakcji |
| S-94 | **I** | Powtórzenie tego samego polecenia | brak drugiej emisji |
| S-95 | **I** | Odcięcie lokalne | skuteczne |
| S-96 | **I** | Zachowanie po restarcie | brak samoczynnego uruchomienia |
| S-97 | **D** | Podtrzymanie zasilania | zgodne z deklaracją |
| S-98 | **I** | Zmierzony **czas od wydania polecenia do rozpoczęcia emisji** | odnotowany; **bez progu zaliczenia** |
| S-99 | **D** | Temperatura pomieszczenia w chwili odbioru | odnotowana; **zapis stanu, nie warunek dopuszczenia** |
| S-100 | **I** | Dotychczasowy sposób uruchomienia **po** dołączeniu kanału SOiA | działa bez zmian |
| S-101 | **I** | Uruchomienie lokalne przy odłączonej łączności | działa |

!!! warning "Sprawdzenia powodujące emisję zewnętrzną"

    Sprawdzenia powodujące **emisję zewnętrzną** wymagają uprzedzenia mieszkańców i uzgodnienia
    z właściwym organem. Tam, gdzie to możliwe, wykonuje się je na sygnale ćwiczebnym albo w trybie
    lokalnym bez emisji. Sprawdzenia S-91 i S-92 są jedynymi, których nie da się wykonać inaczej —
    i dlatego uzgodnienie terminu jest częścią przygotowania odbioru, a nie jego utrudnieniem.

**Interpretacja wyniku S-98.** Projekt nie ustanawia liczbowego progu zaliczenia; stosuje wymóg
niezwłoczności. Pomiar służy zgromadzeniu porównywalnych danych z instalacji. Wynik istotnie
odstający od pozostałych stanowi przesłankę do dodatkowej diagnostyki, a nie samodzielną podstawę
odmowy podpisania protokołu.

**Interpretacja wyniku S-99.** Projekt nie nakłada wymagań na warunki obiektowe. Pomiar dokumentuje
warunki w chwili odbioru, lecz nie potwierdza ich zgodności z deklarowanym zakresem pracy przez cały
rok. Ocena warunków całorocznych należy do właściciela obiektu i projektanta instalacji.

---

## 3. Sprawdzenia okresowe

**Test odsłuchowy — nie rzadziej niż raz na dwanaście miesięcy** oraz po każdej modernizacji
sterownika, w trybie i na wzorze protokołu określonym w Wytycznych z 28 maja 2025 r. Obejmuje
odtworzenie każdego pliku w trybie lokalnym, pomiar czasu trwania i potwierdzenie struktury.

Do tego sprawdzenia dochodzą trzy uzupełniające, wynikające z niniejszych Wytycznych:
**potwierdzenie poprawnej weryfikacji polecenia** — próbą z celowo niepoprawnym podpisem;
**potwierdzenie reguły obszaru** — próbą z kodem obcej gminy, poprawną pod każdym innym względem;
oraz **sprawdzenie stanu zasilania rezerwowego**.

Rozbieżność czasu trwania przekraczająca 5 % albo zmiana struktury sygnału powoduje **wyłączenie
syreny z eksploatacji** do czasu ponownego wgrania pliku wzorcowego. Protokoły przechowuje jednostka
eksploatująca przez okres wskazany w Wytycznych z 28 maja 2025 r.

Dopóki system nie zapewnia potwierdzania obecności urządzeń, test okresowy pozostaje podstawowym
udokumentowanym źródłem informacji o sprawności instalacji. Ewentualne wprowadzenie częstszych
testów indywidualnych wymaga odrębnego określenia procedury, częstotliwości i kryteriów oceny.

---

## 4. Protokół odbioru instalacji

!!! note "Jak czytać protokół odbioru"

    Protokół grupuje wyniki, ale nie zastępuje dowodów szczegółowych z testów i karty konfiguracji. Wykonawca przedstawia wyniki sprawdzeń, przedstawiciel właściciela ocenia ich kompletność i podpisuje rozstrzygnięcie. Wynik „z uwagami” nie usuwa obowiązku usunięcia niezgodności, która według kryteriów dopuszczenia wyklucza eksploatację.

**Instalacja:** …………………………………………………  **Identyfikator urządzenia:** ……………………………

**Data:** ………………  **Wykonujący:** ………………………………  **Przedstawiciel właściciela:** ………………………

**Zamówione klasy zdolności:** ☐ I ☐ II ☐ III ☐ D

| Grupa | Scenariusze | Wynik |
|---|---|---|
| Dostawa i montaż | S-71 … S-83 | ☐ zgodne ☐ uwagi ☐ nie dotyczy |
| Konfiguracja | S-84 … S-88 | ☐ zgodne ☐ uwagi |
| Uruchomienie i emisja | S-89 … S-92 | ☐ zgodne ☐ uwagi |
| Odmowa | S-93, S-94 | ☐ zgodne ☐ uwagi |
| Bezpieczeństwo i zasilanie | S-95 … S-97 | ☐ zgodne ☐ uwagi |
| Współistnienie | S-100, S-101 | ☐ zgodne ☐ uwagi ☐ nie dotyczy |

**Zmierzony czas od wydania polecenia do rozpoczęcia emisji (S-98):** ………… s *(bez progu zaliczenia)*

**Zmierzona temperatura pomieszczenia (S-99):** ………… °C *(zapis stanu)*

**Stwierdzone niezgodności i termin usunięcia:**

_______________________________________________________________________

_______________________________________________________________________

**Rozstrzygnięcie:** ☐ instalacja dopuszczona do eksploatacji ☐ dopuszczona z uwagami
☐ niedopuszczona

Podpisy: ………………………………………  ………………………………………

---

## 5. Proponowane kryteria dopuszczenia instalacji

Instalacja, która uruchamia syrenę mimo niespełnienia warunków — poza własnym obszarem, poza oknem
rozpoczęcia albo przy niepoprawnym podpisie — nie spełnia kryteriów dopuszczenia określonych
w projekcie i wymaga usunięcia przyczyny przed eksploatacją.

Brak emisji po niespełnieniu warunków weryfikacji jest zachowaniem zgodnym z zasadą fail-closed.
Porównanie skutków fałszywego uruchomienia i pominięcia alarmu wymaga odrębnej analizy ryzyka i nie
jest rozstrzygane w niniejszej części.

Wynik pomiaru w scenariuszach S-98 i S-99, dla których projekt nie ustanawia progu, nie stanowi
samodzielnej podstawy odmowy dopuszczenia. Służy dokumentowaniu stanu i tworzeniu zbioru danych
do późniejszego określenia wartości referencyjnych.


---
