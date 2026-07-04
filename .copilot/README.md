# GitHub Copilot Configuration for Mailer

## Instrukcje (Instructions)
- `copilot-instructions.md` – Globalne standardy projektu (Python, PEP 8, testy, bezpieczeństwo, git)

## Skills (Umiejętności)
1. **email-validation** – Walidacja adresów email
2. **mailer-complete-testing** – Kompletne testowanie wszystkich komponentów mailera
3. **email-templates** – Tworzenie i testowanie szablonów emaili (HTML/plain text, dziedziczenie, podstawianie zmiennych)

Użycie:
```
@copilot use email-validation skill
```

## Agenci (Agents)
1. **docs-generator-agent** – Generowanie dokumentacji

Użycie:
```
Generate API documentation for mailer.subscribers module
```

## Workflow
1. Developer pisze kod
2. Copilot sugeruje pattern z odpowiedniego skill
3. Dev generuje testy używając skill
4. Docs generator tworzy dokumentację
5. Code reviews wspierane instrukcjami

## Best Practices
- Zawsze patrz na instrukcje przed rozpoczęciem
- Użyj skill jeśli dostępny
- Agenci dla złożonych, wieloetapowych zadań