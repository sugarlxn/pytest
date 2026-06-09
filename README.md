# pytest template 

## setup
1. setup python env with uv
```shell
uv sync 
```

## start
1. run all test
```shell
uv run pytest
```

2. run specify test_*.py
```shell
uv run pytest test_math.py
```

3. run the specify function in test_*.py
```shell
uv run pytest test_math.py::test_add
```

4. show the detail output 
```shell
uv run pytest -v 
```
