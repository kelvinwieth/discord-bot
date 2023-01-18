#!/bin/bash

docker ps -f name=my_bot -q | xargs --no-run-if-empty docker container stop
docker container ls -a -fname=my_bot -q | xargs -r docker container rm
docker run -d -e MY_TOKEN=$MY_TOKEN --name my_bot my_bot:latest
docker system prune -f
