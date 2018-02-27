#!/bin/sh
./manage.py collectstatic --noinput
./manage.py loaddata apps/rooms/fixtures/test_user.json

until python manage.py migrate; do
  >&2 echo "Postgres database is unavailable - sleeping"
  sleep 1
done

gunicorn config.wsgi:application --workers 2 --bind :8000
