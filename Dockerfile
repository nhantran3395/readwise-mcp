FROM python:3.13-alpine AS builder
WORKDIR /app
RUN pip install uv
COPY . .
RUN uv sync --no-dev \
  && uv run opentelemetry-bootstrap -a requirements > requirements.txt \
  && uv pip install -r requirements.txt


FROM python:3.13-alpine AS production
WORKDIR /app

RUN addgroup -g 10001 user \
  && adduser -u 10001 -G user -s /bin/sh -D user \
  && chown -R 10001:10001 /app

USER 10001

COPY --chown=10001:10001 --from=builder /app/.venv /app/.venv
COPY --chown=10001:10001 --from=builder /app/src /app/src

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]