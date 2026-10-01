Workflow `oaf-operating-model-redesign` został uruchomiony w ograniczonym zakresie.

### 1. Diagnoza robocza

**Fakty podane:**

- problem występuje na styku produktu, sprzedaży i IT;
- handoffy są niejasne;
- odpowiedzialność ginie między jednostkami;
- decyzje eskalują między dyrektorami;
- istnieją dane o objawach, ale brak osobnej analizy interfejsów.

**Wnioski strukturalne — jeszcze niepotwierdzone:**

- odpowiedzialność może być współdzielona bez odpowiadającej jej władzy decyzyjnej;
- eskalacje mogą zastępować brak jasno określonego właściciela decyzji;
- handoffy prawdopodobnie nie mają jednoznacznych wejść, wyjść, kryteriów gotowości ani SLA;
- nie można jeszcze stwierdzić, czy głównym problemem jest struktura, governance, brak capacity authority, czy wykonanie obecnego modelu.

Brak `organizational-interface-review` jest istotnym ograniczeniem. Nie symuluję tej analizy.

### 2. Zasady projektowe

- Jeden jasno wskazany właściciel każdej decyzji materialnej.
- Konsultacja nie może działać jako ukryte veto.
- Odpowiedzialność musi iść razem z zakresem decyzji, capacity i kontrolą nad zależnościami.
- Handoff powinien być traktowany jako kontrakt operacyjny, nie jako przekazanie „na dobre chęci”.
- Eskalacja powinna mieć określony trigger, termin, miejsce docelowe i zakres decyzji.
- Należy poprawiać interfejsy i prawa decyzyjne przed zmianą formalnej hierarchii.

### 3. Ograniczone opcje redesignu

| Opcja | Zakres | Korzyść | Główne ryzyko |
|---|---|---|---|
| A. Minimalna stabilizacja interfejsów | Ujednolicenie 2–3 krytycznych handoffów, decision log, jawne kryteria wejścia/wyjścia | Najmniejsza ingerencja i szybka odwracalność | Może nie wystarczyć, jeśli problem jest strukturalny |
| B. Wspólny model decyzji cross-functional | Dla wybranych decyzji produkt–sprzedaż–IT: jeden owner, obowiązkowi adviserzy, executor, eskalacja i termin | Bezpośrednio ogranicza eskalacje między dyrektorami | Nie zadziała bez potwierdzenia realnej władzy nad capacity |
| C. Stała jednostka/”pod” cross-functional | Trwały zespół odpowiedzialny za wybrany strumień od popytu do dostarczenia | Najsilniejsza ciągłość odpowiedzialności | Przedwczesne bez danych o wolumenie, capacity i granicach mandatów |

### 4. Kierunek prowizoryczny

Najbardziej obronna jest kombinacja **A + ograniczony pilot B**:

1. wybrać jeden konkretny strumień lub klasę decyzji;
2. opisać obecny formalny i faktyczny przebieg;
3. ustalić jednego właściciela decyzji;
4. rozdzielić adviserów, executorów i osoby eskalowane;
5. zdefiniować warunki kompletności handoffu;
6. mierzyć liczbę eskalacji, oczekiwanie, rework i decyzje wracające do poprzedniego etapu.

Nie rekomenduję jeszcze opcji C ani docelowego modelu organizacyjnego. Mogłoby to być jedynie przeniesienie niejasności do nowej jednostki.

### 5. Krytyczne niewiadome

Przed wyborem modelu docelowego trzeba potwierdzić:

- które decyzje najczęściej eskalują;
- kto formalnie i faktycznie podejmuje te decyzje;
- czy dyrektorzy zatwierdzają, czy działają jako de facto właściciele;
- gdzie występuje oczekiwanie, rework i ukryte veto;
- czy właściciel priorytetyzacji kontroluje również capacity i funding;
- jakie są minimalne kryteria przekazania między produktem, sprzedażą i IT.

### 6. Pilot walidacyjny

Pilot powinien objąć jeden reprezentatywny przypadek, np. decyzję dotyczącą zobowiązania wobec klienta wymagającą udziału produktu i IT.

W pilocie należy zarejestrować:

- formalną ścieżkę;
- faktyczną ścieżkę;
- wszystkie oczekiwania i powroty;
- decyzje oraz ich właścicieli;
- momenty eskalacji;
- dostępność capacity i danych wejściowych.

Kryterium sukcesu nie powinno być samo skrócenie czasu. Należy sprawdzić jednocześnie, czy decyzje są jednoznaczne, wykonalne i nie generują przerzuconego reworku.

### Status workflow

- Diagnoza: **częściowa, oparta na objawach**.
- Opcje: **zdefiniowane w zakresie ograniczonym**.
- Wybór modelu docelowego: **pozostawiony nierozstrzygnięty**.
- Governance redesign: **jeszcze nieuruchamiany**.
- Transformation blueprint: **jeszcze nieuruchamiany**.
- Najbliższy krok: **mała analiza reprezentatywnych interfejsów i decyzji**, nie pełny redesign organizacji.
