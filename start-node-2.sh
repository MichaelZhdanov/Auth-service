#!/bin/bash

# This script is used to start auth-pages 3 and 4 on node 2
cd auth-page-3
docker-compose up -d
cd ..
cd auth-page-4
docker-compose up -d