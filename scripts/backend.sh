#!/bin/sh

# server
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python server.py