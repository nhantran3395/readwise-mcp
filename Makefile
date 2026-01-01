dev:
	uvicorn src.server:app --reload

lint-and-format:
	ruff check --fix .
	ruff format .

check-type:
	pyrefly check . --verbose

start-inspector:
	npx @modelcontextprotocol/inspector