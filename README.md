# Readwise MCP Server

An MCP server that provides comprehensive tools for interacting with Readwise.io highlights and notes.

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.14+-green.svg)](https://github.com/jlowin/fastmcp)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-red.svg)](https://docs.pydantic.dev/)

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Available Tools](#-available-tools)
- [Development](#-development)
- [Project Structure](#-project-structure)
- [Docker Deployment](#-docker-deployment)
- [Contributing](#contributing)

---

## Prerequisites

- **Python 3.13+** - Required for running the server
- **uv** - Fast Python package installer and resolver ([installation guide](https://github.com/astral-sh/uv))
- **Node.js** (optional) - For using MCP Inspector during development

---

## 🚀 Quick Start

### 1. Clone and Navigate to Project

```bash
  cd readwise-mcp
```

### 2. Install Dependencies

```bash
  make prepare-env
```

This installs all dependencies including development tools, respecting the lockfile for reproducible builds.

### 3. Configure Environment

```bash
  cp .env.example .env
```

Edit `.env` with your Katalon TestOps credentials and endpoints (see [Configuration](#-configuration) for details).

### 4. Start the Server

```bash
  make dev
```

The server will be available at: **`http://localhost:8000/mcp`**

### 5. Test with MCP Inspector (Optional)

Verify the server is working correctly:

```bash
  make start-inspector
```

Then connect to `http://localhost:8000/mcp` in the inspector interface.

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

| Variable                | Description              | Example                      |
|-------------------------|--------------------------|------------------------------|
| `SERVER_PORT`           | Port for the MCP server  | `8080`                       |
| `READWISE_API_BASE_URL` | Readwise.io base URL     | `https://readwise.io/api/v2` |
| `READWISE_API_KEY`      | Readwise.io access token | `<token>`                    |


---

## 🛠 Available Tools

#### Highlights

- `list_highlights` - Retrieve all Readwise highlights

---

## 🧪 Development

### Code Quality

```bash
# Lint and format code
make lint-and-format

# Type checking
make check-type
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html
```

### Development Workflow

1. Make changes to source code in `src/`
2. Run linters and type checkers to catch issues early
3. Write tests in `tests/unit/` or `tests/integration/`
4. Run test suite to verify changes
5. Format code before committing

---

## 🏗 Project Structure

```
readwise-mcp/
├── src/
│   ├── tools/                    # MCP tool implementations
│   │   └──highlight.py           
│   ├── models/                   # Data models & schemas
│   │   └── highlight.py
│   ├── middlewares/              # Custom middleware
│   ├── errors/                   # Custom errors
│   │   └── api_error.py
│   ├── utils/                    # Utility functions
│   │   └── http.py
│   ├── config.py                 # Configuration management
│   ├── server.py                 # FastMCP server setup
│   └── mcp_instance.py           # MCP instance
├── tests/
│   ├── unit/                     # Unit tests
│   └── integration/              # Integration tests
├── docs/                         # Additional documentation
├── Dockerfile                    # Multi-stage production build
├── docker-compose.yaml           # Container orchestration
├── pyproject.toml                # Python project metadata
└── README.md                     # This file
```

---

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
  # Build the image
docker build -t readwise-mcp .

# Run the container
docker run -p 8000:8000 --env-file .env readwise-mcp
```

### Using Docker Compose

```bash
  # Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Health Check

```bash
  curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

## Contributing

### Guidelines

1. Follow existing code style (enforced by `ruff`)
2. Add type hints to all functions
3. Write tests for new features
4. Update documentation as needed
5. Ensure all checks pass before submitting PRs