# Skills Factory — pełna kampania E2E dla Luny

Pracuj w zwykłym Chat. Wybierz z menu wtyczek **Skills Factory Cloud Next**. Domyślny model: Luna; Sol tylko do uzasadnionych przypadków brzegowych. Astra jest poza tą kampanią. Przejście do Work wymaga zgody użytkownika dla konkretnego przypadku, po zapisaniu dowodu, dlaczego dostępne narzędzia Chat nie wystarczają.

## Cel i aktualny runtime

Wykonaj wszystkie 490 przypadków: 245 authored, 89 existing-runtime, 38 closure-regression, 70 loader-parity i 48 workflow. Katalog zawiera 54 skills oraz 16 workflowów; osobny `skill-development` jest workflowem repo, a nie dodatkowym narzędziem Cloud MCP. Backlog ma 89 pozycji, w tym propozycje przyszłego developmentu. Oceniaj ich kryteria; nie implementuj wszystkich propozycji w trakcie kampanii.

Docelowy Site jest w wersji **14**. Wymagana rewizja Site: `05a720e4afcf5b2ccaf3c22186075aec61359800`. Osadzony Lab: `0.33.4`, źródło `b5ce981af12003e8a8c00ed66efb58f3cee3c314`. Weryfikuj odpowiednie warstwy osobno. `baseline.json` w pakiecie jest snapshotem rzeczywistych odczytów po publikacji; przed każdym nowym przebiegiem sprawdź aktualne `runtime_info`.

## Zawartość przestrzeni

- `campaign/queue.json`: identyfikatory, priorytety, hashe input/rubric i zależności backlogu. Manifest planu jest niezmienny.
- `campaign/executor-inputs.zip` i `campaign/executor/`: same wejścia dla wykonawcy. Wykonawca nie otrzymuje rubryk ani mapy oczekiwanych wyników.
- `campaign/evaluator/`: rubryki dla oddzielnego oceniającego.
- `campaign/coverage.json`, `campaign/BACKLOG.md`: pełna mapa komponentów i backlog.
- `evidence/preflight/`: rzeczywista identyfikacja, katalog i smoke regression po publikacji.
- `runs/`: nowe wyniki. Jeden katalog `<case-id>/<run-id>/` na każdy niezależny przebieg; nigdy nie nadpisuj wcześniejszej próby.
- `RECEIPT.template.json`: wzór wyniku. `NOT_RUN` i outcome null są stanem początkowym, nie zaliczeniem.
- `START-LUNA.md`: gotowy prompt orkiestratora.

## Przebieg pojedynczego testu

1. Otwórz świeży Chat i wybierz Cloud Next. Wykonawca otrzymuje tylko wskazany plik input. Zanotuj URL czatu, model, reasoning i czas UTC.
2. Wywołaj rzeczywiste `runtime_info`. Zapisz wynik; wymagaj `attestation_status: verified`, wskazanej rewizji Site, zgodnego Lab i tool schema digest. Gdy rewizja różni się od pinu, zachowaj dowód i uzgodnij nowy przebieg; nie przenoś PASS między wersjami.
3. Wykonaj input przez dostępne narzędzia. `load_skill` ma argument **`skill_name`**, np. `{ "skill_name": "oaf-health-check" }`. Odczytaj instrukcje oraz referencje i wykonaj ich flow przez model. Sama lista lub ładowanie nie kończy workflowu. Router jest klasyfikatorem; do pełnego flow potrzebne jest osobne ładowanie oraz wykonanie instrukcji.
4. Zachowaj actual tool trace, final answer i ewentualne pliki/read-back. Dla wykresów zapisz screenshot widocznego wyniku w Chat. SVG w wyniku MCP potwierdza payload; widoczność wymaga obserwacji klienta.
5. Oddzielny evaluator otrzymuje wejście, wynik, trace i odpowiadającą rubrykę. Ocenia wymagania i zapisuje powody, odniesienia do dowodów oraz status każdej warstwy: behavior, integration, identity, client_display.
6. Zapisz receipt i artefakty w nowym katalogu w `runs/`. Nowe case IDs są planem rozszerzającym kampanię; zanim będą formalnymi release receipts, trzeba zarejestrować je w istniejącym runnerze. Lokalna ocena E2E nie jest automatycznym zezwoleniem na release.

## Kolejność

Najpierw preflight, 70 loaderów i 38 regresji. Następnie 48 flow cases dla wszystkich 16 workflowów. Dalej pozostałe testy runtime i authored, z priorytetem P0/P1 oraz zależnościami z backlogu. Na końcu raport per component i backlog acceptance criteria. Testy różnych intencji nie powinny dzielić pamięci jednego wykonawcy.

Pierwsze regresje: „Mam akcje. Co zrobić?” musi dać `clarification_required`, pustą listę candidates i brak rekomendacji. „Review stock ACN”, „Oceń spółkę ASML.” i „Przeanalizuj akcje NVDA.” powinny wskazywać `investment-security-review`. Kolejne smoke checks: PL uppercase/lowercase opportunity routing, ładowanie referencji OAF, bar/line chart i invalid arguments.

## Dane i operacje zapisujące

Używaj syntetycznych danych z inputów. Zwykłe odpowiedzi i lokalne pliki dowodów mogą powstawać w przestrzeni kampanii. Przed testem realnego write/read-back musi istnieć jawnie wskazany izolowany store/namespace, rzeczywisty konektor, kontrola uprawnień i cleanup. Ten pakiet nie provisionuje bazy danych ani canonical record-store connectora. Gdy brak takiej integracji, oceniaj zachowanie i fallback na fixture, a rzeczywisty persistence oznacz `NOT_RUN`/blocked z konkretną przyczyną. Nie nazywaj symulacji zaliczonym zapisem. Skille dostępne w Lab/Site nie wymagają promocji do produkcji do zwykłych testów flow.

## Pętla napraw

Po rzeczywistym FAIL zachowaj pierwszą próbę, powiąż defect z backlogiem, przygotuj małą poprawkę i test. Publikuj zmiany zgodnie z aktualnym `docs/SITES-PUBLISHING.md`, gdy użytkownik zlecił wdrożenie. Po nowej publikacji utwórz świeży baseline i oddzielny przebieg dla failing case oraz sąsiednich granic. Nie odtwarzaj odrzuconego transferu poświadczeń inną drogą. Zgoda na publikację utrzymuje się w ramach zleconego zadania; platformowe approvals nadal obowiązują.

Raport zawiera PASS/FAIL/REVIEW_REQUIRED/NOT_RUN, wykonane versus symulowane integracje, zmiany, dokładne rewizje i pozostałe testy. Element backlogu jest DONE dopiero po spełnieniu wszystkich jego kryteriów, nie po przygotowaniu promptów ani po samym buildzie.

## Odtworzenie pakietu

Generator przyjmuje `--baseline evals/campaigns/closure-v14/baseline.json --instructions docs/LUNA-E2E.md` oraz nowy, pusty `--output`. Historyczne baselines i receipts pozostają zachowane. Przy kolejnej publikacji użyj nowego snapshotu runtime/catalog i nowej instrukcji z aktualnym pinem.
