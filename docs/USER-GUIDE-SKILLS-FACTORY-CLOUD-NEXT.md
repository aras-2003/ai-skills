# Skills Factory Cloud Next — instrukcja użytkownika

**Stan na 7 października 2026 r.** Site działa prywatnie w wersji 9. Udostępnia katalog Lab 0.33.4: 70 skills, w tym 16 workflowów. Nazwa Site i pluginu w tej chwili brzmi **Skills Factory Cloud Next**.

## Do czego służy

Plugin udostępnia instrukcje Skills Factory modelowi w ChatGPT. Model wybiera lub stosuje właściwy skill/workflow i przygotowuje odpowiedź. Sam MCP nie wykonuje całego rozumowania workflowu i nie podejmuje za Ciebie decyzji.

W zwykłym ChatGPT Chat najpierw jawnie wybierz plugin **Skills Factory Cloud Next** z podpowiedzi `@Skills Factory Cloud Next`. Samo napisanie „użyj MCP” nie gwarantuje, że Chat go wywoła. Jeśli nazwa ulegnie zmianie, wybierz aktualną pozycję widoczną w podpowiedziach pluginów; nie wpisuj na ślepo starej nazwy.

## Najprostszy sposób użycia

1. Otwórz nową rozmowę w trybie **Chat**.
2. W polu wiadomości wpisz `@` i wybierz **Skills Factory Cloud Next** (lub aktualną nazwę widoczną w podpowiedziach).
3. Opisz cel, kontekst i ograniczenia zwykłym językiem. Podaj tylko dane, które możesz udostępnić w tej prywatnej rozmowie.
4. Przy ważnym wyniku poproś model o wskazanie użytego workflowu, brakujących dowodów, założeń i granic wniosku.
5. Jeśli wynik twierdzi, że użył pluginu, sprawdź czy w rozmowie widać dołączoną pozycję pluginu. W testach poproś też o surowy wynik narzędzia i rewizję runtime.

Najlepiej opisywać zadanie, a nie tylko nazwę skillu. Nazwę podaj jawnie, gdy chcesz wymusić znaną procedurę albo przeprowadzasz test regresji.

### Przykłady

**Naturalne zadanie:**

> Oceń, gdzie proces podejmowania decyzji w tym przykładzie się blokuje. Oddziel fakty od hipotez i nie projektuj jeszcze nowego governance.

**Jawny workflow:**

> Użyj `oaf-health-check`. Najpierw zastosuj jego kryteria wejścia, dobierz tylko potrzebne obszary i wskaż, które wnioski są faktami, a które hipotezami.

**Test routingu inwestycyjnego:**

> Użyj Skills Factory Cloud Next do routingu tego pytania. Zwróć `route`, `child_workflow`, `status`, `recommendation` i `workflow_executed`. Nie analizuj inwestycji, nie zapisuj danych i nie sugeruj transakcji.

## Co udostępnia MCP

- `runtime_info` — identyfikacja wdrożonej wersji Site, źródła i kontraktu narzędzi.
- `list_skills` — katalog dostępnych skills/workflowów.
- `load_skill` — instrukcja wybranego skillu oraz dozwolone referencje; pliki ewaluacyjne nie są udostępniane.
- `route_investment_request` — klasyfikacja zapytania inwestycyjnego i wskazanie workflowu. To routing, nie rekomendacja ani wykonanie workflowu.
- `render_bar_chart` i `render_line_chart` — generowanie wykresów z przekazanych danych.

## Ważne ograniczenia

- Site jest prywatny. Plugin jest przeznaczony do testów właściciela, nie do publicznego katalogu.
- Wersja 9 raportuje własną rewizję Site. Katalog Lab ma osobną rewizję i numer: obecnie 0.33.4. Zmiana kodu Site nie oznacza automatycznie zmiany treści Lab.
- `route_investment_request` nie ładuje ani nie wykonuje wybranego workflowu. Model musi osobno załadować wskazaną instrukcję i zastosować jej bramki.
- Brak połączonego źródła danych, integracji lub wymaganych uprawnień może zatrzymać workflow. Model powinien to ujawnić, a nie symulować odczyt lub zapis.
- Test na syntetycznych danych nie potwierdza działania na prawdziwym portfelu, w repozytorium ani w systemie zewnętrznym.
- Wykres może zostać wygenerowany jako payload, ale nie zakładaj, że każdy klient pokaże go identycznie. Sprawdź widok wykresu i tabelę danych.
- Odpowiedzi modelu mogą być błędne. Zweryfikuj ważne liczby, źródła i decyzje.

## Jakiego modelu używać

Zgodnie z przyjętą strategią testów:

- **GPT-6 Luna** — domyślny wybór do większości testów i typowych zadań. W pierwszej kolejności testuj w zwykłym Chat.
- **GPT-6 Sol** — przypadki brzegowe, sprzeczne instrukcje i trudne błędy, których Luna nie rozstrzygnęła.
- **Astra** — tylko wyjątkowo ważne przypadki krytyczne lub pogłębiony przegląd/refaktoryzacja poza standardową kampanią. Nie używaj jej do rutynowych testów.
- **Work** — dopiero gdy konkretna czynność wymaga dostępu do plików, repozytorium lub runnera, którego Chat nie może użyć. Wtedy zacznij od Luny; Sol/Astra tylko zgodnie z powyższymi progami.

Nazwy modeli w interfejsie mogą się zmieniać. Kieruj się bieżącą listą modeli, nie starą nazwą w tym dokumencie.

## Gdy zmieni się nazwa lub wersja

Jeśli nazwa Site albo pluginu zmieni się, wyszukaj aktualną nazwę w selektorze pluginów ChatGPT i zaktualizuj tę instrukcję przy następnym wydaniu. Nie twórz nowego pluginu tylko dlatego, że zmienił się numer wersji. Przed testem wersji sprawdź przez `runtime_info`, jaki Site/revision faktycznie odpowiada. Przy pytaniach o bieżący adres Site skorzystaj z linku Site w ustawieniach właściciela.

## Zgłaszanie problemu

Zapisz: treść promptu, tryb Chat/Work, wybrany model, czy plugin był jawnie dołączony, nazwę wybranego workflowu, widoczny wynik narzędzia i rewizję z `runtime_info`. Nie dołączaj haseł, tokenów ani prywatnych danych portfela. Rozróżnij:

- **PASS** — wykonanie było widoczne i spełniło kryteria;
- **FAIL** — wykonanie się odbyło, ale naruszyło kryterium;
- **NOT RUN / BLOCKED** — brak wykonania albo wymaganej integracji; nie oznacza to PASS.
