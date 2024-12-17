# solana-libs
Solana testing libs

### Requirements
- python : 3.11
- [uv](https://docs.astral.sh/uv/) : python package and project manager build in rust


### Installation
- Install python version & dependencies 
```bash
uv python install 3.11
uv venv --python 3.11
uv sync
```

### Checking
- Linting
```bash
uv run ruff check
uv run isort services tests main.py
```

- Testing
```bash
uv run pytest
```

### Running
- Run the main.py
```bash
uv run main.py
```