#!/bin/sh
echo 'Collecting static files...'
python manage.py collectstatic --no-input
echo 'Checking postgres...'
postgres-healthcheck
echo 'Setting up db...'
python manage.py makemigrations
python manage.py migrate
python manage.py create_admin
# python manage.py create_mock_users
# python manage.py loaddata industries.json
# python manage.py loaddata index.json
# python manage.py loaddata about
# python manage.py loaddata testimonials
# python manage.py loaddata posts
python manage.py train
echo 'Running server...'
python manage.py runserver 0.0.0.0:8080
exec "$@"