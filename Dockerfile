# =========================
# Stage 1: Builder
# =========================
FROM python:3.11-alpine AS builder

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev g++ make

# Set working directory
WORKDIR /app

# Copy requirements
COPY src/requirements.txt .

# Install Python dependencies to /root/.local
RUN pip install --no-cache-dir --user -r requirements.txt

# =========================
# Stage 2: Runtime
# =========================
FROM python:3.11-alpine

# Install runtime dependencies only
RUN apk add --no-cache libffi

# Set working directory
WORKDIR /app

# Copy app source
COPY src/dashboard.py .

# Copy installed Python packages from builder
COPY --from=builder /root/.local /root/.local

# Add Python packages to PATH
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
