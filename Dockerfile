# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app
COPY src/requirements.txt .

RUN apt-get update && apt-get install -y build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app
COPY src/dashboard.py .
COPY --from=builder /usr/local /usr/local

EXPOSE 8501
ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
