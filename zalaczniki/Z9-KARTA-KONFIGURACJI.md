---
tytuł: "Załącznik nr 9 — Karta konfiguracji urządzenia"
dokument: "Podręcznik podłączania syren alarmowych i innych urządzeń do SOiA"
wersja: 0.4
data: 2026-08-23
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
źródło: "Wydzielono z PODRECZNIK_v2.md"
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 9 — Karta konfiguracji urządzenia


## Przeznaczenie i zasady stosowania karty

Jedna karta opisuje **jedno urządzenie**. Zawiera wszystkie wartości potrzebne instalatorowi
do uruchomienia instalacji i wszystkie wartości, których **nie ma w żadnym dokumencie
publikowanym**: numery, hasło sterujące, wykaz numerów uprawnionych, identyfikator urządzenia
i mapę poleceń.

Podział jest celowy. Wytyczne i pozostałe załączniki opisują **struktury** i można je swobodnie
rozsyłać. Karta zawiera **wartości** i krąży poza obiegiem publikowanym — w wydruku albo
w przekazie chronionym, nigdy w repozytorium ani w załączniku do wiadomości rozsyłanej szeroko.

> [!warning] Dokument zawierający dane wrażliwe operacyjnie
> Wypełniona karta zawiera dane uwierzytelniające i numery uprawnione. Jej przekazywanie,
> przechowywanie, aktualizowanie, archiwizowanie i wycofywanie powinno odbywać się zgodnie
> z zatwierdzoną polityką bezpieczeństwa, retencji i odpowiedzialności dowodowej.

Legenda: oznaczenie **[W]** wskazuje pole wypełniane przez instalatora na obiekcie. Pozostałe
wartości nadaje Komenda Główna PSP albo zamawiający, a instalator wprowadza je bez zmian.

> [!note] Odpowiedzialność za kartę konfiguracji
> Karta nie służy wykonawcy do samodzielnego ustalania wartości operacyjnych. KG PSP albo zamawiający przekazuje wartości zatwierdzone dla instalacji, instalator wprowadza je bez zmiany i uzupełnia pola oznaczone `[W]`, a właściciel przejmuje kartę po odbiorze. Każda późniejsza zmiana wartości wymaga aktualizacji karty przez podmiot do tego uprawniony.

---

## A. Identyfikacja urządzenia

| Pole | Wartość |
|---|---|
| Numer karty / urządzenia | |
| Jednostka odpowiedzialna | |
| Lokalizacja — miejscowość, adres, obiekt | [W] |
| Identyfikator urządzenia | `………………-……-………` — numer kolejny, typ, kod jednostki |
| Typ syreny | ☐ elektroniczna ☐ silnikowa ☐ instalacja modernizowana (retrofit) ☐ inne urządzenie sygnalizacyjne |
| Zamówione klasy zdolności | ☐ I ☐ II ☐ III |
| Zakres zamówienia | ☐ dostawa i montaż (D) ☐ wymagania wobec producenta syreny (P) |
| Producent i model syreny | |
| Numer seryjny syreny | [W] |
| Producent i model sterownika | |
| Numer seryjny sterownika | [W] |
| Wersja oprogramowania sterownika | [W] |

---

## B. Obszar działania

Wpisać **wyłącznie siedmiocyfrowe kody gmin**, na których syrena fizycznie oddziałuje. Kod powiatu
lub województwa jest niedopuszczalny — urządzenie tak skonfigurowane pominie ostrzeżenia zadane
przez narysowanie obszaru na mapie.

| Lp. | Kod gminy (7 cyfr) | Nazwa jednostki |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

Potwierdzenie zgodności kodów z rejestrem podziału terytorialnego: [W] ……………………… (data, podpis)

---

## C. Łączność

| Pole | Wartość |
|---|---|
| Sposób podłączenia podstawowy | ☐ przewodowy ☐ bezprzewodowy ☐ komórkowy |
| Sposób podłączenia zapasowy | ☐ przewodowy ☐ bezprzewodowy ☐ komórkowy ☐ brak |
| Adres punktu dostępu SOiA | |
| Numer abonencki urządzenia | |
| Operator / rodzaj sieci | ☐ sieć wydzielona ☐ operator własny jednostki *(faza 2026–2027)* |
| Kod PIN karty abonenckiej | [W] ………… ☐ PIN wyłączony |
| Punkt dostępu do sieci danych | [W] |
| Data i sposób przekazania karty abonenckiej | [W] |

---

## D. Zabezpieczenia

| Pole | Wartość |
|---|---|
| Hasło sterujące | [W] ………………… — **zmienić z domyślnego**, nadać **unikalne dla tego urządzenia** |
| Data ustalenia hasła | [W] |
| Numery uprawnione do wydawania poleceń | 1) …………………  2) ………………… |
| Numery otrzymujące potwierdzenia | 1) …………………  2) ………………… |
| Identyfikator klucza weryfikującego wykaz | |
| Sposób przechowywania materiału kryptograficznego | ☐ moduł sprzętowy ☐ bezpieczna enklawa procesora |

> [!warning] Unikalność hasła sterującego
> Hasło wspólne dla wielu urządzeń jest niedopuszczalne. W okresie bez sieci wydzielonej hasło jest
> podstawowym, a nie wyłącznie uzupełniającym zabezpieczeniem kanału tekstowego.

---

## E. Mapa poleceń i wysterowanie syreny

