# Trajectoires

High-school alumni directory — built with Django, Tailwind CSS and HTMX as an open-source Security-by-Design / DevSecOps teaching project.

## Requirements

- Python 3.13+

## Setup

```bash
git clone https://github.com/LucasJeanpierre/Trajectoires.git
cd Trajectoires

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt -r requirements-dev.txt

python manage.py migrate
python manage.py createsuperuser
```

## Run locally

```bash
python manage.py tailwind runserver
```

## Pre-commit hooks

Runs Ruff (lint/format) and Gitleaks (secret scanning) automatically on every commit:

```bash
pre-commit install
```
