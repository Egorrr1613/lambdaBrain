#!/bin/bash

FILE_PATH="ASD_SECOND/lesson_4_aBST/"

# python3 -m black "$FILE_PATH"
# python3 -m darker "$FILE_PATH"
python3 -m ruff check --fix "$FILE_PATH"
python3 -m mypy "$FILE_PATH"
python3 -m pylint "$FILE_PATH" --output-format=colorized

python3 -m pytest --cov="$FILE_PATH" --ignore=ASD_FIRST --cov-report=html