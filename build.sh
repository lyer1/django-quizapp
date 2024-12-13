#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django

python manage.py makemigrations
python manage.py migrate