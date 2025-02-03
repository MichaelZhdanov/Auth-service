#!/bin/bash

# This script is used to start auth-pages 1 and 2 on node 1
cd auth-page
docker-compose up -d
cd ..
cd auth-page-2
docker-compose up -d