# Agent-Template-Repo

A Python project for testing and developing AI agents with a modular architecture.

## Quick Start

### 1. Create and activate Python environment

```bash
uv venv --python 3.11
source .venv/bin/activate
```

### 2. Install dependencies

```bash
# Install all dependencies
uv pip install ".[all]"
```

## Project Structure

```
agent-template-repo/
├── app/
│   ├── agents/          # Agent implementations
│   ├── api/            # API endpoints
│   └── core/           # Core configuration
├── docs/               # Documentation
└── pyproject.toml      # Project configuration
```

## Development

### Adding Dependencies

```bash
# Add main dependencies
uv add requests

# Add development dependencies
uv add --optional dev pylint

# Add documentation dependencies
uv add --optional docs sphinx
```

### Running the Application

```bash
make dev
```

## Documentation

Build the documentation:

```bash
cd docs
make html
```