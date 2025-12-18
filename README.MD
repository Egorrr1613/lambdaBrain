
### Run format code:
```bash
./run_checks.sh
```

### Run tests:
```bash
 python -m pytest 28_task/*.py
```

### Collect coverage
Добавить в агрументы запуска `--cov=. --cov-report=html`

Или из cli:

```bash
python3 -m pytest --cov=ASD_SECOND/lesson_2_BST --ignore=ASD_FIRST --cov-report=html
```