#!/bin/bash

# Use it to build all the services for the first time
cd node1
docker-compose up -d --build
cd ..
cd node2
docker-compose up -d --build