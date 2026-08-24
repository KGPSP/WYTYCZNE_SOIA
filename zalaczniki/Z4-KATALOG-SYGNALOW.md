---
tytuł: "Załącznik nr 4 — Katalog sygnałów i plików referencyjnych"
dokument: "Podręcznik podłączania syren alarmowych i innych urządzeń do SOiA"
wersja: 0.4
data: 2026-08-23
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
źródło: "Wydzielono z PODRECZNIK_v2.md"
---

[← Powrót do podręcznika](../PODRECZNIK_v2.md#spis-treści)

# Załącznik nr 4 — Katalog sygnałów i plików referencyjnych


## Cel i zakres załącznika

W obiegu funkcjonują trzy sposoby oznaczania tego samego dźwięku: opis w rozporządzeniu, nazwa
pliku referencyjnego i kod stosowany w kanałach technicznych. Załącznik przedstawia ich
jednoznaczne powiązanie, w tym równoważność oznaczeń „modulowany trzy minuty”,
`1_alarm_ludnosci.wav` i `SIREN_ALARM_MODULATED_3M`.

Załącznik jest też jedynym miejscem, w którym te powiązania są zapisane w tekście. Wartości
maszynowe — wykaz plików, sumy kontrolne, wersje — publikowane są pod adresem produkcyjnym SOiA
i to one są rozstrzygające przy wdrożeniu.

---

## Cztery sygnały akustyczne

Rozporządzenie Ministra Spraw Wewnętrznych i Administracji z dnia 14 maja 2025 r. w sprawie alarmów
i komunikatów ostrzegawczych określa w załączniku cztery sygnały akustyczne syreny. Nie ma ich
więcej i nie wolno tworzyć własnych.

**Alarm dla ludności cywilnej — ogłoszenie.** Modulowany dźwięk syreny alarmowej trwający trzy
minuty. To jest jeden z sygnałów skierowanych do ludności
i wyzwalanych centralnie.

**Alarm dla ludności cywilnej — odwołanie.** Ciągły dźwięk syreny alarmowej trwający trzy minuty.
Rozporządzenie umieszcza go w kolumnie „odwołanie alarmu”, co bywa źródłem nieporozumienia:
odwołanie alarmu **jest emisją dźwięku, a nie jej zaprzestaniem**. Cisza nie odwołuje niczego.

**Alarm dla jednostki ochrony przeciwpożarowej.** Trzykrotnie wzrastający i opadający dźwięk syreny
z przerwami trzydziestosekundowymi, łącznie trzy minuty. Służy do wezwania strażaków, a nie do
ostrzegania ludności — to inny odbiorca i inne uprawnienie do uruchomienia.

**Alarm ćwiczebny lub treningowy.** Ciągły dźwięk syreny trwający jedną minutę. Różni się od odwołania
alarmu **wyłącznie czasem trwania** — jedna minuta zamiast trzech. Jest to najłatwiejsza do pomylenia
para w całym katalogu i warto o tym pamiętać przy konfiguracji urządzenia.

Rozporządzenie dopuszcza obok sygnału akustycznego zapowiedź słowną powtarzaną trzykrotnie, oraz
odrębnie sygnał wizualny w postaci żółtego trójkąta. Kontrakt SOiA nie przenosi dziś treści słownej,
a sygnalizacja wizualna pozostaje poza zakresem Wytycznych.

---

## Pliki referencyjne

Wytyczne Komendanta Głównego Państwowej Straży Pożarnej z dnia 28 maja 2025 r. w sprawie
przygotowania, dystrybucji oraz eksploatacji cyfrowych sygnałów alarmowych syren ustanawiają dla
każdego z czterech sygnałów **plik wzorcowy**, opatrzony sumą kontrolną. Pliki te są jedyną
obowiązującą postacią sygnału.

Wszystkie mają format **WAV PCM 16 bit mono** przy próbkowaniu **8 kHz**. Urządzenie musi obsłużyć
ten format; wyższe próbkowanie jest dopuszczalne, niższe nie.

| Sygnał | Plik | Czas | Struktura | Charakterystyka |
|---|---|---|---|---|
| Ogłoszenie alarmu — ludność cywilna | `1_alarm_ludnosci.wav` | 180 s | ciąg przebiegów wzrastająco-opadających, bez przerw | okres przebiegu ok. 5 s, pasmo modulacji ok. 350–900 Hz |
| Alarm dla jednostki ochrony ppoż. | `2_alarm_osp.wav` | 180 s | trzy bloki przebiegu rozdzielone przerwami 30 s | okres przebiegu ok. 5 s, pasmo ok. 350–900 Hz |
| Alarm ćwiczebny lub treningowy | `3_alarm_cwiczebny.wav` | 60 s | dźwięk ciągły | ton ok. 600 Hz, dopuszczalnie 550–650 Hz |
| Odwołanie alarmu — ludność cywilna | `4_odwolanie_alarmu.wav` | 180 s | dźwięk ciągły | ton ok. 600 Hz, dopuszczalnie 550–650 Hz |

Wartości pasma i częstotliwości są poglądowe, z dopuszczalnym odchyleniem ±15 %. Wiążące są:
**czas trwania w tolerancji ±5 %** oraz **struktura czasowa** — modulacja oraz liczba i długość
przerw. Poziom na wyjściu wzmacniacza musi mieścić się w granicach **±3 dB** względem wzorca,
bez przesterowania.

### Sumy kontrolne

Wartości sum kontrolnych są zgodne z wykazem opublikowanym wraz z pakietem. Instalacja pliku
o niezgodnej sumie jest niedopuszczalna.

| Plik | SHA-256 |
|---|---|
| `1_alarm_ludnosci.wav` | `1b5f5ef4223c6bcffb9205f7bba82d1349ba928fbcaac50978e5d8a90763dcfa` |
| `2_alarm_osp.wav` | `6940ec902ba5e81b708a0d3f717200872d79b6e5ad427cc46adec55d78c23cd5` |
| `3_alarm_cwiczebny.wav` | `16e84498292a743e44b3622b8626e5fe21b0c243f7e1f52d8e438c4123f67a0e` |
| `4_odwolanie_alarmu.wav` | `4049bb3792210fcfd682bcbe2a7d512a310c4c0b7ca6a3e57851ec0203d7df63` |

**Źródłem rozstrzygającym są Wytyczne KG PSP z dnia 28 maja 2025 r.** — dokument podpisany,
a nie strona internetowa, z której plik pobrano. Podmiana zawartości strony niczego nie daje,
dopóki instalator porównuje sumę z Wytycznymi. Wartości przytoczono tu dla wygody; przy rozbieżności
obowiązują Wytyczne.

---

## Sposoby pozyskania plików referencyjnych

Pliki referencyjne są udostępniane dwiema drogami, które prowadzą do tego samego materiału.

**Dla podmiotów publicznych — kaskadą.** W trybie określonym w § 4 Wytycznych z 28 maja 2025 r.:
Komenda Główna PSP udostępnia pakiet komendantom wojewódzkim, ci właściwym organom ochrony ludności,
podmiotom ochrony przeciwpożarowej oraz innym podmiotom prowadzącym systemy ostrzegania.

**Dla wszystkich pozostałych — publicznie, do pobrania ze strony.** Pliki wraz z opisem, czasem
trwania i sumami kontrolnymi są dostępne na `soia.info` w miejscu przeznaczonym do pobrania przez
człowieka.

**System nie przenosi plików.** Nie ma podpisanego wykazu audio ani punktu dostępu, z którego
sterownik pobierałby dźwięk — polecenie wskazuje sygnał, a plik jest już w urządzeniu, wgrany
**przy instalacji**, dokładnie tak, jak robiono to dotychczas. W instalacji, w której pliki
znajdują się w pamięci samej syreny, wgrywa je wykonawca syreny albo sterownika.

Rozwiązanie to wynika z otwartości poziomu zerowego: skoro dowolny podmiot może odebrać polecenie
i wyemitować sygnał, musi też mieć legalną drogę do materiału wzorcowego. Bez tego powstałyby
dźwięki wymyślone samodzielnie — czyli dokładnie ta rozbieżność, której Wytyczne z 2025 r. miały
zapobiec.

Niezależnie od drogi pozyskania obowiązuje ta sama zasada: **przed instalacją pliku należy
potwierdzić zgodność jego sumy kontrolnej**.

---

## Powiązanie z kodami technicznymi

Ten sam sygnał występuje w kanałach SOiA pod dwiema postaciami: jako kod sygnału w podpisanym
wykazie poleceń oraz jako cyfra komendy w kanale wiadomości tekstowych. Poniższa tabela jest
jedynym miejscem, w którym te trzy światy są zestawione.

| Sygnał | Plik referencyjny | Kod sygnału | Komenda SMS |
|---|---|---|---|
| Ogłoszenie alarmu — ludność cywilna | `1_alarm_ludnosci.wav` | `SIREN_ALARM_MODULATED_3M` | `*1` |
| Odwołanie alarmu — ludność cywilna | `4_odwolanie_alarmu.wav` | `SIREN_ALL_CLEAR_STEADY_3M` | `*3` |
| Alarm dla jednostki ochrony ppoż. *(poza obecną fazą)* | `2_alarm_osp.wav` | `SIREN_JOP_CALLOUT_3M` | `*5` |
| Alarm ćwiczebny lub treningowy | `3_alarm_cwiczebny.wav` | `SIREN_EXERCISE_STEADY_1M` | `*7` |

Kody sygnałów obowiązują od wersji słownika **2026.2**. Urządzenie sprawdza wersję słownika przy
każdym pobraniu wykazu i **odrzuca nieznany kod, nie przerywając obsługi pozostałych poleceń** —
inaczej rozszerzenie katalogu wyłączyłoby starsze urządzenia w terenie.

### Rozróżnienie słownika kodów i uprawnień do wydania sygnału

Należy rozróżnić zakres słownika kodów od uprawnienia do wydawania sygnałów. Słownik określa kody,
które mogą wystąpić w kontrakcie i które urządzenie MUSI obsługiwać ze względu na przewidywany
wieloletni okres eksploatacji. Uprawnienie do wydania sygnału stanowi odrębną decyzję operacyjną.

Ujęcie kodu sygnału wywołania jednostki ochrony przeciwpożarowej w słowniku 2026.2 nie oznacza
nadania uprawnienia do jego wydania. SOiA służy obecnie ostrzeganiu ludności, a funkcja wywoływania
jednostek pozostaje niedostępna w interfejsie operatorskim do czasu wdrożenia odrębnego etapu.

Cyfry komend należą do **profilu bazowego kanału wiadomości tekstowych**, który jest wersjonowany
i będzie się zmieniał wraz z profilami kolejnych producentów. Wiążąca jest struktura powiązania,
a nie konkretne brzmienie cyfry; obowiązujące wartości dla danej instalacji zapisuje się w karcie
konfiguracji.

---

## Czynności i polecenia niebędące sygnałami akustycznymi

Dwa pojęcia bywają wciągane do katalogu, a do niego nie należą, bo nie odpowiada im żaden dźwięk.

**Odwołanie akcji nierozpoczętej** to polecenie „nie zaczynaj”, skuteczne wyłącznie wobec emisji,
która jeszcze nie ruszyła. Nie ma pliku, nie ma dźwięku i nie zatrzymuje niczego, co już trwa.

**Zatrzymanie emisji** nie występuje w żadnym kanale i nie istnieje jako polecenie. Rozpoczęta
sekwencja wykonuje się do końca — sprawdzono to na urządzeniu i nie da się jej przerwać inaczej
niż odjęciem zasilania. Co najmniej jedna pełna sekwencja zabrzmi zawsze, niezależnie od tego,
co zostanie wysłane po jej rozpoczęciu.

Czym innym jest **odcięcie lokalne**: czynność na obiekcie, wykonywana na obwodzie wykonawczym,
niezależna od łączności i od oprogramowania. Zatrzymania nie ma, odcięcie jest zawsze.

Jeżeli alarm ogłoszono omyłkowo po rozpoczęciu emisji, sekwencja trwa przez pełny czas właściwy
dla danego sygnału. Działaniem operacyjnym jest odwołanie alarmu, czyli odrębna emisja sygnału
ciągłego przez trzy minuty.

---

## Wersjonowanie

W obiegu są dwie niezależne wersje i nie wolno ich mylić.

**Wersja pakietu plików referencyjnych**, w formacie `v.RRRRMMDD`, zgodnie z § 3 ust. 2 Wytycznych
z 28 maja 2025 r. Zmienia się, gdy zmienia się materiał dźwiękowy. Każda nowa wersja otrzymuje
protokół zmian, a urządzenie powinno umieć pobrać nowy pakiet bez wizyty serwisowej.

**Wersja słownika kodów**, obecnie `2026.2`. Zmienia się, gdy dochodzi nowy kod sygnału albo zmienia
się znaczenie istniejącego. Każda zmiana wymaga przeglądu zgodności urządzeń już zainstalowanych.

Zmiana jednej z tych wersji nie pociąga automatycznie zmiany drugiej.

> [!caution] Wymaga decyzji przed akceptacją — aktualizacja pakietu audio
> IoT Feed nie przenosi plików dźwiękowych. Jeżeli urządzenie ma później pobierać nową wersję pakietu bez wizyty serwisowej, trzeba odrębnie wskazać kanał dystrybucji, źródło zaufania, kontrolę integralności, zasady wersjonowania i sposób potwierdzenia instalacji. Do czasu tej decyzji nie należy utożsamiać aktualizacji pakietu z cyklicznym pobieraniem Feedu.

---

## Sprawdzenie okresowe

Zgodność brzmienia potwierdza się **testem odsłuchowym wykonywanym nie rzadziej niż raz na
dwanaście miesięcy** oraz po każdej modernizacji sterownika, w trybie i na wzorze protokołu
określonym w Wytycznych z 28 maja 2025 r. Test obejmuje odtworzenie każdego pliku w trybie lokalnym,
pomiar czasu trwania i potwierdzenie struktury sygnału.

Stwierdzenie rozbieżności czasu trwania przekraczającej 5 % albo zmiany struktury sygnału powoduje
**wyłączenie syreny z eksploatacji** do czasu ponownego wgrania pliku wzorcowego.

---

## Rozbieżności stwierdzone w materiale źródłowym

W Wytycznych z 28 maja 2025 r. występują dwie niezgodności wewnętrzne dotyczące pliku
`2_alarm_osp.wav`. Tabela w § 2 opisuje jego strukturę jako „ciągły x 30 s”, podczas gdy Karta
referencyjna w tym samym dokumencie oraz brzmienie rozporządzenia wskazują trzy bloki wzrastająco-
-opadające rozdzielone przerwami trzydziestosekundowymi. Maksymalna amplituda tego pliku podana
jest w jednym miejscu jako 0,9438, w drugim jako 0,7977.

W niniejszym załączniku przyjęto brzmienie zgodne z rozporządzeniem i Kartą referencyjną.
Rozstrzygnięcie rozbieżności w dokumencie źródłowym wymaga erraty i pozostaje poza zakresem
Wytycznych o podłączaniu syren.


---
