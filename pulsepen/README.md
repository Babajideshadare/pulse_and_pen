# Pulse & Pen

A personal blood pressure and lifestyle tracking app built with **Django 6** and **Django REST Framework**.

Pulse & Pen lets each user:

- Log blood pressure readings (date, time, systolic, diastolic, pulse, notes)
- Log lifestyle/journal entries (sleep, exercise, diet, mood/stress)
- View a personal dashboard summarizing recent data
- Access the same data programmatically via a secure REST API (token-based auth)

---

## Features

### Blood Pressure Tracking

- Create, read, update, and delete BP entries:
  - Date
  - Time
  - Systolic / diastolic pressure
  - Pulse
  - Optional note
- All entries are **linked to the logged-in user** and cannot be seen by others.

### Lifestyle / Journal Tracking

- Create daily journal entries with:
  - Sleep hours and quality
  - Exercise type and duration
  - Diet notes
  - Mood / stress description
- Each entry is scoped to the authenticated user.

### Dashboard

- Login-required dashboard summarizing the current user’s data:
  - Total number of BP entries
  - Last 5 BP entries
  - Total number of journal entries
  - Last 5 journal entries

### Authentication & Profiles

- User registration (username + password)
- Login and logout (HTML forms)
- Simple profile page for updating email
- After login, users are redirected to the BP entries list

### REST API

- Token-based API built with Django REST Framework
- Endpoints for:
  - Blood pressure entries
  - Journal entries
- All API views:
  - Require authentication
  - Automatically scope queries to the authenticated user
  - Automatically attach `user` on create

---

## Tech Stack

- Python
- Django 6
- Django REST Framework
- SQLite (default development database)
- HTML templates + CSS (no frontend framework)

