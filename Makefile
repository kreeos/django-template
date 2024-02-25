# Define the Docker Compose command
DOCKER_COMPOSE := docker-compose

# Run the Django development server
up:
	$(DOCKER_COMPOSE) up

# Build new image
build:
	$(DOCKER_COMPOSE) build

# # Run Django database migrations
# migrate:
# 	$(DOCKER_COMPOSE) run --rm web python manage.py migrate

# # Create a new Django superuser
# createsuperuser:
# 	$(DOCKER_COMPOSE) run --rm web python manage.py createsuperuser

# # Collect static files
# collectstatic:
# 	$(DOCKER_COMPOSE) run --rm web python manage.py collectstatic

# # Run tests
# test:
# 	$(DOCKER_COMPOSE) run --rm web python manage.py test

# # Clean up Docker containers and volumes
# clean:
# 	$(DOCKER_COMPOSE) down -v
