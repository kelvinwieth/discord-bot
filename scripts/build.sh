#!/bin/bash

DOCKERFILE_PATH=$1

docker build -t my_bot:latest $DOCKERFILE_PATH
