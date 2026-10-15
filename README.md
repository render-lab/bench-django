# Seed: Django app

Minimal Django project (`config`) with `/` and `/health/`. Expects Postgres via
`DATABASE_URL` (falls back to sqlite locally). No deploy config.

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Production runs on Render with Gunicorn and managed PostgreSQL. Set `DEBUG=0`,
`SECRET_KEY`, and `DATABASE_URL`; the Render hostname is allowed automatically.
For custom domains, set `ALLOWED_HOSTS` to a comma-separated list of hostnames.

`render.yaml` describes the production resources. Builds install requirements and
collect static files; the pre-deploy command applies database migrations.
The HTTP health check is `/health/`.
