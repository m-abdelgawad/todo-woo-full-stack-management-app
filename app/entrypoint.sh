#!/bin/sh

# Wait for database to start listening at port 5432
while ! nc -z db 5432; do
    echo "Database is not running yet. Will wait for 1 second."
    sleep 1
done

echo "Migrating database..."
python manage.py migrate

echo "Start running the application..."
gunicorn --access-logfile - --workers 3 --bind 0.0.0.0:8000 todowoo_website.wsgi:application
