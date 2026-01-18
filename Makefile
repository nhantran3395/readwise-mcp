dev:
	@echo "Starting dev server..."
	uvicorn src.server:app --reload

lint-and-format:
	@echo "Running linter check..."
	ruff check --fix .

	@echo "Running formatter check..."
	ruff format .

check-type:
	@echo "Running type check..."
	pyrefly check . --verbose

start-inspector:
	@echo "Starting MCP Inspector..."
	npx @modelcontextprotocol/inspector

test-unit:
	@echo "Running unit tests"
	pytest .