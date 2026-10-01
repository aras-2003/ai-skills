Workflow `oaf-health-check` wykonany w zakresie capability dostępnych w tej sesji:

- `portfolio-prioritization`
- `evidence-loop-review`

`strategy-to-execution-diagnostic` jest niedostępny w pakiecie production, więc nie symuluję jego wykonania.

## Executive diagnosis

Problem nie wygląda na pojedynczy błąd roadmapy, lecz na brak stabilnego mechanizmu podejmowania decyzji portfelowych i uczenia się z wyników. Reaktywna selekcja oraz kwartalne zmiany priorytetów są obserwowane; ich przyczyną może być brak porównywalnych danych, niejasne kryteria decyzji albo brak forum z realną władzą nad finansowaniem i zakresem — tego nie da się jeszcze rozstrzygnąć. Brak połączenia roadmap z mierzalnymi wynikami wskazuje również na nieskuteczną pętlę evidence-to-action, ale nie dowodzi jeszcze, czy głównym problemem są metryki, ownership, cadence czy mechanizm decyzyjny.

## OAF heatmap

| Domena | Status | Typ | Pewność | Główny problem | Konsekwencja |
|---|---|---|---|---|---|
| Portfolio prioritization | żółty/czerwony | observed | wysoka dla symptomów, niska dla przyczyn | Inicjatywy wybierane reaktywnie, priorytety zmieniają się co kwartał | rozproszenie capacity, koszt zmian, brak wiarygodnego commitmentu |
| Evidence loop | czerwony | observed | wysoka dla symptomów, niska dla mechanizmu | Roadmapy nie są powiązane z mierzalnymi outcome’ami i decyzjami korygującymi | raportowanie nie prowadzi do uczenia ani świadomej zmiany priorytetów |

## Cross-domain causes

- **Brak minimalnego, porównywalnego zestawu danych dla inicjatyw — hipoteza.**  
  Potrzebne są: sponsor, wspierany outcome strategiczny, mierzalny rezultat, mandatory status, koszt, capacity, urgency, dependencies, risk, confidence i consequence of delay.

- **Priorytety mogą być zmieniane bez jawnego mechanizmu evidence-to-action — hipoteza.**  
  Należy sprawdzić, czy przeglądy mają progi działania oraz czy uczestnicy mają prawo zmieniać finansowanie, zakres i zasoby.

- **Brak stabilnej translacji strategii na outcome’y — symptom obserwowany, przyczyna niepotwierdzona.**  
  Pełna diagnoza wymaga niedostępnej w tej sesji capability `strategy-to-execution-diagnostic`.

## Critical unknowns

1. Kto formalnie decyduje o zmianie priorytetów, finansowania i zakresu?
2. Czy każda aktywna inicjatywa ma named ownera i mierzalny outcome?
3. Jakie dane są używane podczas kwartalnych zmian priorytetów?
4. Czy istnieją progi typu continue / stop / re-scope / defer?
5. Ile inicjatyw jest mandatory, a ile konkuruje o tę samą capacity?
6. Czy przeglądy mierzą outcome’y, czy głównie aktywność i postęp prac?

## Najkrótszy sensowny następny krok

W najbliższym przeglądzie portfela utworzyć jedną wspólną kartę dla wszystkich aktywnych inicjatyw i nie wykonywać jeszcze scoringu bez danych. Karta powinna wymagać: ownera, outcome’u strategicznego, mierzalnego rezultatu, kosztu, capacity, zależności, ryzyka, pilności, confidence oraz konsekwencji opóźnienia.

Na tej podstawie podjąć jedną jawną decyzję dla każdej inicjatywy: `continue`, `stop`, `re-scope` albo `defer`. To najkrótszy krok, który jednocześnie ujawni, czy dominującym problemem jest jakość danych, kryteria priorytetyzacji, capacity czy brak władzy decyzyjnej.
