# Skills Factory — pakiet domknięcia do wykonania przez Lunę

Stan odniesienia: 2026-10-07. To instrukcja **wykonania nowych testów**, nie raport ich zaliczenia.

## Co jest faktem

Odczyt Cloud MCP w tej sesji potwierdził:

- Site **Skills Factory Cloud Next**, wersja 12, prywatny; nie zmieniaj widoczności.
- Site source/release: `5a598bb0f6bd52b395b35da02107d1898213d980`.
- `attestation_status: verified`, `identity_source: site_environment`.
- Osadzony Lab `0.33.4`, źródło `b5ce981af12003e8a8c00ed66efb58f3cee3c314`.
- Katalog: **54 skills + 16 workflow entrypoints = 70**. `skill-development` jest osobnym workflowem repozytorium, nie 71. elementem MCP.
- Repo main użyte do przygotowania: `434922cd05216eec56f7fa766ca1569c0b637668`.
- Sześć narzędzi MCP: `runtime_info`, `list_skills`, `load_skill`, `route_investment_request`, `render_bar_chart`, `render_line_chart`.

Snapshot odczytów: `evals/campaigns/closure-v12/baseline.json`. Nie kopiuj go jako dowodu nowego przebiegu. Każdy przebieg wymaga świeżej identyfikacji. Site SHA, Lab SHA i GitHub main SHA są różnymi warstwami; ich różność sama w sobie nie jest błędem.

## Przygotowanie pakietu

W checkoutcie zawierającym tę instrukcję, z zależnościami z `requirements-dev.lock`:

```sh
python scripts/eval/prepare_closure.py --output /tmp/skills-factory-closure-v12-run-01
python scripts/eval/prepare_closure.py --output /tmp/skills-factory-closure-v12-run-01 --validate
```

Katalog wyjściowy musi być nowy/pusty. Ponowienie nie nadpisuje poprzednich dowodów.

Wynik zawiera:

- `queue.json`: kolejkę wszystkich przypadków, priorytety, powiązania backlogu, hashe input/rubric, stan startowy `NOT_RUN`.
- `executor-inputs.zip` oraz `executor/`: wyłącznie ponumerowane prompty; bez rubryk i mapy oczekiwanego routingu.
- `evaluator/`: osobne kryteria semantyczne; tylko dla oceniającego.
- `coverage.json`: macierz każdego z 70 elementów, testy oraz osobny przegląd capability/side effects.
- `BACKLOG.md` i `backlog-snapshot.json`: pełne **89** zadań z oryginalnymi statusami, zakresem, zależnościami i kryteriami odbioru.
- `summary.json`: kontrolne liczby; nie zawiera runtime PASS.
- `orchestrator-handoff.zip`: całość do przekazania Lunie-orchestratorowi; **nie** przekazuj tego archiwum niezależnemu executorowi.

Pakiet obejmuje wszystkie 245 przypadków źródłowych (240 skills, 5 repo workflows), 88 par runtime input/rubric, 48 nowych przypadków całych workflowów, 36 regresji i testów granic (w tym brakujące negative cases meta/Career) i 70 testów ładowania/parytetu. To **487 definicji**, nie 487 wykonanych testów. Nie dodawaj tych kategorii do historycznej liczby R16.

38 ogólnych fixture'ów dostało w tym nowym pakiecie konkretne dane i obserwowalne kryteria z `skill-refinements.yaml`; oryginałów nie zmieniono. Zachowano ich pochodzenie i hash oryginalnego inputu. Dwa historyczne fallbacki zakładały brak specjalisty w produkcyjnym katalogu; overlay v12 sprawdza użycie faktycznie dostępnego specjalisty. Wyników overlay **nie przypisuj staremu R16**. Historyczne wyniki i piny pozostają nietknięte.

## Modele, Chat i izolacja

Wszystkie przebiegi zaczynaj w **zwykłym Chat**, z wybraną wtyczką **Skills Factory Cloud Next**, modelem **Luna**. Same nazwy skillów w odpowiedzi nie wystarczają: wymagane jest rzeczywiste `load_skill` i wykonanie załadowanej instrukcji przez host model.

Repo, pliki i przeglądarka nie oznaczają automatycznie Work. Korzystaj z dostępnych konektorów w Chat. Jeśli konkretna niezbędna operacja rzeczywiście nie działa, zapisz dowód, spróbuj bezpiecznej alternatywy i zapytaj użytkownika o **ten konkretny** test w Work. Bez jego zgody pozostań przy Chat i kontynuuj niezablokowane przypadki.

