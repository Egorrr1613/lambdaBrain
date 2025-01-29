#!/bin/bash

FILE_PATH="1_4_ASD/2/12/standard_bubble_sort_one_dummy.py"

python3 -m black "$FILE_PATH"
python3 -m darker "$FILE_PATH"
python3 -m ruff check --fix "$FILE_PATH"
python3 -m mypy "$FILE_PATH"
python3 -m pylint "$FILE_PATH" --output-format=colorized
