#!/bin/bash

pkill gunicorn

. portal_env/bin/activate
cd app
gunicorn -w 4 -b 0.0.0.0:4000 app:app --access-logfile ../log/access.log -D