Sol tylko do potwierdzonych trudnych przypadków brzegowych i publikacji według aktualnego `docs/SITES-PUBLISHING.md`. Nie używaj Astra w standardowej kampanii. Nie obiecuj cen ani oszczędności bez aktualnych danych.

Luna-orchestrator może czytać ten dokument i rubryki. **Executor** dostaje tylko pojedynczy `.input.md`, dostępny runtime/katalog i zasady bezpieczeństwa — nie ten dokument, kolejkę z targetami ani evaluator ZIP. Jeden świeży czat na przypadek. Oceniający dostaje zapis wykonania dopiero po zamknięciu odpowiedzi. Wykonanie w sesji znającej rubrykę jest assisted i nie daje niezależnego PASS.

Nie wysyłaj samodzielnie wiadomości do innych istniejących czatów. Użytkownik przekazuje ten pakiet Lunie. Pakiet nie tworzy runnera/modelowego API ani nie daje nowych uprawnień.

## Kolejność domykania — kolejka robocza

| Krok | Zadania | Wykonanie i kryterium domknięcia |
|---|---|---|
| 1 | ENG-01, EXI-01 | Świeże main/Site/Lab identities; uzgodnij AIS/RT oraz count 54/17/16/70. Stare piny w README/backlogach oznacz historyczne, nie traktuj jako aktualną instalację. |
| 2 | E2E-01 | Browser Chat: rzeczywisty `runtime_info`, exact revision i trace. Fixture stale/missing sprawdza tylko rozumowanie; do pełnego zamknięcia dodaj kontrolowany test wykrywania starej/brakującej rejestracji w host integration. |
| 3 | E2E-04, ENG-17 | 70 × `load-*`; compare instrukcje i dozwolone referencje z **dokładnym** artefaktem Lab, nie tylko bieżącym main. Potem porównaj różnicę źródła Lab z main i objaśnij wpływ. Dla workflowów obowiązkowe `references/WORKFLOW.md`; zero `references/evals/`, `tests/` i rubryk. |
| 4 | E2E-02, E2E-05, EXI-04 | Dwa wykresy, osobno SVG/payload, accessibility, tabela, rzeczywisty obraz klienta. Screenshot w Chrome obowiązkowy dla display. Naprawę opisu bar potwierdź regresją. |
| 5 | ENG-10, EXI-01 | Natural routing PL/EN, uppercase Ł, route-only, bez fan-out; 5 dawnych obserwacji OAF z nowymi inputami. Dodatkowo wykonaj pozytywne, near-miss i konkurujące routing fixtures. |
| 6 | E2E-02 | 48 nowych testów flow: 16 × dane / brak preconditions / narrow near-miss. Direct `architecture-review` i `capability-gap-analysis` testuj osobno od parent workflowu. Zbierz raw refs i odpowiedź. |
| 7 | ENG-03/04/05/06, ENG-02 | Dedykowane meta inputy plus repo-only skill-development. queued/no_steps ≠ PASS; brak identity/channel, stale authorization i digest mismatch blokują release. Positive control daje recommendation, nie automatyczną publikację. |
| 8 | EXI-02 | Career: validity → context → role evaluation → CV gaps → tailoring → brief → process update, na fikcyjnych danych. Osobny live listing potrzebuje rzeczywistego URL/czasu/statusu, nie domniemania z syntetycznego ATS. |
| 9 | ENG-15/16, E2E-03 | Security injection, denied/timeout, bootstrap contradiction, schema/renderer validation. Oddziel symulowaną odpowiedź od rzeczywiście wywołanego błędu. Review deklarowanych permissions każdego elementu. |
| 10 | ENG-20 | Odczyt bieżącej ochrony main/production, wymaganych checks i publisher permissions; lock/hashes, pełne SHA Actions, artifact digests. Nie zmieniaj branch protection ani publishera „dla testu”. |
| 11 | Cała kampania R16 + supplemental | Ponownie wykonaj pozostałe istniejące inputy na v12; wyniki oznacz current v12 overlay, nie historyczny production PASS. Do świadomej regresji R16 użyj oryginalnego pinu/artifactu i osobnych receipts. |
| 12 | ENG-08, ENG-19 | Zweryfikuj import nowych case IDs do formalnego runner/receipt systemu i audyt zamknięć; przygotowany ZIP nie jest nową implementacją runnera. Nie zamykaj ENG-08 na podstawie eksportera. |

