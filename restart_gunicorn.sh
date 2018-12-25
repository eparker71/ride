#!/usr/bin/bash
ps -ef | grep gunicorn | awk '{print $2}' | xargs -n 1 kill
gunicorn --workers=2 ride.wsgi:application --bind 0.0.0.0:8000 -D

