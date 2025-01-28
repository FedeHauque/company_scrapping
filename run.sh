#!/bin/bash
# file: run.sh

if [ ! -d env ]; then
    python -m venv env
fi
source ./env/Scripts/activate
python -m pip install -r requirements.txt
python -m playwright install
python scrapper.py