# Email Templates Skill

## Cel umiejętności
Wspieranie tworzenia, podstawiania zmiennych i testowania szablonów emaili (HTML i plain text) dla projektu Mailer. Skill obejmuje nową funkcjonalność "Email Templates", czyli generowanie treści wiadomości na podstawie wielokrotnego użytku szablonów zamiast statycznego tekstu w kodzie.

## Kontekst
- Projekt: Mailer (Flask + email)
- Silnik szablonów: Jinja2 (już używany przez Flask do `templates/`)
- Każdy email ma wersję HTML oraz plain text (fallback dla klientów bez obsługi HTML)

## Template Inheritance (dziedziczenie szablonów)

Podstawowy szablon bazowy definiuje wspólny layout (nagłówek, stopka), a konkretne szablony go rozszerzają.

```
templates/emails/base_email.html      # wspólny layout
templates/emails/welcome.html         # dziedziczy z base_email.html
templates/emails/confirmation.html    # dziedziczy z base_email.html
templates/emails/newsletter.html      # dziedziczy z base_email.html
```

```python
def render_email(template_name: str, context: dict) -> str:
    """Renderuj szablon emaila z kontekstem zmiennych."""
    from flask import render_template
    return render_template(f"emails/{template_name}", **context)
```

## Variable Substitution (podstawianie zmiennych)

Zmienne przekazywane są jako słownik i wstrzykiwane do szablonu (`{{ subscriber_name }}`, `{{ unsubscribe_link }}`). Zawsze waliduj obecność wymaganych kluczy przed renderowaniem, aby uniknąć pustych pól w wysłanej wiadomości.

```python
REQUIRED_FIELDS = {"subscriber_name", "unsubscribe_link"}

def validate_context(context: dict) -> bool:
    """Sprawdź czy kontekst zawiera wymagane pola."""
    return REQUIRED_FIELDS.issubset(context.keys())
```

## HTML / Plain Text

Każdy szablon powinien mieć odpowiednik plain text (`welcome.html` + `welcome.txt`), generowany albo ręcznie, albo automatycznie ze strippingu tagów HTML — plain text zawsze jako fallback w wielo-częściowej wiadomości MIME.

## Template Testing

```python
def test_render_welcome_email():
    context = {"subscriber_name": "Anna", "unsubscribe_link": "https://x/unsub"}
    result = render_email("welcome.html", context)
    assert "Anna" in result
    assert "unsub" in result

def test_missing_required_field_raises():
    assert not validate_context({"subscriber_name": "Anna"})
```

## Przykładowe szablony
- **Welcome** – powitanie nowego subskrybenta
- **Confirmation** – potwierdzenie zapisu (double opt-in)
- **Newsletter** – cykliczny biuletyn z listą artykułów

## Reguły
- Nie osadzaj logiki biznesowej w szablonach – tylko wyświetlanie danych
- Waliduj kontekst przed renderowaniem
- Testuj każdy szablon osobno (happy path + brakujące pole)