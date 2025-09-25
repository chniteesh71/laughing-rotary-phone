# Use Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY src/requirements.txt .
COPY src/dashboard.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Set environment to avoid prompts
ENV PYTHONUNBUFFERED=1

# Run Streamlit
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
