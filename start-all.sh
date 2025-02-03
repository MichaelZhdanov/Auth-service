#!/bin/bash

# Start all services if they are already built
cd node1
docker-compose up -d
cd ..
cd node2
docker-compose up -d