#!/bin/bash

# Step 1: Take down the Docker Compose setup
echo "Stopping and removing containers, networks, and volumes..."
docker-compose down --volumes --remove-orphans

# Step 2: Prune unused Docker resources (images, build cache, volumes)
echo "Pruning unused Docker resources..."
docker system prune -a --volumes -f

# Step 3: Bring up the Docker Compose services
echo "Starting the Docker Compose services..."
docker-compose up 

echo "Docker Compose services are up and running."
