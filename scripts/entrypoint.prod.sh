#!/bin/sh
python manage.py collectstatic --no-input
postgres-healthcheck
python manage.py makemigrations
python manage.py migrate
python manage.py create_admin
python manage.py loaddata industries.json
python manage.py loaddata carousel.json
python manage.py loaddata about
gunicorn -b 0.0.0.0:${PORT} core.wsgi:application --timeout 90
exec "$@"