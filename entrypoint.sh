#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell < /create_superuser.py
python3 manage.py runserver 0.0.0.0:8000