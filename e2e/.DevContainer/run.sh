#!/bin/bash

# docker run -v /workspaces/playwright-practice:/var/scenario -it playwright-python:latest /bin/bash
# 落として、上げて、再度落とす

docker-compose down
docker-compose up -d
docker-compose down