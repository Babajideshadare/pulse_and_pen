This document describes how to deploy the **Pulse & Pen** Django app to a production environment.

The steps below assume:

- A Linux server (Ubuntu/Debian-like)
- Python 3.11+
- A virtual environment
- Gunicorn (app server)
- Nginx (reverse proxy)

You can adapt these steps to platforms like Render, Railway, Heroku, etc.

---

## Pre‑requisites
**On your server, install:**
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip nginx git

---

1. **Clone your project**

cd /opt
sudo git clone <your-repo-url> pulsepen
sudo chown -R $USER:$USER pulsepen
cd pulsepen

Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install --upgrade pip
pip install -r requirements.txt

2. Configure Environment Variables
On the server, set:
export DJANGO_SECRET_KEY='your-production-secret-key'
export DJANGO_DEBUG='false'
export DJANGO_ALLOWED_HOSTS='your-domain.com,www.your-domain.com'

3. Update pulsepen/settings.py to read them:
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-insecure-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'true').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',') if not DEBUG else []

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

5. Apply migrations
python manage.py migrate

6. Collect static files
python manage.py collectstatic

7. Run the App with Gunicorn
source venv/bin/activate
gunicorn pulsepen.wsgi:application --bind 0.0.0.0:8000