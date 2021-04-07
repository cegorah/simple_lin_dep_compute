#!/bin/bash
pip3 install -r requirements.txt
python3 manage.py runserver --host=0.0.0.0 --port=8080