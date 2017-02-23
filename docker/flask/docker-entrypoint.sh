#!/bin/bash
cd /app
pip install -r ./requirements.txt
uwsgi --ini ./uwsgi.ini