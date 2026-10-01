Workflow `oaf-health-check` wykonany w ograniczonym zakresie do dostępnych capability:

- `portfolio-prioritization`
- `evidence-loop-review`

Gałąź `strategy-to-execution-diagnostic` jest niedostępna i nie była symulowana.

### Diagnoza wykonawcza

- **[observed | wysoka]** Wybór inicjatyw jest reaktywny, a priorytety zmieniają się kwartalnie — **dowód:** bezpośredni opis sytuacji; **pewność:** objaw został podany wprost.
- **[observed | wysoka]** Roadmapy zespołów nie są obecnie skutecznie łączone z mierzalnymi wynikami strategicznymi — **dowód:** bezpośredni opis sytuacji; **pewność:** objaw został podany wprost.
- **[supported | średnia]** Obecny problem dotyczy jednocześnie porównywalności decyzji portfelowych i pętli evidence-to-action — **dowód:** reaktywna selekcja, zmienność priorytetów i brak traceability; **ograniczenie:** nie ma jeszcze danych o mechanizmie przyczynowym.
- **[hypothesis | średnia]** Organizacja może mieć raportowanie lub przeglądy, które nie prowadzą do jawnych decyzji o finansowaniu, zakresie, kolejności lub zasobach — **do sprawdzenia:** protokoły przeglądów i decyzji kwartalnych.

### OAF heatmap

| Domena | Twierdzenie | Status | Pewność | Dowód / ograniczenie |
|---|---|---|---|---|
| Portfolio prioritization | Selekcja inicjatyw jest reaktywna. | observed | wysoka | Bezpośredni opis użytkownika. |
| Portfolio prioritization | Brakuje potwierdzenia, że inicjatywy są porównywane na wspólnym zestawie danych. | review-state limitation | wysoka | Nie podano ownera, outcome, kosztu, capacity, zależności ani urgency dla inicjatyw. |
| Evidence loop | Roadmapy nie mają skutecznej ścieżki do mierzalnych outcome’ów strategicznych. | observed | wysoka | Bezpośredni opis użytkownika. |
| Evidence loop | Nie wiadomo, czy dominującym problemem jest jakość metryk, ownership, cadence, interpretacja czy mechanizm działania. | review-state limitation | wysoka | Brak danych o KPI, progach, właścicielach i reakcjach po przeglądach. |
| Strategy–execution diagnostic | Pełna diagnoza tego obszaru nie została wykonana. | review-state limitation | wysoka | Wymagana gałąź jest niedostępna w produkcyjnej instalacji. |

### Wiodące hipotezy

1. **Brak wspólnego, używanego mechanizmu porównywania inicjatyw.**  
   Wzmocni ją próbka bez porównywalnych danych o outcome, ownerze, koszcie, capacity, zależnościach i koszcie opóźnienia. Osłabi ją obecność takich danych przy jednoczesnym obchodzeniu rankingu.

2. **Przeglądy kwartalne generują raporty, ale nie mają progów działania i jawnych decyzji.**  
   Wzmocni ją brak zapisanych triggerów, decyzji, właścicieli działań lub realnej władzy forum nad priorytetami i zasobami. Osłabi ją powtarzalny ślad: metryka → próg → decyzja → korekta roadmapy.

3. **Problem leży w tłumaczeniu strategii na outcome’y roadmap.**  
   Wzmocni ją brak jednoznacznego outcome i miernika dla większości inicjatyw. Osłabi ją obecność traceability, jeśli zespoły nadal nie używają jej przy podejmowaniu decyzji.

### Najkrótszy sensowny następny krok

Przeprowadź jedną, ograniczoną sesję normalizacji dowodów na próbce:

- 3 inicjatywy z ostatnich dwóch kwartałów: kontynuowana, repriorytetyzowana i zatrzymana/opóźniona;
- decyzje, które zmieniły ich priorytet;
- dwa ostatnie przeglądy kwartalne.

Dla każdej inicjatywy sprawdź tylko: ownera, strategic outcome, miernik wyniku, koszt, capacity, zależności, urgency, ryzyko, mandatory status i konsekwencję niedostarczenia. Dla przeglądów sprawdź: użyte dowody, progi działania, decyzje, uprawnienia forum i zapisane korekty.

Rezultatem ma być jedna macierz **initiative → outcome → evidence → decision → roadmap change**. Nie twórz jeszcze scoringu ani docelowego modelu governance. Próbka może pozostać nierozstrzygająca; wtedy rozszerz ją tylko o kolejne przypadki, które rozdzielają powyższe hipotezy.
