#!/bin/bash
# file: run.sh

python -m venv env
source ./env/Scripts/activate
python -m pip install -r requirements.txt
python -m playwright install
python scrapper.py