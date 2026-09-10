---
tytuł: "Załącznik nr 1 — Słownik pojęć"
wersja: "0.5"
data: 2026-09-10
status: "projekt wytycznych"
autor: Biuro Informatyki i Łączności Komendy Głównej Państwowej Straży Pożarnej
---

[← Powrót do podręcznika](../PODRECZNIK_v2_ROZDZIELONY.md#spis-treści)

# Załącznik nr 1 — Słownik pojęć

## System i odpowiedzialność

**SOiA / SOIA.KGPSP** — system ostrzegania i alarmowania obejmujący przygotowanie, dystrybucję i wykonanie poleceń oraz utrzymanie urządzeń. Decyzja o alarmowaniu wynika z właściwej procedury i uprawnień, a system ją wykonuje.

**ALARM.soia** — warstwa operacyjna dostępna pod adresem `alarm.soia.info`, publikująca komunikaty i podpisany IoT Feed. **SYRENY.soia** — warstwa operacyjnego zarządzania uruchamianiem syren pod adresem `syreny.soia.info`, w tym właściwe profile SMS. Relacje, uprawnienia i wersje integracji wskazuje KG PSP; same adresy nie potwierdzają uruchomienia każdej planowanej funkcji.

**Orchestra Manager** — techniczne zarządzanie urządzeniami: rejestracja, konfiguracja, stan, telemetria, dostęp i aktualizacje. Nie jest odrębnym źródłem decyzji alarmowej. **Orchestra SDN** — właściwa dla instancji droga kontrolowanej komunikacji zarządczej.

**Organ ochrony ludności** — organ podejmujący decyzje w granicach właściwości ustawowej. **Administrator KG PSP** — podmiot uprawniony do przyjęcia konfiguracji, rejestracji egzemplarza i nadania dostępu w określonym zakresie. **Właściciel instalacji** — podmiot odpowiedzialny za jej stan, eksploatację i dokumentację. **Wykonawca** — dostawca platformy, integracji lub montażu w zakresie zamówienia.

**PL-CAP** — profil komunikatu ostrzegawczego oparty na CAP. **IoT Feed** — podpisany, jednokierunkowy wykaz poleceń wykonawczych w profilu `PL-CAP-DIST-IOT`. Feed nie jest samym komunikatem CAP ani potwierdzeniem emisji.

## Platforma i przygotowanie urządzenia

**Sterownik** — urządzenie brzegowe z mikrokomputerem, tożsamością i systemem bazowym, na którym aplikacja KG PSP kwalifikuje polecenia i steruje lokalnym interfejsem. Może być osobnym modułem lub częścią zestawu. Modem i bramka nie są jego synonimami.

**OrchestraOS** — system bazowy używany w platformie KG PSP. **Yocto Project** — środowisko budowy systemu Linux dla określonego sprzętu. **BSP** — pakiet obsługi konkretnej płyty, jej rozruchu i urządzeń. Wykonawca buduje obraz ze wskazanego wydania komponentów udostępnionych przez KG PSP na wniosek.

**Provisioning** — przygotowanie egzemplarza: obraz, indywidualna tożsamość, konfiguracja startowa, rejestracja i przypisanie. **ZTP** — automatyzacja pierwszego przyłączenia dzięki wcześniejszemu przygotowaniu. Samo pojawienie się urządzenia w sieci nie nadaje mu zaufania.

**Przyjęcie modelu** — sprawdzenie konkretnej konfiguracji sprzętu i oprogramowania. **Rejestracja egzemplarza** — przyjęcie tożsamości konkretnej sztuki do właściwego środowiska. **Odbiór obiektu** — potwierdzenie funkcji w rzeczywistej instalacji. Są to odrębne etapy.

**Flota** — grupa zgodnych urządzeń używana do zarządzania. Nie wyznacza obszaru alarmowania. **Karta konfiguracji** — dokument modelu lub egzemplarza z wersjami, przypisaniem, portami i dowodami. Wypełniona karta i jej sekrety pozostają poza publikacją.

**Bramka LoRaWAN** — osobny element przekazujący ruch radiowy urządzeń końcowych do LNS. **LNS** — serwer sieci LoRaWAN. **CUPS** — usługa konfiguracji bramki. Żaden z tych elementów nie jest aplikacją interpretującą IoT Feed.

## Cztery niezależne osie doboru

| Pojęcie | Znaczenie |
| --- | --- |
| Klasa odbiorcy w komendzie | Do jakiej kategorii urządzenia jest skierowane polecenie, np. `SIREN_CONTROLLER`. |
| Klasa zdolności | I — rdzeń; 1.5 — profil kompaktowy z audio; II — rozszerzony z audio; III — lokalny TTS. Wymagania określa Z3. |
| Profil wykonawczy i tryb połączenia | Syrena elektroniczna, silnikowa lub inny odbiornik; AUDIO/PTT, API albo izolowane sterowanie stykowe. |
| Poziom podłączenia | 0 — odczyt publiczny; 1 — kanały rejestrowane; 2 — dodatkowe usługi wydzielone/SMS według profilu. |

Oznaczenie 1.5 nie jest wersją feedu ani poziomem rejestracji. Profil modernizacji oznacza adaptację instalacji istniejącej, nie osobny rodzaj dźwięku lub tożsamości urządzenia. Otwartość odczytu poziomu 0 nie jest potwierdzeniem zgodności platformy z Z3.

## Polecenie i efekt

**Komenda** — pojedyncze polecenie wykonawcze z tożsamością operacji. **Kod sygnału** — identyfikator funkcji określonej w kontrakcie, nie plik dźwiękowy. **Sygnał alarmowy** — przebieg określony w katalogu Z4 i właściwym przepisie.

**Plik referencyjny** — zatwierdzony zasób lokalny o określonej wersji i sumie. **Manifest pakietu audio** — wykaz plików, ich parametrów i skrótów powiązany z akceptacją KG PSP. Nie jest IoT Feed. Aktualizacja zasobów jest czynnością utrzymaniową, a wykonanie alarmu nie zależy od pobierania audio.

**TTS** — lokalne przekształcenie zatwierdzonego tekstu w mowę. Odtwarzanie gotowego nagrania nie jest TTS. Syrena silnikowa nie odtwarza ani plików, ani mowy.

**Okno rozpoczęcia** — czas, w którym można rozpocząć lokalną operację. Nie jest czasem trwania dźwięku ani ważnością całego ostrzeżenia. **Emisja** — fizyczne wytworzenie dźwięku; aktywacja wyjścia jest wcześniejszym, odrębnym etapem.

**CANCEL_PENDING** — anulowanie określonej, znanej akcji oczekującej zgodnie z kontraktem. Nie jest sygnałem odwołania i nie zatrzymuje emisji trwającej. **Odwołanie alarmu** — odrębna funkcja akustyczna, w profilu dla ludności sygnał ciągły 180 s. **Techniczne STOP** — funkcja właściwego kontraktu, jeśli została przewidziana i odebrana; nie zastępuje odwołania. **Odcięcie lokalne** — czynność sprzętowa o pierwszeństwie bezpieczeństwa. Dla silnika odcina napęd, lecz wirnik może jeszcze wybiegać.

**Arbitraż** — wspólne rozstrzygnięcie dostępu do tego samego toru. **Odrzucenie** kończy kwalifikację tej operacji. **Odroczenie** zachowuje operację do ponownej kwalifikacji na warunkach profilu. **Wynik niepewny** oznacza brak dowodu pozwalającego rozstrzygnąć, czy nastąpiło wykonanie; nie uprawnia do automatycznego ponowienia.

## Obszar i zaufanie

**TERYT** — krajowy rejestr podziału terytorialnego. **TERC** — kody jednostek: dwie cyfry województwa, cztery powiatu i siedem gminy. Tor konfiguruje się siedmiocyfrowym kodem gminy. Cyfra rodzaju jest znacząca; miasto i obszar wiejski gminy miejsko-wiejskiej nie są zamienne.

**Reguła zawierania** — geokod polecenia musi obejmować teren przypisany danemu torowi. Nie porównuje się w ten sposób kodów ulic ani miejscowości. Zasięg akustyczny nie rozszerza samodzielnie adresowania.

**Podpis feedu**, **indywidualna tożsamość urządzenia** oraz **zaufanie aktualizacji i rozruchu** są trzema odrębnymi domenami. Publiczne klucze weryfikacji mogą być wspólne; prywatnych kluczy i sekretów egzemplarzy nie współdzieli się. Nieznany klucz nie uzyskuje zaufania tylko przez wystąpienie w odebranej treści.

**Fail-closed** — niespełnienie warunków kwalifikacji powoduje brak nowego wykonania. **Świeżość** — ważność podpisanej treści i komendy. **Ochrona przed powtórzeniem** — trwała historia zapobiegająca ponownemu wykonaniu, także po restarcie i zmianie kanału.

**Potwierdzenie** — informacja o określonym etapie: przyjęciu, starcie, końcu lub błędzie. Doręczenie SMS, ACK, stan przekaźnika i pomiar akustyczny nie są tym samym. Numery nadawców i odbiorców statusu określa się oddzielnie.