| Polecenie | Sygnał | Kod polecenia |
|---|---|---|
| Test łączności — bez emisji | — | |
| Ogłoszenie alarmu — ludność cywilna | modulowany, 180 s | |
| Odwołanie alarmu — ludność cywilna | ciągły, 180 s | |
| Alarm dla jednostki ochrony ppoż. | 3 bloki z przerwami 30 s, 180 s | |
| Alarm ćwiczebny lub treningowy | ciągły, 60 s | |
| Awaryjne wygaszenie wyjścia | — | |

| Pole | Wartość |
|---|---|
| Tryb sprzężenia z syreną | ☐ cyfrowy przez interfejs syreny ☐ audio — syrena jako nagłośnienie ☐ stykowy |
| Wyjście audio — kanał i poziom | [W] |
| Wyjście sterowania nadawaniem | [W] nr przekaźnika: ………… |
| Wyjścia przekaźnikowe — przeznaczenie | [W] |
| Wersja pakietu plików referencyjnych | `v.………………` |
| Napięcie zasilania części zewnętrznej pod obciążeniem | [W] ………… V |
| Zmierzona jakość toru radiowego części wewnętrznej | [W] |
| Potwierdzenie sum kontrolnych plików | ☐ zgodne — [W] data: ………… |

---

## E.1. Elementy zapewniane przez instalatora

Zestaw nie obejmuje elementów zależnych od obiektu — długości tras, rodzaju podłoża i warunków
zewnętrznych. Ich brak w dostawie **nie jest niekompletnością**. Firma monterska przygotowuje je
przed przyjazdem, po ustaleniu warunków na miejscu.

> [!note] Przykład: elementy zależne od obiektu
> Kotwy dobiera się do konkretnej ściany i nie można ich ustalić wyłącznie na podstawie modelu sterownika. Brak właściwych kotew nie jest wadą fabrycznej dostawy, ale uniemożliwia bezpieczny montaż. Warunki obiektu należy więc rozpoznać przed rozpoczęciem prac, a potrzebne elementy przygotować przed przyjazdem na montaż.

| Element | Przygotowano |
|---|---|
| Przewód sieciowy między częścią wewnętrzną a zewnętrzną, odpowiedniej kategorii i długości | ☐ |
| Przedłużenie przewodu zasilającego część zewnętrzną | ☐ |
| Przewód i złącza wielkiej częstotliwości dla anteny nawigacji satelitarnej | ☐ |
| Puszki połączeniowe o szczelności właściwej dla montażu zewnętrznego | ☐ |
| Dławnice, przepusty, uszczelnienia i materiały odporne na promieniowanie słoneczne | ☐ |
| Kotwy, kołki i śruby dobrane do rodzaju i nośności ściany | ☐ |
| Konstrukcja wsporcza części zewnętrznej, jeżeli montaż na ścianie nie jest możliwy | ☐ |
| Przewody zasilania sieciowego i ochronny | ☐ |
| Środki ochrony przepięciowej wynikające z projektu obiektu | ☐ |

---

## F. Odbiór instalacji

| Czynność | Wynik |
|---|---|
| Kompletność dostawy sprawdzona wobec listy zawartości zestawu | ☐ |
| Kontrola mechaniczna i elektryczna przed załączeniem wykonana | ☐ |
| Okablowanie zgodne z mapą listwy przyłączeniowej | ☐ |
| Temperatura pomieszczenia — **zmierzona i odnotowana** [W] ………… °C | ☐ |
| Karta abonencka włożona, zasięg potwierdzony | ☐ |
| Bezprzerwowe przejście na zasilanie rezerwowe sprawdzone | ☐ |
| Łącze między częścią wewnętrzną a zewnętrzną aktywne | ☐ |
| Hasło sterujące zmienione z domyślnego i unikalne | ☐ |
| Numery uprawnione wprowadzone | ☐ |
| Obszar skonfigurowany kodami gmin, bez kodu powiatu | ☐ |
| Pliki referencyjne wgrane, sumy kontrolne zgodne **z Wytycznymi z 28 maja 2025 r.** | ☐ |
| Wyjścia zmapowane zgodnie z częścią E | ☐ |
| Test łączności — potwierdzenie przyjęcia, **bez emisji** | ☐ |
| Test ogłoszenia alarmu — przyjęcie i wykonanie | ☐ |
| Test odwołania alarmu — **emisja sygnału ciągłego, nie cisza** | ☐ |
| Test zachowania przy poleceniu dla obcej gminy, **poprawnym pod każdym innym względem** — brak reakcji | ☐ |
| Test powtórzenia tego samego polecenia — brak drugiej emisji | ☐ |
| Odcięcie awaryjne — sprawdzone | ☐ |
| Podtrzymanie zasilania — sprawdzone | ☐ |
| Zmierzony czas od wydania polecenia **do rozpoczęcia emisji** *(bez progu zaliczenia)* | [W] ………… s |

Uwagi: [W]

_______________________________________________________________________

_______________________________________________________________________

| Instalator | Przedstawiciel właściciela |
|---|---|
| imię, nazwisko | imię, nazwisko |
| data | data |
| podpis | podpis |

---

## Zasady obiegu i aktualizacji wypełnionej karty

Egzemplarz przekazuje się właścicielowi urządzenia w sposób potwierdzony. Zasady przechowywania
kopii przez wykonawcę, okres retencji oraz sposób wycofywania wersji nieaktualnych określa
zatwierdzona polityka bezpieczeństwa i dokumentacji. Kartę aktualizuje się przy każdej zmianie
hasła, numerów uprawnionych, obszaru albo wersji pakietu plików referencyjnych.

Karty **nie umieszcza się** w repozytoriach dokumentacji, w załącznikach do korespondencji
rozsyłanej ani w materiałach przekazywanych do publikacji.


---
