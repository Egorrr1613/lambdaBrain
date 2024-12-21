#!/bin/bash

FILE_PATH="1_4_ASD/1/1_8.py"

python -m black "$FILE_PATH"
python -m darker "$FILE_PATH"
python -m ruff check --fix "$FILE_PATH"
python -m mypy "$FILE_PATH"
python -m pylint "$FILE_PATH" --output-format=colorized
