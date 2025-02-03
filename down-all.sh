#!/bin/bash

# Immediate shutdown of all services
cd node1
docker-compose stop
cd ..
cd node2
docker-compose stop