# Seed: Django app

Minimal Django project (`config`) with `/` and `/health/`. Expects Postgres via
`DATABASE_URL` (falls back to sqlite locally). No deploy config.

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
