# Pulse & Pen – Week 1 Progress

This repository contains **Pulse & Pen**, a Django project for tracking blood pressure readings and related lifestyle notes (sleep, exercise, stress, etc.). The long‑term goal is to help users and, eventually, doctors see how daily habits affect blood pressure.

This note describes what has been implemented **so far (Week 1)**.

## Project Overview
- **Tech stack**
  - Python 3.12
  - Django
- **Project name:** `pulse_and_pen`
- **Main app:** `heartline`

The project is currently focused on **server-rendered HTML pages** using Django templates. API work (DRF, JWT, etc.) will come in later weeks.

### Key files
- `heartline/views.py`
  - `FAKE_BP_ENTRIES`: in-memory list of sample BP records.
  - `home(request)`: passes `bp_entries` to `home.html`.
  - `bp_detail(request, entry_id)`: finds one entry by `id` and passes it to `bp_detail.html` (404 if not found).

- `heartline/urls.py`
  - `/` → `home`
  - `/bp/<int:entry_id>/` → `bp_detail`

- Templates in `templates/`:
  - `base.html` – shared layout and simple styling.
  - `home.html` – list of sample entries.
  - `bp_detail.html` – details for a single entry.

## How to run locally
```bash
python -m venv .venv
source .venv/Scripts/activate

pip install django

python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000/ for the list.
Visit http://127.0.0.1:8000/bp/1/ (or 2, 3…) for details.

  Next steps (Week 2)
Create a real BPEntry model and migrate the database.
Register BPEntry in Django admin.
Replace the fake list with real database queries.
Add basic create/update/delete forms for BP entries.
