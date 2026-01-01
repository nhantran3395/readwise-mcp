FROM python:3.13.2-slim AS builder

WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

FROM python:3.13.2-slim AS production

WORKDIR /app
RUN groupadd -g 10001 user \
  && useradd -u 10001 -g user -s /bin/sh -m user \
  && chown -R 10001:10001 /app

COPY --chown=user:user --from=builder /app/.venv /app/.venv
COPY --chown=user:user src /app/src

USER user
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]
