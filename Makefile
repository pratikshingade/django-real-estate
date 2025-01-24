ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env
else
$(error ".env file not found! Please create one or ensure it exists in the project root.")
endif

# Variables
COMPOSE = docker compose
API_CONTAINER = api
DB_CONTAINER = postgres-db
DB_VOLUME = estate-src_postgres_data
EXCLUDE_FOLDERS = "(migrations|real_estate_env)"
# Default Target
.DEFAULT_GOAL := help

# Targets
.PHONY: help build up down show-logs migrate makemigrations superuser collectstatic down-v volume estate-db test test-html flake8 black-check black-diff black isort-check isort-diff isort clean

help:
	@echo "Available commands:"
	@echo "  build           Build and start the containers"
	@echo "  up              Start the containers in detached mode"
	@echo "  down            Stop and remove containers"
	@echo "  show-logs       Display logs from all containers"
	@echo "  migrate         Apply database migrations"
	@echo "  makemigrations  Create new database migrations"
	@echo "  superuser       Create a Django superuser"
	@echo "  collectstatic   Collect static files"
	@echo "  down-v          Stop and remove containers, including volumes"
	@echo "  volume          Inspect the database volume"
	@echo "  estate-db       Access the PostgreSQL database"
	@echo "  test            Run tests with pytest"
	@echo "  test-html       Run tests and generate an HTML coverage report"
	@echo "  flake8          Check Python code style with flake8"
	@echo "  black-check     Check code formatting with Black"
	@echo "  black-diff      Show differences for Black formatting"
	@echo "  black           Format code with Black"
	@echo "  isort-check     Check import order with isort"
	@echo "  isort-diff      Show differences for isort"
	@echo "  isort           Format imports with isort"
	@echo "  clean           Clean up unused Docker resources"

build:
	$(COMPOSE) up --build -d --remove-orphans

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

show-logs:
	$(COMPOSE) logs

migrate:
	$(COMPOSE) exec $(API_CONTAINER) python3 manage.py migrate

makemigrations:
	$(COMPOSE) exec $(API_CONTAINER) python3 manage.py makemigrations

superuser:
	$(COMPOSE) exec $(API_CONTAINER) python3 manage.py createsuperuser

collectstatic:
	$(COMPOSE) exec $(API_CONTAINER) python3 manage.py collectstatic --no-input --clear

down-v:
	$(COMPOSE) down -v

volume:
	$(COMPOSE) volume inspect $(DB_VOLUME)

estate-db:
	$(COMPOSE) exec $(DB_CONTAINER) psql --username=postgres --dbname=estate

test:
	$(COMPOSE) exec $(API_CONTAINER) pytest -p no:warnings --cov=.

test-html:
	$(COMPOSE) exec $(API_CONTAINER) pytest -p no:warnings --cov=. --cov-report html

flake8:
	$(COMPOSE) exec $(API_CONTAINER) flake8 .

black-check:
	$(COMPOSE) exec $(API_CONTAINER) black --check --exclude=$(EXCLUDE_FOLDERS) .


black-diff:
	$(COMPOSE) exec $(API_CONTAINER) black --diff --exclude=$(EXCLUDE_FOLDERS) .

black:
	$(COMPOSE) exec $(API_CONTAINER) black --exclude=$(EXCLUDE_FOLDERS) .

isort-check:
	$(COMPOSE) exec $(API_CONTAINER) isort . --check-only --skip env --skip migrations --skip real_estate_env


isort-diff:
	$(COMPOSE) exec $(API_CONTAINER) isort . --diff --skip env --skip migrations --skip real_estate_env


isort:
	$(COMPOSE) exec $(API_CONTAINER) isort . --skip env --skip migrations --skip real_estate_env


clean:
	@echo "Cleaning up unused Docker resources..."
	docker system prune -f --volumes
