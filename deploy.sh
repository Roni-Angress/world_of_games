#!/bin/bash

# Build and run the application
docker-compose up --build -d

# Tag the image
docker tag world_of_games-web:latest roniangress/world_of_games-web:latest

# Push the image to Docker Hub
docker push roniangress/world_of_games-web:latest
