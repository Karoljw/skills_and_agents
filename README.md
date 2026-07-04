# Mailer

Prosta aplikacja Python do zarządzania listami mailowymi z interfejsem webowym opartym na Flask.

Projekt powstał na potrzeby ćwiczenia **"GitHub Copilot Skills, Agents i Instrukcje"** w ramach kursu *Narzędzia do automatyzacji budowy oprogramowania*.

## Opis

Mailer pozwala na:
- zarządzanie listą subskrybentów (dodawanie, usuwanie, wyświetlanie),
- wysyłkę wiadomości email do subskrybentów,
- walidację adresów email przed dodaniem do listy,
- obsługę przez prosty interfejs webowy (Flask).
## Struktura projektu

```
skills_and_agents/
├── mailer/                  # logika biznesowa
│   ├── __init__.py
│   ├── email_sender.py      # wysyłanie emaili
│   ├── subscribers.py        # zarządzanie subskrybentami
│   └── web.py                # aplikacja Flask
├── templates/                # szablony HTML (Flask, Jinja2)
├── static/                   # pliki CSS/JavaScript
├── tests/                    # testy jednostkowe (pytest)
├── .copilot/                 # konfiguracja GitHub Copilot (skills, dokumentacja)
├── .agents/                  # definicje agentów AI
├── copilot-instructions.md   # globalne wytyczne dla GitHub Copilot
├── requirements.txt          # zależności projektu
└── README.md                 # ten plik
```

## Wymagania

- Python 3.9+
- pip
## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/<twoja-nazwa>/skills_and_agents.git
cd skills_and_agents
```

2. Utwórz i aktywuj środowisko wirtualne:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

## Uruchomienie

```bash
python -m mailer.web
```

Aplikacja domyślnie dostępna pod `http://localhost:5000`.

## Testy

Projekt korzysta z `pytest`:

```bash
pytest tests/
```

Sprawdzenie pokrycia testami:

```bash
pytest --cov=mailer tests/
```

## Konfiguracja środowiska

Dane wrażliwe (np. dane serwera SMTP) należy przechowywać w pliku `.env` (nigdy niecommitowanym do repozytorium):

```
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=twoj_login
SMTP_PASSWORD=twoje_haslo
```

## GitHub Copilot – Skills i Agents
 
Projekt zawiera skonfigurowane wsparcie GitHub Copilot (globalne instrukcje, skille i agenci) ułatwiające pracę nad kodem, testami i dokumentacją. Szczegóły w [`.copilot/README.md`](.copilot/README.md).