Wszystkie pozostałe pozycje backlogu są rozpisane w `BACKLOG.md`. Nowe domeny i roadmapa CON/WRI/PRO/LEA/LIF/STR/DOM pozostają **przyszłym developmentem**, a nie istniejącymi skillami, które można rzekomo zaliczyć. Po obecnej jakości: jedno domain review, następnie wąski, uzasadniony slice. Nie wykonuj 89 propozycji naraz i nie rozszerzaj scope bez decyzji właściciela.

## Dowody, bezpieczeństwo i realne ograniczenia

Zapisz dla każdego przebiegu: case ID, input/rubric hashes, UTC czas, URL czatu, model i reasoning, fresh runtime_info, katalog/tool availability, surowy trace narzędzi, final answer, reviewer, assisted/unassisted, output/trace digests, a dla display także screenshot. Osobno oceniaj behavior, integration, exact-version identity i client display.

Stosuj istniejący protokół `scripts/eval/README.md`: `outcome` (`passed`, `failed`, null) osobno od `execution_state` (`executed`, `blocked`, `awaiting_runner`, `no_steps`, `not_executed`). `NOT_RUN` ma outcome null i konkretny powód. `REVIEW_REQUIRED` = wykonano, ale dowód nie pozwala na pełne zaliczenie. Blokada dostępu nie jest automatycznie defektem produktu.

Nowa kolejka jest manifestem planu, **nie formalnym release receipt**. `receipt.py` nie zna wszystkich nowych identyfikatorów; przed formalnym release należy zarejestrować nowe pary input/rubric w repozytoryjnym systemie kampanii i zwalidować receipts. Nie dopisuj PASS do historii, żeby ominąć ten brak.

- Żadnych zapisów testowych do realnego Investment OS, CRM, profili, polityk, tez, transakcji, CV ani innych danych prywatnych. Testy write/idempotency wymagają izolowanego, jawnie wskazanego test store/namespace, cleanupu i rzeczywistych read-back receipts. Brak takiego środowiska = integration NOT_RUN; ocena logiki na fikcyjnym fixture może być wykonana oddzielnie.
- Eksporter nie usuwa żądań write ze starych inputów: bezpieczeństwo egzekwuje orchestrator. Kieruj je do izolowanego store; nie puszczaj ich na prawdziwych danych. Nie nazywaj poprawnego „odmówiono zapisu” zaliczeniem udanego zapisu.
- `list_skills` nie wykonuje workflowu. `route_investment_request` tylko klasyfikuje. `load_skill` tylko ładuje instrukcje; pełny flow wymaga działania host modelu i osobnych konektorów.
- `PAYLOAD_RENDERED` nie oznacza `CLIENT_RENDERED`. Uczciwy fallback może zaliczyć wymaganie fallbacku, ale nie zamyka obowiązkowego display w E2E-02.
- Statyczny scanner nie dowodzi runtime safety. 70 source matches nie dowodzi reference digest parity ani równoważnych uprawnień Chat/Lab.
- Nie wyłączaj prywatności, auth, checks ani sandboxa. Po denial nie odtwarzaj odrzuconej operacji inną drogą; zbierz dokładną przyczynę i wykonaj niezablokowane testy.
- Brak production promotion nie blokuje testowania elementu dostępnego w Lab/Site. Nie promuj maturity i nie wdrażaj produkcji jako efektu kampanii.

## Deterministyczne kontrole repo

Ustalenia z przygotowania, do dopięcia w ENG-01/ENG-08, nie nowe runtime FAIL:

- `campaign.py validate` wypisuje na sztywno „38 cases”, choć test struktury R16 potwierdza 44 core + 3 supplemental. Napraw informacyjny licznik i dodaj test zgodności komunikatu z konfiguracją.
- Domyślne `common.ACTIVE_CAMPAIGN` nadal wskazuje R6; jawny harness używa R16. Sprawdź skutki dla domyślnego wyszukiwania/importu receipts i usuń niejednoznaczność bez przepisywania historii.
- Stare README/guide mają m.in. Site v9, stare piny/liczby i pięć zamiast sześciu release-review fixture'ów. Uzgodnij aktualne wskazówki, zachowując historyczne daty/receipts.
- Capability schema przechodzi, ale **70/70 ocen pozostaje UNASSESSED**. Nie zamykaj ENG-16 na podstawie pozytywnej walidacji schematu.
- Do kontroli R16 potrzebna jest dostępna historia z przypiętym commitem; shallow clone może ją odciąć. Pobierz historię, nie zmieniaj pinu tylko po to, by test przeszedł.
- Ustaw zapisywalny `MPLCONFIGDIR` podczas testów rendererów; tymczasowy fallback cache nie jest testem widoczności wykresu w Chat.

