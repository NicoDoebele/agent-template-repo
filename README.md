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

## CI/CD

### Docker Build Workflow

This project includes a GitHub Actions workflow that automatically builds and pushes Docker images to Docker Hub when code is pushed to the main branch.

#### Setup Required

1. **GitHub Container Registry**: The workflow automatically uses GitHub's built-in container registry (ghcr.io)
2. **Repository Permissions**: Ensure the workflow has permission to write packages in your repository settings
3. **Package Visibility**: Set your package visibility in repository settings (public/private)

#### Workflow Behavior

- **On push to main**: Builds and pushes the image with tags:
  - `latest`
  - `main`
  - `sha-{commit_hash}`