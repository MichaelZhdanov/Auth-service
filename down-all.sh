#!/bin/bash

# Immediate shutdown of all services
cd auth-page
docker-compose down
cd ..
cd auth-page-2
docker-compose down
cd ..
cd auth-page-3
docker-compose down
cd ..
cd auth-page-4
docker-compose down
cd ..