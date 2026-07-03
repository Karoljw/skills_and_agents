# GitHub Copilot Instructions - Mailer Project

## 1. Python i Zależności
- Python 3.9+
- Standard: PEP 8 (linting: `flake8`, formatowanie: `black`)
- Type hints obowiązkowe dla wszystkich funkcji publicznych
- Plik `requirements.txt` musi być zawsze aktualny względem używanych bibliotek
- Preferuj wbudowaną bibliotekę standardową nad zewnętrznymi paczkami, jeśli to możliwe

## 2. Struktura kodu
- Moduły: max 500 linii
- Funkcje: max 50 linii
- Klasy: zasada pojedynczej odpowiedzialności (Single Responsibility)
- Struktura projektu do zachowania:
  - `mailer/` – logika biznesowa (subskrybenci, wysyłka emaili)
  - `templates/` – szablony HTML (Flask, Jinja2)
  - `static/` – pliki CSS/JavaScript
  - `tests/` – testy jednostkowe (pytest)

## 3. Konwencje nazewnicze
- Zmienne i funkcje: `snake_case`
- Klasy: `PascalCase`
- Stałe: `UPPER_SNAKE_CASE`
- Pliki testów: `test_<nazwa_modułu>.py`
- Nazwy opisowe, unikaj skrótów niejasnych dla innych deweloperów

## 4. Testy
- Framework: `pytest` + `pytest-cov`
- Minimum 80% code coverage
- Każda nowa funkcja: co najmniej 2 testy (happy path + edge case)
- Mockuj zewnętrzne usługi (serwer SMTP, baza danych) – żadnych realnych wysyłek emaili w testach
- Testy trzymane w `tests/`, odzwierciedlają strukturę `mailer/`

## 5. Bezpieczeństwo
- Brak danych wrażliwych (hasła, klucze API, credentials SMTP) zapisanych w kodzie
- Wszystkie sekrety przez zmienne środowiskowe (`.env`, nigdy niecommitowane)
- Walidacja wszystkich danych wejściowych, szczególnie adresów email z formularzy
- Ochrona przed SQL injection przy operacjach na bazie subskrybentów

## 6. Obsługa błędów
- Funkcje wysyłające email zwracają jasny status sukces/błąd (nie ukrywaj wyjątków)
- Loguj błędy zamiast pomijać je w ciszy (`try/except` z konkretnym wyjątkiem, nie `except: pass`)
- Waliduj dane wejściowe na granicy warstw (np. formularz Flask → logika biznesowa)

## 7. Git i commity
- Konwencja commitów: Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`)
- Nazewnictwo branchy: `feature/*`, `bugfix/*`, `docs/*`
- Pull Requesty: krótki opis zmian + dołączone testy dla nowej funkcjonalności