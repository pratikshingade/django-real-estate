FROM python:3.11.0-slim-buster

# Set application directory
ENV APP_HOME=/app
RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

# Metadata
LABEL maintainer="pratik.shingade04@gmail.com"
LABEL description="Development image for Real Estate Project"

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gettext netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install requirements
RUN pip3 install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Copy entrypoint and startup scripts
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

# Set entrypoint and default command
ENTRYPOINT ["/entrypoint"]
CMD ["/start"]

# Add optional health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD nc -z localhost 8000 || exit 1
