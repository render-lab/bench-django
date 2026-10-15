# Seed: Django app

Minimal Django project (`config`) with `/` and `/health/`. Expects Postgres via
`DATABASE_URL` (falls back to sqlite locally). No deploy config.

```bash
pip install -r requirements.txt
DEBUG=1 python manage.py migrate
DEBUG=1 python manage.py runserver
```

## Production on Render

`render.yaml` defines a Python web service and private Postgres database in Oregon.
The service builds static files with WhiteNoise, applies database migrations in the
pre-deploy step, and runs Gunicorn. `/health/` checks database connectivity.

Production requires `SECRET_KEY` and `DATABASE_URL`. Debug mode defaults to off;
the Render hostname is automatically allowed. Set `ALLOWED_HOSTS` to add custom
domains. HTTPS redirects, secure cookies, and HSTS are enabled in production.

The initial deployment is provisioned through the Render API. The Blueprint is
the reproducible configuration for future setup; automatic Blueprint sync is not
enabled. Preserve existing secrets and connect the existing database if adopting
the Blueprint later.
