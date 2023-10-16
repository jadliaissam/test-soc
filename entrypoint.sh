#!/bin/sh

# make database migrations
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

# Collect static files (if needed)
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn socotec.wsgi:application --bind 0.0.0.0:8000