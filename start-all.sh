#!/bin/bash

# Start all services if they are already built
cd auth-page
docker-compose up -d
cd ..
cd auth-page-2
docker-compose up -d
cd ..
cd auth-page-3
docker-compose up -d
cd ..
cd auth-page-4
docker-compose up -d
cd ..