#!/usr/bin/env bash
#
# Script that runs an ephemeral ('removes the container after it gets stopped')
# Docker container with the Jupyter notebook and Python.
# Should be saved in the directory where the course files have been saved and
# started from within it.

docker run \
  -ti \
  --rm \
  -p 8888:8888 \
  -v "$PWD":/home/jovyan blazejtooploox/programming_basics_docker:latest
