
[Github Repository](https://github.com/charara-code/data-filter.git
)
# Install pipx

### Windows

```bash
py -m pip install --user pipx
```

### macOs and Linux

```bash
python3 -m pip install --user pipx
```

# Install poetry

```bash
pipx install poetry
```
Then run
```bash
poetry env activate
poetry install
```

to install dependencies into poetry's virtual environment.

# Run the CLI

cmd to run

```bash
poetry run python -m data-filter.main
```

After running the command you will enter CLI mode type `-h` to get usage instructions.

You can use the example files found in `examples/`

### Note

- Some features of sort and filter are implemented as functions in their respective classes but not integrated in the CLI, you can experiment with them in the `main.py` file or call said functions in their `if __name__ == "__main__"` block.

- There are still erorrs and bugs in the app, the CLI might not behave correctly.

- XML loader are implemented but CLI functionnalites like sort, filter, stats, etc... are not implemented.