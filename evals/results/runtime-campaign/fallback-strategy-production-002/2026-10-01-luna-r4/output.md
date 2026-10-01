Workflow `arek-ai-skills:oaf-health-check` wykonany w ograniczonym zakresie. Gałąź `strategy-to-execution-diagnostic` jest niedostępna w aktywnej instalacji, więc nie była symulowana. Nie uruchamiałem projektowania governance ani transformacji — dane nie uzasadniają jeszcze takich zmian.

## Diagnoza wykonawcza

Firma ma strategię, ale nie ma stabilnego mechanizmu przekładania jej na porównywalne decyzje portfelowe i roadmapy. Reaktywna selekcja inicjatyw oraz kwartalne zmiany priorytetów są obserwowane; brak powiązania roadmap z mierzalnymi wynikami również. Najbardziej prawdopodobny problem strukturalny to pęknięcie między strategią, decyzjami portfelowymi, finansowaniem/pojemnością zespołów i cyklem uczenia się. Nie można jeszcze potwierdzić, czy główną przyczyną są niejasne prawa decyzyjne, słabe dane inicjatyw, brak właścicieli wyników czy nieskuteczny rytm przeglądów.

## OAF heatmap

| Domena | Status | Typ ustalenia | Pewność | Główny problem | Konsekwencja |
|---|---|---|---|---|---|
| Portfolio prioritization | krytyczny | observed | wysoka | Inicjatywy są wybierane reaktywnie, a priorytety zmieniają się kwartalnie | Portfel nie zapewnia stabilnej sekwencji realizacji |
| Evidence loop | krytyczny | observed | wysoka | Roadmapy nie są łączone z mierzalnymi wynikami strategicznymi | Zespoły nie mają wspólnego mechanizmu oceny postępu |
| Decision rights | do weryfikacji | hypothesis | średnia | Nie wiadomo, kto ma mandat do zmiany priorytetów, finansowania i pojemności | Możliwe decyzje reaktywne lub wielokrotne eskalacje |
| Operating model | do weryfikacji | hypothesis | średnia | Odpowiedzialność za wynik strategiczny może być rozdzielona od kontroli nad roadmapą i zasobami | Możliwe lokalne optymalizacje bez odpowiedzialności za wynik enterprise |

## Przyczyny przekrojowe

1. **Brak wspólnego kontraktu między strategią a portfelem — hypothesis.**  
   Należy sprawdzić, czy każda inicjatywa ma właściciela wyniku, mierzalny outcome, uzasadnienie strategiczne i konsekwencję zaniechania.

2. **Priorytety mogą być zmieniane bez równoległej decyzji o pojemności i finansowaniu — hypothesis.**  
   Potwierdzeniem byłby ślad decyzji pokazujący zmianę priorytetu bez jawnego wycofania, przesunięcia lub odblokowania zasobów.

3. **Rytm przeglądów może generować raportowanie, ale nie decyzje adaptacyjne — hypothesis.**  
   Trzeba sprawdzić, czy przeglądy kończą się konkretną decyzją: kontynuować, zmienić zakres, zatrzymać albo przesunąć zasoby.

## Krytyczne niewiadome

- Kto formalnie i faktycznie zmienia priorytety?
- Czy zmiana priorytetu wymaga ujawnienia kosztu alternatywnego?
- Ile inicjatyw ma właściciela mierzalnego wyniku, a nie tylko właściciela dostarczenia?
- Czy kwartalne przeglądy mogą zmienić finansowanie, zakres i pojemność zespołów?
- Czy istnieją inicjatywy obowiązkowe, które są mieszane z inicjatywami uznaniowymi?

## Najkrótszy sensowny następny krok

Przeprowadź bounded evidence sample na trzech ostatnich inicjatywach:

- jednej kontynuowanej,
- jednej zdepriorytetyzowanej,
- jednej dodanej reaktywnie.

Dla każdej sprawdź tylko: właściciela wyniku, powiązany outcome strategiczny, miernik, uzasadnienie priorytetu, koszt/pojemność, zależności, decyzję o zmianie oraz ślad tego, kto i na jakiej podstawie ją podjął.

Ten mały przekrój rozstrzygnie, czy pierwszym problemem jest przede wszystkim:

- brak porównywalnych danych inicjatyw,
- niejasne prawa decyzyjne,
- brak sprzężenia decyzji z finansowaniem i pojemnością,
- czy nieskuteczny mechanizm przeglądu i reakcji.

Dopiero po tym próbkowaniu warto kierować sprawę do `decision-rights-review`, `portfolio-prioritization` albo `evidence-loop-review` w trybie pogłębionym.
