---
title: "Załącznik nr 1 — Słownik pojęć"
---

[← Powrót do podręcznika](../index.md#spis-tresci)

# Załącznik nr 1 — Słownik pojęć


Załącznik określa terminologię stosowaną w odniesieniu do SOiA. Nie obejmuje pojęć
ogólnotechnicznych; definiuje terminy mające w systemie znaczenie szczególne oraz terminy, których
zamienne używanie może prowadzić do niejednoznaczności.

Każdemu hasłu przypisano jedno znaczenie. Określenia niezalecane wskazano pod adnotacją
*Określenia niezalecane*. Pozostałe części dokumentu powinny stosować terminologię z niniejszego
załącznika.

---

## System i jego komponenty

W obszarze ostrzegania i alarmowania funkcjonują przedsięwzięcia o podobnych oznaczeniach.
Poniższe rozróżnienia służą zapewnieniu ich jednoznacznej identyfikacji.

**SOiA**
System ostrzegania i alarmowania — całość rozwiązania, obejmująca tworzenie komunikatu
ostrzegawczego, jego dystrybucję kanałami i wykonanie na urządzeniach w terenie.
*Określenia niezalecane*: „system syren”, „platforma alarmowa”.

**ALARM.soia**
System oparty na standardzie CAP, integrujący i publikujący komunikaty ostrzegawcze do urządzeń
IoT, telefonów, aplikacji i pozostałych kanałów. Jest jedynym miejscem, w którym powstaje polecenie
dla syreny. Działa według zasady **„jeden alert — wiele urządzeń naraz”**: uprawniona osoba wydaje
ostrzeżenie raz, a system zapewnia, że identyczna treść trafia jednocześnie do wszystkich kanałów.
Dostępny pod adresem `alarm.soia.info`, gdzie publikowana jest także jego dokumentacja.
*Określenia niezalecane*: `CAP_ALERT` — nazwa robocza z wcześniejszego etapu prac; `demo.soia.info` oraz
„serwer demonstracyjny” — **nazwy wycofane**, nadal obecne w starszych materiałach.

**ZKWSD.soia**
Zarządzanie Kryzysowe — System Wspomagania Decyzji SOiA. Odrębna aplikacja obiegu zdarzeń między
centrami zarządzania kryzysowego, w kaskadzie RCB → WCZK → PCZK/MCZK → GCZK → PSP.
**Nie jest to system sterowania syrenami** i te dwie nazwy nie są zamienne.
*Określenia niezalecane*: `SOiA-ALERT` — nazwa wycofana.

**Odbiorca komunikatu**
Kanał albo urządzenie, do którego trafia opublikowane ostrzeżenie: telefon przez wiadomość tekstową
i aplikację, komputer przez portal publiczny i strony, tablet, syrena alarmowa oraz urządzenia
z modułem sieciowym — domofony, tablice informacyjne, systemy radiowe, huby domowe, znaki zmiennej
treści i inne. Syrena jest **jednym z odbiorców**, a nie osobnym systemem.

**PL-CAP**
Krajowy profil interoperacyjności ostrzegania, oparty na standardzie OASIS CAP 1.2. Określa
format komunikatu ostrzegawczego, jego walidację i dystrybucję.

**IoT Feed**
Jednokierunkowy, podpisany wykaz poleceń wykonawczych, publikowany przez ALARM.soia i pobierany
przez sterowniki. Nie jest komunikatem CAP i nie jest dowodem, że alarmowanie faktycznie nastąpiło.

**`PL-CAP-DIST-IOT`**
Formalna nazwa profilu, w którym publikowany jest IoT Feed. Występuje w treści koperty i służy
sterownikowi do sprawdzenia, że rozmawia z właściwym kontraktem.

!!! note "PL-CAP, IoT Feed i urządzenie — dla odbiorcy nietechnicznego"

    PL-CAP opisuje ostrzeżenie przeznaczone do wielu kanałów. IoT Feed jest podpisanym wykazem poleceń dla urządzeń korzystających z toru danych. ALARM.soia publikuje Feed, a sterownik automatycznie go pobiera, weryfikuje i interpretuje; JST nie wykonuje tych czynności ręcznie. Obecność ostrzeżenia w części informacyjnej nie uruchamia syreny. Wykonanie następuje wyłącznie po dostarczeniu polecenia właściwym kanałem oraz jego kwalifikacji i weryfikacji przez urządzenie zgodnie z profilem tego kanału.

---

## Uczestnicy i zakresy odpowiedzialności

**Organ ochrony ludności**
Organ właściwy do ogłoszenia alarmu w rozumieniu ustawy o ochronie ludności i obronie cywilnej —
w szczególności wójt, burmistrz, prezydent miasta, starosta i wojewoda. To on ogłasza alarm;
system jedynie przenosi jego decyzję.

**Administrator SOiA**
Osoba lub komórka rozstrzygająca o dopuszczeniu **każdego zgłoszonego urządzenia z osobna** do
kanałów zamkniętych, przydzielająca tożsamość, kartę abonencką i numer. Decyzja administratora nie
jest czynnością techniczną i nie następuje automatycznie po złożeniu zgłoszenia.

**Przystąpienie**
Zgłoszenie urządzenia do rejestracji — chwila, od której podmiot stosuje Wytyczne w całości.
Do tego momentu urządzenie pobierające publiczny wykaz poleceń jest odbiorcą informacji
udostępnianej powszechnie. Stosowanie Wytycznych jest dobrowolne; przystąpienie nie jest.
*Określenia niezalecane*: „podłączenie” w znaczeniu prawnym — podłączyć można się bez przystąpienia.

**Profil gminy**
Konto zakładane jednostce samorządu terytorialnego, w którym rejestruje ona własne urządzenia.
Porządkuje wnioski i wiąże je z podmiotem odpowiedzialnym; **nie zastępuje decyzji** administratora
o dopuszczeniu pojedynczego urządzenia.

**Właściciel urządzenia**
Podmiot odpowiadający za instalację, jej stan techniczny i skutki działania — jednostka samorządu
terytorialnego, jednostka ochrony przeciwpożarowej, zakład pracy albo osoba prywatna.

**Wykonawca**
Podmiot montujący i uruchamiający instalację. Może być tożsamy z producentem sterownika, ale
nie musi.

---

## Urządzenia i elementy instalacji

**Punkt alarmowy**
Miejsce, w którym zainstalowano syrenę wraz z jej sterownikiem i zasilaniem. Jeden punkt alarmowy
może obejmować więcej niż jedną syrenę.

**Syrena**
Urządzenie wytwarzające sygnał akustyczny. Sama nie podejmuje decyzji.

**Sterownik**
Warstwa pośrednia między SOiA a syreną: odbiera polecenia dowolnym kanałem, weryfikuje je,
prowadzi własną maszynę stanów i uruchamia wyjście wykonawcze. To sterownik, a nie system
centralny, wie, jak fizycznie uruchomić daną syrenę.
*Określenia niezalecane*: „moduł GSM”, „bramka” — to elementy sterownika, nie jego synonimy.

**Bramka**
Urządzenie pośredniczące w transmisji — w kanale SMS przyjmuje komendę i przekazuje ją do
sterownika. Nie interpretuje treści polecenia.

**Profil sterownika**
Sposób, w jaki sterownik zamienia znaczenie polecenia na fizyczne działanie. Wyróżnia się profil
**elektroniczny** (odtworzenie pliku dźwiękowego przez wzmacniacz), **silnikowy** (sterowanie
układem wykonawczym syreny mechanicznej) oraz **modernizacyjny (retrofit)** (dołączenie kanału SOiA
do istniejącej instalacji przez adapter).

**Klasa urządzenia**
Kategoria **odbiorcy polecenia**, zapisana w treści IoT Feed. Sterownik wykonuje wyłącznie polecenia
skierowane do jego klasy.

**Klasa zdolności**
Zakres wymagań, którym urządzenie podlega — **klasa I** (rdzeń, obowiązuje zawsze), **klasa II**
(tor audio, gdy sterownik sam odtwarza dźwięk), **klasa III** (profil głosowy, opcjonalna).
Zamawiający wskazuje w zamówieniu klasy zdolności, których wymaga.

!!! warning "Rozróżnienie pojęć"

    *Klasa urządzenia* określa, **do kogo** skierowane
    jest polecenie, i wynika z kontraktu. *Klasa zdolności* określa, **jakich zdolności wymaga się** od urządzenia,
    i wynika z Wytycznych. Terminu „klasa” nie należy używać bez właściwego określenia.

**Poziom podłączenia**
Zakres kanałów, którymi urządzenie łączy się z SOiA. **Poziom 0** to publiczny IoT Feed bez
rejestracji, **poziom 1** dokłada kanał niezwłocznego powiadomienia po dopuszczeniu przez administratora,
**poziom 2** dokłada prywatną sieć APN i kanał SMS. Poziomy są **kumulatywne**: wyższy dokłada
kanał, nie zastępuje niższego.
*Określenia niezalecane*: „tryb podstawowy/rozszerzony” — sugeruje, że jeden wyklucza drugi.

**Karta konfiguracji**
Dokument przekazywany instalatorowi, zawierający wartości właściwe dla jednej instalacji: numery,
hasło sterujące, mapę komend i identyfikator urządzenia. Nie jest publikowany i nie stanowi
części dokumentacji rozsyłanej.

---

## Polecenia wykonawcze, sygnały alarmowe i emisja

Poniższe pojęcia rozróżniają czynności, które w języku potocznym mogą być określane zbiorczo jako
„włączenie syreny”. Ich konsekwentne stosowanie jest wymagane przy przygotowaniu zamówienia
i implementacji.

**Komenda**
Pojedyncze polecenie wykonawcze w IoT Feed, opatrzone własnym identyfikatorem. Komenda **nie jest
alarmem** — jest technicznym poleceniem wynikającym z alarmu ogłoszonego przez organ.

**Kod sygnału**
Symbol wskazujący, **który** sygnał akustyczny ma zabrzmieć. Kod nie zawiera dźwięku ani jego
parametrów — wskazuje pozycję w katalogu sygnałów.

**Sygnał alarmowy**
Dźwięk o strukturze i czasie trwania określonym w rozporządzeniu o alarmach i komunikatach
ostrzegawczych. Rozporządzenie określa cztery: ogłoszenie alarmu dla ludności cywilnej, odwołanie
alarmu, alarm dla jednostki ochrony przeciwpożarowej oraz alarm ćwiczebny lub treningowy.

Urządzenie MUSI umieć wyemitować **wszystkie cztery**. System wydaje obecnie wyłącznie sygnały
skierowane **do ludności**; alarm dla jednostki ochrony przeciwpożarowej pozostaje poza obecnym
zakresem SOiA i jest wywoływany dotychczasowymi środkami. Zdolność urządzenia i zakres usługi
to dwie różne rzeczy.

**Plik referencyjny**
Wzorcowy plik dźwiękowy zatwierdzony przez KG PSP, opatrzony sumą kontrolną. Jedyna obowiązująca
postać sygnału; modyfikacja brzmienia, długości lub struktury jest niedopuszczalna.

**System nie przenosi plików referencyjnych.** Udostępnia się je do pobrania na stronie SOiA,
a wgrywa **przy instalacji**. Źródłem rozstrzygającym dla sumy kontrolnej są Wytyczne z dnia
28 maja 2025 r. — dokument podpisany, a nie strona internetowa, z której plik pobrano.

**Emisja**
Pojedyncze, konkretne odtworzenie sygnału przez syrenę — od załączenia wyjścia do jego wyłączenia.
Jedna komenda oznacza **jedną** emisję. Emisja kończy się sama, po czasie wynikającym z sygnału.

**Okno rozpoczęcia**
Przedział czasu, w którym wolno rozpocząć emisję. Poza tym oknem sterownik nie uruchamia syreny,
nawet jeśli alarm nadal obowiązuje. Czas obowiązywania alarmu, okno rozpoczęcia i czas emisji
to **trzy różne rzeczy**. Obowiązująca długość okna publikowana jest maszynowo pod adresem
produkcyjnym (§ 4 ust. 2 aktu); od niej wyprowadzony jest próg dryfu zegara z W-A13.

**Odwołanie akcji nierozpoczętej**
Polecenie „nie zaczynaj”, skuteczne wyłącznie wobec emisji, która jeszcze się nie rozpoczęła.
Nie zatrzymuje emisji trwającej.
*Określenie niezalecane*: „stop”. Jest to operacja odrębna od zatrzymania emisji.

**Odwołanie alarmu**
Prawnie określony **sygnał akustyczny** oznaczający koniec zagrożenia: ciągły dźwięk syreny
trwający trzy minuty. Odwołanie alarmu jest **emisją, nie ciszą** — to jedno z najczęstszych
nieporozumień w tym obszarze.

**Zatrzymanie emisji**
Polecenie „przerwij trwający sygnał”, wydane z systemu. **Nie istnieje** — żaden kanał go nie
przenosi. Rozpoczęta sekwencja wykonuje się do końca; sprawdzono to na urządzeniu, a właściwość tę
przyjęto jako wymaganie.
*Określenia niezalecane*: „STOP”, „stop zdalny” — sugerują istnienie polecenia, którego nie ma.

**Odcięcie lokalne**
Czynność **na obiekcie**, przerywająca tor wykonawczy niezależnie od łączności i od oprogramowania:
element obsługowy, rozłącznik albo odjęcie zasilania. Ma pierwszeństwo przed poleceniem zdalnym
i jest wymagane niezależnie od kanału.

Rozróżnienie jest wiążące: **zatrzymania nie ma, odcięcie jest zawsze.** Pierwsze byłoby funkcją
systemu, drugie jest uprawnieniem człowieka stojącego przy urządzeniu.

**Zakończenie emisji**
Naturalne wygaśnięcie sygnału po upływie jego czasu. Nie wymaga żadnego polecenia i nie jest
zdarzeniem sterowanym z zewnątrz.

---

## Obszar działania i reguły przypisania terytorialnego

**TERYT**
Krajowy rejestr podziału terytorialnego. W SOiA stosuje się wyłącznie kody jednostek podziału
(TERC): dwie cyfry oznaczają województwo, cztery powiat, siedem gminę.

**Cyfra rodzaju**
Siódma cyfra kodu gminy, rozróżniająca gminę miejską, wiejską i miejsko-wiejską oraz — w tej
ostatniej — samo miasto i sam obszar wiejski. Jest **znacząca**: dwa kody o wspólnych sześciu
cyfrach mogą opisywać tereny rozłączne.

**Reguła zawierania**
Zasada rozstrzygająca, czy polecenie dotyczy danego urządzenia: kod obszaru w poleceniu musi być
równy kodowi urządzenia albo wobec niego nadrzędny. Zależność w drugą stronę nie wystarcza —
ostrzeżenie dla jednej gminy nie uruchamia syreny opisanej kodem całego powiatu.

**Obszar urządzenia**
Lista **siedmiocyfrowych** kodów gmin, na których syrena fizycznie oddziałuje. Konfiguracja kodem
województwa lub powiatu jest niedopuszczalna i musi zostać przez sterownik odrzucona albo
zgłoszona jako błąd — urządzenie tak skonfigurowane pominie alerty rysowane po jego terenie.

---

## Model zaufania i zasady weryfikacji

Model zaufania SOiA opiera się na jednej zasadzie: **sam fakt, że wiadomość dotarła zaufaną
drogą, nie uprawnia do uruchomienia syreny.** Uprawnia dopiero zweryfikowana treść.

**Podpis**
Kryptograficzne potwierdzenie, że treść IoT Feed pochodzi z ALARM.soia i nie została zmieniona po
drodze. Szyfrowanie połączenia go nie zastępuje.

**Identyfikator klucza**
Oznaczenie klucza użytego do podpisu, pozwalające sterownikowi wybrać właściwy klucz publiczny
i przejść wymianę klucza bez przerwy w działaniu. Nieznany identyfikator powoduje odmowę
wykonania polecenia.

**Świeżość**
Termin ważności treści IoT Feed. Po jego upływie sterownik nie wykonuje żadnego zawartego tam
polecenia, choćby połączenie działało poprawnie.

**Ochrona przed powtórzeniem**
Mechanizm gwarantujący, że to samo polecenie — odebrane ponownie, innym kanałem albo po restarcie
urządzenia — nie spowoduje drugiej emisji. Musi przetrwać zanik zasilania.

**Fail-closed**
Zasada, według której każda wątpliwość skutkuje **niewykonaniem** polecenia. Nierozpoznany kod
obszaru, nieznany identyfikator klucza, przeterminowana treść, niepełny format — każde z nich
oznacza brak emisji. Niedopuszczalne jest wykonanie polecenia na podstawie domniemania.

**Klucz podpisujący**
Klucz, którym system podpisuje wydawaną treść. Jest **jeden**, pozostaje po stronie KG PSP i nigdy
nie trafia do urządzenia. Nie należy go mylić z **tożsamością urządzenia**, która jest indywidualna
dla każdego egzemplarza i którą urządzenie dowodzi, kim jest.

**Źródło czasu**
Zewnętrzne odniesienie służące do synchronizacji zegara urządzenia. Projekt wskazuje państwowe
serwery czasu jako źródło podstawowe i wymaga co najmniej dwóch niezależnych źródeł. Nawigacja
satelitarna może stanowić źródło uzupełniające.

**Dryf**
Rozbieżność zegara urządzenia wobec czasu odniesienia. Po przekroczeniu progu urządzenie odmawia
wykonania polecenia, ponieważ ocena okna rozpoczęcia zależy od wiarygodnego czasu urządzenia.

**Niezwłoczność**
Obowiązująca miara czasu od wydania polecenia do rozpoczęcia emisji: najszybciej, jak jest to
technicznie możliwe. **Progu liczbowego nie ustanowiono**, ponieważ nie istnieje norma, z której
dałoby się go wyprowadzić; czas mierzy się przy odbiorze i zapisuje bez oceny.

**Zamknięta grupa abonencka**
Grupa numerów w sieci operatora — ruch odbywa się wyłącznie między numerami
należącymi do grupy. Ogranicza, kto może wysłać wiadomość; nie potwierdza, kto ją wysłał.

**Hasło sterujące**
Ciąg poprzedzający komendę SMS, weryfikowany przez urządzenie. Zabezpiecza przed skutkiem
wiadomości wysłanej omyłkowo wewnątrz grupy. Nie jest podpisem.

**Numery uprawnione**
Wykaz numerów uprawnionych do wydania komendy danemu urządzeniu i otrzymujących potwierdzenia.
*Określenia niezalecane*: „lista zaufanych”, „numery autoryzowane” — sugeruje zaufanie szersze niż uprawnienie do jednej syreny.

**Potwierdzenie**
Wiadomość zwrotna urządzenia. Rozróżnia się **przyjęcie komendy** i **wykonanie** — są to dwa różne
zdarzenia i żadne z nich nie dowodzi, że sygnał był słyszalny.

---

!!! note "Trzy domeny zaufania"

    W dokumencie występują trzy odrębne domeny zaufania. W pierwszej `keyId` wskazuje właściwy klucz podpisujący. Klucz podpisujący pozostaje po stronie podpisującej, a odpowiadający mu klucz publiczny służy urządzeniu do weryfikacji podpisu IoT Feed. Indywidualna tożsamość urządzenia służy do rozpoznawania go w kanałach zamkniętych. Klucze aktualizacji i bezpiecznego rozruchu chronią oprogramowanie urządzenia. Tych domen nie należy łączyć ani używać zamiennie.

## Terminologia wycofana

Poniższe określenia pojawiają się w starszych materiałach i nie należy ich używać.

**„Alarm główny”, „alarm OSP”**
Nazewnictwo z uchylonego rozporządzenia z 2013 r. Obowiązujące nazwy to „alarm dla ludności
cywilnej” i „alarm dla jednostki ochrony przeciwpożarowej”.

**`demo.soia.info`, „serwer demonstracyjny”**
Wcześniejsze oznaczenie adresu produkcyjnego. Obowiązuje `alarm.soia.info`.

**„Manifest audio”, „podpisany wykaz plików referencyjnych”**
Pojęcie z wcześniejszego etapu prac, gdy zakładano, że system będzie rozprowadzał zawartość
dźwiękową. **Nie powstało i nie powstanie** — system przenosi polecenie, nie dźwięk.

**„STOP”, „stop zdalny”, „polecenie zatrzymania”**
Sugerują istnienie funkcji, której nie ma. Zobacz **Zatrzymanie emisji** i **Odcięcie lokalne**.

**„Syrena podłączona do systemu producenta”**
Nie jest to poziom podłączenia do SOiA. Urządzenie sterowane wyłącznie z platformy producenta
pozostaje poza systemem, dopóki nie odbiera i nie weryfikuje poleceń SOiA którymś z opisanych
kanałów.


---
