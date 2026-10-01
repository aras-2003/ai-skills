Uruchomiłem workflow `oaf-operating-model-redesign` w zakresie, który da się obronić na podstawie dostępnych capability.

## 1. Diagnoza

### Fakty

- Problem występuje na styku produktu, sprzedaży i IT.
- Handoffy są niejasne.
- Odpowiedzialność ginie między jednostkami.
- Decyzje eskalują między dyrektorami.
- Dane pozwalają opisać objawy, ale nie zawierają osobnej analizy interfejsów organizacyjnych.

### Hipotezy, których nie należy jeszcze traktować jako potwierdzonych

- Brak jednoznacznych kryteriów wejścia/wyjścia dla handoffów.
- Odpowiedzialność nie jest powiązana z realną władzą nad priorytetami, capacity lub zależnościami.
- Eskalacje pełnią funkcję zastępczego mechanizmu decyzyjnego.
- Możliwe są równoległe lub ukryte weta między funkcjami.

Brakujący `organizational-interface-review` jest niedostępny w tej sesji. Nie symuluję jego wykonania, dlatego przyczyny interfejsowe pozostają hipotezami.

## 2. Zasady projektowe

- Jeden jawny owner dla każdej materialnej decyzji i każdego kluczowego handoffu.
- Konsultacja nie oznacza prawa weta.
- Eskalacja musi mieć określony trigger, adresata, termin i zakres decyzji.
- Odpowiedzialność musi iść w parze z authority, capacity i kontrolą zależności.
- Produkt, sprzedaż i IT powinny zachować autonomię wykonawczą tam, gdzie liczy się kontekst i szybkość.
- Spójność enterprise należy wymuszać tylko dla obszarów takich jak architektura, bezpieczeństwo, ryzyko, interoperacyjność i zobowiązania wobec klienta.

## 3. Ograniczone opcje redesignu

| Opcja | Zakres | Korzyść | Główne ryzyko |
|---|---|---|---|
| A. Minimalna korekta interfejsów | Ustalenie kontraktów handoffów, ownerów decyzji, kryteriów akceptacji i ścieżki eskalacji | Najmniejsza ingerencja; odwracalny pilot | Nie rozwiąże problemu, jeśli przyczyną jest brak capacity lub realnej władzy |
| B. Cross-functional value stream | Wspólny mechanizm prowadzenia inicjatyw produktu–sprzedaży–IT z jednym ownerem rezultatu i uzgodnionym capacity | Lepsza odpowiedzialność end-to-end i mniej przekazań | Wymaga realnego mandatu i alokacji zasobów |
| C. Silniejsza centralizacja decyzji | Centralny portfel/prioritization forum z większą władzą nad priorytetami i zależnościami | Może ograniczyć konflikty między jednostkami | Ryzyko zwiększenia kolejek i kolejnego poziomu eskalacji |

## 4. Kierunek

Nie ma jeszcze wystarczających dowodów do wyboru docelowego modelu.

Do czasu zebrania danych należy utrzymać Opcję A jako preferowany, niskiego ryzyka kierunek pilotażowy. Nie oznacza to wyboru docelowego operating modelu. Opcja B powinna pozostać realną alternatywą, jeśli okaże się, że problem wynika z rozproszonej odpowiedzialności i braku wspólnego capacity. Opcję C należy traktować jako wariant rezerwowy, nie jako domyślną odpowiedź.

## 5. Najważniejsze decyzje do zbadania

Nie przypisuję nowych właścicieli, ponieważ formalne i faktyczne ownership nie zostały udokumentowane.

Należy prześledzić kilka ostatnich przypadków dla tych klas decyzji:

- priorytetyzacja inicjatyw między produktem, sprzedażą i IT;
- przyjęcie inicjatywy przez kolejną jednostkę;
- zmiana zakresu lub terminu po przekazaniu;
- decyzja o wyjątku wobec standardowej ścieżki;
- alokacja capacity przy konflikcie priorytetów.

Dla każdej decyzji trzeba ustalić:

- formalnego ownera;
- faktycznego decydenta;
- proponującego;
- doradców;
- wykonawcę;
- ścieżkę eskalacji;
- punkty oczekiwania, reworku i niejawnego weta;
- dostępne authority i capacity.

## 6. Minimalny pilot walidacyjny

Przeprowadzić pilotaż na jednym powtarzalnym strumieniu produktu–sprzedaży–IT:

1. wybrać 3–5 niedawnych przypadków;
2. odtworzyć formalną i faktyczną ścieżkę;
3. zdefiniować ownera oraz kryteria wejścia/wyjścia handoffu;
4. ustalić timebox eskalacji;
5. rozdzielić decyzję, konsultację i wykonanie;
6. porównać liczbę przekazań, eskalacji, reworku i czasu oczekiwania przed oraz po zmianie.

Nie należy jeszcze projektować pełnego governance ani transformacji enterprise.

## Następny krok workflow

Najpierw potrzebna jest reprezentatywna analiza interfejsów organizacyjnych. Następnie można zastosować:

1. `decision-rights-review` dla potwierdzonych klas decyzji;
2. `decision-bottleneck-analysis` dla decyzji z rzeczywistą latencją;
3. dopiero po wyborze kierunku — `governance-design`;
4. `transformation-blueprint` dopiero po wystarczającym rozstrzygnięciu modelu docelowego.
