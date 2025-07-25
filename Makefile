dev:
	uv run uvicorn app.main:app --reload

lint:
	uv run pylint app

format-preview:
	uv run yapf --diff --recursive app

format:
	uv run yapf --in-place --recursive app