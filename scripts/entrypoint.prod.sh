#!/bin/sh
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata industries.json
python manage.py create_admin
gunicorn -b 0.0.0.0:8500 core.wsgi:application --timeout 90
exec "$@"