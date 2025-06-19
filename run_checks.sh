#!/bin/bash

FILE_PATH="ASD_FIRST/0/test_pyryght.py"

python3 -m black "$FILE_PATH"
python3 -m darker "$FILE_PATH"
python3 -m ruff check --fix "$FILE_PATH"
python3 -m mypy "$FILE_PATH"
python3 -m pylint "$FILE_PATH" --output-format=colorized
