# Use official slim Python image for reduced size
FROM python:3.11.0-slim-buster

# Set environment variables for stability and efficiency
ENV APP_HOME=/app \
  PYTHONDONTWRITEBYTECODE=1 \ 
  PYTHONUNBUFFERED=1 \
  PATH="/root/.local/bin:$PATH"

# Create application directory
WORKDIR $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles $APP_HOME/mediafiles

# Metadata labels
LABEL maintainer="pratik.shingade04@gmail.com"
LABEL description="Development image for Real Estate Project"
LABEL Author="Pratik Shingade"

# Install essential system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gettext \
    netcat \
    gcc \
    postgresql-client \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Upgrade pip to latest version
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy startup scripts and ensure proper permissions
COPY ./docker/local/django/entrypoint /entrypoint
COPY ./docker/local/django/start /start
COPY ./docker/local/django/celery/worker/start /start-celeryworker
COPY ./docker/local/django/celery/flower/start /start-flower

RUN chmod +x /entrypoint /start /start-celeryworker /start-flower

# Copy the application code
COPY . .

# Define entrypoint script
ENTRYPOINT ["/entrypoint"]
