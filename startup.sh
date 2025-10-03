#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Start Gunicorn server
gunicorn --bind 0.0.0.0:8000 --workers 3 dimeji.wsgi:application