Przez dostępny repo/file/terminal connector, nie przez wymyślone narzędzia MCP:

```sh
python scripts/validate/validate_all.py
python scripts/eval/validate_isolation.py
python scripts/eval/validate_routing.py
python scripts/eval/campaign.py validate
python scripts/eval/skill_release_campaign.py validate
python scripts/security/scan_skills.py --report /tmp/closure-security.json
python scripts/capabilities/validate_contract.py --report /tmp/closure-capabilities.json
python -m unittest discover -s scripts/validate/tests -p 'test_*.py'
python -m unittest discover -s scripts/eval/tests -p 'test_*.py'
python -m unittest discover -s scripts/security/tests -p 'test_*.py'
python -m unittest discover -s scripts/capabilities/tests -p 'test_*.py'
python -m unittest discover -s scripts/package/tests -p 'test_*.py'
python -m unittest discover -s scripts/readiness/tests -p 'test_*.py'
python -m unittest discover -s scripts/release/tests -p 'test_*.py'
python -m unittest discover -s skills/commerce/economics/unit-economics-review/tests -p 'test_*.py'
```

Build Lab i walidacja artefaktu według README/CI na nowym katalogu. Nie uruchamiaj całego Site publishing tylko po to, żeby przygotować testy. Zmiany zachowania po naprawie wymagają nowego verified deployment oraz nowego pinu kampanii; stary wynik nie dziedziczy PASS.

## Pętla poprawka → regresja → raport

Po FAIL: zachowaj dowód, powiąż defect z istniejącym backlog ID lub dodaj nowy z konkretnymi acceptance criteria. Zrób małą poprawkę na branchu, sprawdź deterministyczne gates, opublikuj zgodnie z aktualnym runbookiem tylko jeśli użytkownik zlecił wdrożenie. Potwierdź nowy Site runtime i embedded Lab. Powtórz failing case, sąsiednie boundary cases, affected workflow oraz routing/display gdy dotknięte. Nie powtarzaj niezmienionych kilkuset przypadków bez powodu; końcowa szeroka regresja musi jasno wskazywać dokładną testowaną rewizję.

Raport końcowy: PASS / FAIL / REVIEW_REQUIRED / NOT_RUN per case i component; blockers z przyczyną; actual vs simulated failures; zapisane skutki uboczne; poprawki i rewizje; spełnione/niespełnione kryteria backlogu; lista pozostałych testów. DONE dopiero po spełnieniu **wszystkich** kryteriów konkretnego zadania, nie dlatego że raport brzmi dobrze.

## Prompt do przekazania Lunie-orchestratorowi

> Przeczytaj docs/LUNA-CLOSURE-V12.md i przygotuj nowy pakiet closure-v12 przez scripts/eval/prepare_closure.py. Wykonuj kolejkę w kolejności domykania z dokumentu, w zwykłym Chat z Skills Factory Cloud Next, domyślnie Luna. Każdy executor ma świeży czat i widzi wyłącznie input, nigdy rubrykę. Zbieraj actual tool traces, fresh identity i browser display evidence; symulacje oznacz oddzielnie. Nie zapisuj nic do realnych prywatnych systemów; write cases wymagają izolowanego test store. Work tylko po mojej zgodzie na konkretny przypadek, Sol do uzasadnionych edge cases, Astra poza kampanią. Nie przepisuj historycznych PASS ani pinów R16. Realne FAIL naprawiaj małymi zmianami i wykonuj regresję. Publikację rób tylko w ramach wyraźnie zleconego wdrożenia, według aktualnego docs/SITES-PUBLISHING.md. Na końcu daj macierz wyników, backlog closure z dowodami i dokładną listę pozostałych prac. Nie zaliczaj testu bez wykonania ani zadania bez spełnienia jego acceptance criteria.
