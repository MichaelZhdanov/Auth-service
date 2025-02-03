#!/bin/bash

# Use it to build all the services for the first time
cd auth-page
docker-compose up -d --build
cd ..
cd auth-page-2
docker-compose up -d --build
cd ..
cd auth-page-3
docker-compose up -d --build
cd ..
cd auth-page-4
docker-compose up -d --build
cd ..