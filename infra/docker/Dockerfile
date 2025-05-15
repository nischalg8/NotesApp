# Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements/ /app/requirements/
RUN pip install --user -r /app/requirements/prod.txt

# Runtime stage
FROM python:3.11-slim

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PATH="/root/.local/bin:$PATH"

# Copy installed Python packages from builder
COPY --from=builder /root/.local /root/.local

# Copy your source code
COPY alembic.ini /app/alembic.ini
COPY alembic/ /app/alembic/
COPY src/ /app/src/

# Optional: entrypoint
COPY infra/docker/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Gunicorn command
CMD ["gunicorn", "--chdir", "/app/src", "main:app", "--bind", "0.0.0.0:8000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker"]