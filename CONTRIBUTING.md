# Contributing

## Development Setup

This project uses `uv` for dependency management. Install it first:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install dependencies:

```bash
uv sync
```

## Code Style

This project follows the **Google Python Style Guide**. We use:

- **Pylint** for linting (`pylint>=3.3.7`)
- **YAPF** for code formatting (`yapf>=0.43.0`)

### Running Linting and Formatting

```bash
# Lint the codebase
make lint

# Preview formatting changes
make format-preview

# Apply formatting
make format
```

## Documentation

Documentation is built with **Sphinx** (`sphinx>=8.2.3`) using the **Read the Docs theme** (`sphinx-rtd-theme>=3.0.2`).

### Building Docs

```bash
cd docs
make html
```

The docs will be generated in `docs/build/html/`.

### Docstring Style

Use Google-style docstrings (enabled in Sphinx config):

```python
def my_function(param1: str, param2: int) -> bool:
    """Short description of function.

    Longer description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When something goes wrong
    """
    pass
```

## Development Server

Run the development server:

```bash
make dev
```

This starts the FastAPI server with auto-reload at `http://localhost:8000`.

## Template Usage

**Important**: This is a template repository. When using this as a starting point for your own project:

1. **Replace the project name** in `pyproject.toml`:
   ```toml
   name = "your-project-name"
   ```

2. **Update documentation** in `docs/source/conf.py`:
   ```python
   project = 'your-project-name'
   copyright = '2025, Your Name'
   author = 'Your Name'
   ```

3. **Update the README.md** with your project's specific information

4. **Replace the description** in `pyproject.toml` to match your project

5. **Update dependencies** as needed for your specific use case

## Project Structure

```
agent-test/
├── app/                    # Main application code
│   ├── agents/            # Agent implementations
│   ├── api/               # FastAPI endpoints
│   └── core/              # Core configuration
├── docs/                  # Sphinx documentation
├── pyproject.toml         # Project configuration
└── Makefile              # Development commands
```

## Dependencies

### Core Dependencies
- `fastapi>=0.116.1` - Web framework
- `uvicorn[standard]>=0.27.0` - ASGI server
- `pydantic-settings>=2.10.1` - Settings management
- `langchain>=0.3.27` - LLM framework
- `openai>=1.97.1` - OpenAI API client

### Development Dependencies
- `pylint>=3.3.7` - Code linting
- `yapf>=0.43.0` - Code formatting

### Documentation Dependencies
- `sphinx>=8.2.3` - Documentation generator
- `sphinx-rtd-theme>=3.0.2` - Documentation theme

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run linting and formatting: `make lint && make format`
5. Update documentation if needed
6. Submit a pull request

## Code Review Guidelines

- All code must pass Pylint checks
- Code must be formatted with YAPF
- New features should include tests
- Documentation should be updated for new features
- Follow Google Python Style Guide conventions
