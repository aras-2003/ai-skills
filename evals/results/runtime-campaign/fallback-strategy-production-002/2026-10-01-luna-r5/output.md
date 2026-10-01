## Diagnoza wykonawcza

- **[observed | wysoka]** Inicjatywy są wybierane reaktywnie, a priorytety zmieniają się co kwartał — dowód: opis sytuacji; wystarczające do potwierdzenia niestabilności portfela, ale nie jej przyczyny.
- **[observed | wysoka]** Zespoły nie potrafią połączyć roadmap z mierzalnymi wynikami strategicznymi — dowód: opis sytuacji; nie rozstrzyga, czy problemem są metryki, właścicielstwo, proces decyzyjny czy brak wspólnego mechanizmu oceny.
- **[supported | średnia]** Portfolio nie ma obecnie wystarczająco porównywalnych danych do rzetelnego priorytetyzowania — wynika z braku wskazanych outcome’ów, właścicieli, kosztu, capacity, zależności i kosztu opóźnienia.
- **[hypothesis | średnia]** Najbardziej prawdopodobny jest rozpad pętli „strategiczny outcome → wybór inicjatywy → przegląd dowodów → decyzja o kontynuacji/zmianie”, ale obecne dane nie wskazują jeszcze dominującego miejsca awarii.

## OAF heatmap

| Domena | Claim | Status | Pewność | Dowód / ograniczenie |
|---|---|---|---|---|
| Strategy–execution | Strategia wzrostu i transformacji nie przekłada się stabilnie na wybór oraz prowadzenie inicjatyw. | observed | wysoka | Bezpośredni opis użytkownika; niedostępna specjalistyczna gałąź `strategy-to-execution-diagnostic`. |
| Portfolio prioritization | Decyzje portfelowe są reaktywne i niestabilne. | observed | wysoka | Bezpośredni opis użytkownika. |
| Portfolio prioritization | Nie można jeszcze uczciwie policzyć rankingu inicjatyw. | supported | wysoka | Brakuje minimalnych porównywalnych danych; workflow zabrania tworzenia fałszywej precyzji. |
| Evidence loop | Roadmapy nie są skutecznie powiązane z mierzalnymi outcome’ami strategicznymi. | observed | wysoka | Bezpośredni opis użytkownika. |
| Evidence loop | Nie wiadomo jeszcze, czy dominującą awarią są metryki, cadence, właścicielstwo, interpretacja czy mechanizm działania. | supported | wysoka | Opis potwierdza skutek, nie mechanizm. |
| Operating model | Możliwe niedopasowanie odpowiedzialności, authority, funding/capacity lub interfejsów między strategią, portfolio i zespołami. | hypothesis | średnia | Mechanizm pasuje do objawów, ale brak danych o strukturze i mandatach. |
| Decision rights | Nie ma wystarczających dowodów, aby stwierdzić, że problemem są konkretne niejasne prawa decyzyjne. | observed | wysoka | Użytkownik nie podał danych o opóźnieniach ani sporach decyzyjnych; nie należy tego dopowiadać. |

## Wiodące hipotezy

1. **Brak wspólnego mechanizmu porównywania inicjatyw.**  
   Wzmocni ją sytuacja, w której różne inicjatywy nie mają porównywalnych outcome’ów, ownerów, capacity, zależności i kosztu opóźnienia. Osłabi ją istnienie takiego mechanizmu, który jest omijany.

2. **Przeglądy raportują postęp, ale nie wywołują decyzji adaptacyjnych.**  
   Wzmocni ją brak jawnych progów działania lub brak korekt scope/funding/priorytetu po przeglądach. Osłabi ją dowód, że decyzje są podejmowane, lecz problem leży wcześniej — w definicji outcome’ów.

3. **Odpowiedzialność za wynik nie jest połączona z authority i capacity.**  
   Wzmocni ją sytuacja, w której owner roadmapy nie może kontrolować finansowania, zależności lub zasobów. Osłabi ją jasne właścicielstwo i wystarczające uprawnienia przy jednoczesnych problemach pomiarowych.

## Najkrótszy sensowny następny krok

Wykonać **jedną, ograniczoną normalizację dowodów** dla:

- 5–7 ostatnio wybranych inicjatyw, w tym co najmniej 2 kontynuowanych mimo zmiany priorytetów;
- 2 ostatnich zmian priorytetów kwartalnych;
- 2 ostatnich przeglądów portfolio lub roadmap.

Dla każdej inicjatywy zebrać tylko: strategiczny outcome, miarę wyniku, ownera, status mandatory/non-mandatory, koszt/capacity, zależności, koszt opóźnienia oraz decyzję podjętą na ostatnim przeglądzie.

Ten próbny wycinek rozróżni:

- brak porównywalnego modelu priorytetyzacji;
- awarię pętli dowodowej i progów działania;
- niedopasowanie owner–authority–capacity.

Próbka może pozostać niejednoznaczna; wtedy należy ją rozszerzyć o kolejny cykl, zamiast od razu projektować pełny model governance lub reorganizację.

Wykorzystane capability: `oaf-health-check`, `portfolio-prioritization`, `evidence-loop-review`, `operating-model-review`. Gałąź `strategy-to-execution-diagnostic` była niedostępna i nie została symulowana.
