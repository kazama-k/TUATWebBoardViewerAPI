#!/usr/bin/env bash

echo "Apply database migrations"
python3 manage.py makemigrations
python3 manage.py sqlmigrate article 0001_initial
python3 manage.py migrate

echo "Starting Server"
python3 manage.py runserver 0.0.0.0:8000
