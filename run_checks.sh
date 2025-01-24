#!/bin/bash

FILE_PATH="1_4_ASD/2/dummy_node_in_list.py"

python3 -m black "$FILE_PATH"
python3 -m darker "$FILE_PATH"
python3 -m ruff check --fix "$FILE_PATH"
python3 -m mypy "$FILE_PATH"
python3 -m pylint "$FILE_PATH" --output-format=colorized
