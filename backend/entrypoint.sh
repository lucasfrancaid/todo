#!/bin/bash

./manage.py makemigrations --noinput
./manage.py migrate

exec "$@"