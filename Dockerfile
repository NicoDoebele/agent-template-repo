FROM python:3.11


WORKDIR /code

# Install uv
RUN pip install uv

# Copy dependency files
COPY ./pyproject.toml /code/pyproject.toml
COPY ./uv.lock /code/uv.lock

# Install dependencies using uv
RUN uv sync --frozen

# Copy application code
COPY ./app /code/app

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]