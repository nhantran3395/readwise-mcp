dev:
	uvicorn src.server:app --reload

lint-and-format:
	ruff check --fix .
	ruff format .

type-check:
	pyrefly check . --verbose