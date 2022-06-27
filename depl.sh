#!/bin/bash

set -e

DOCKER_IMAGE="shakilahmmeed/boigram"
CONTAINER_NAME="boigram"
ENV_FILE="./.env"
PORT="8088"


echo "Deploying $DOCKER_IMAGE to Docker Container..........."

if [ $(docker inspect -f '{{.State.Running}}' $CONTAINER_NAME) = "true" ]; then
    echo "Stopping Existing Container.........."
    docker stop $CONTAINER_NAME
fi


docker rm $CONTAINER_NAME

echo "Updating Docker Image........."
docker pull $DOCKER_IMAGE


echo "Starting $CONTAINER_NAME using Docker Image name: $DOCKER_IMAGE ............."

docker run --name $CONTAINER_NAME \
           --mount source=$CONTAINER_NAME,target=/app \
           --restart unless-stopped \
           --env-file $ENV_FILE -d \
           -p $PORT:8000 $DOCKER_IMAGE

docker exec -it $CONTAINER_NAME python manage.py migrate
docker ps -a