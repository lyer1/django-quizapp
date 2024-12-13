#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django
pip install gunicorn uvicorn

python manage.py makemigrations
python manage.py migrate