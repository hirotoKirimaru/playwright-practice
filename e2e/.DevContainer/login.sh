#!/bin/bash

docker run -v /workspaces/playwright-practice/e2e:/var/scenario -it playwright-python:latest /bin/bash