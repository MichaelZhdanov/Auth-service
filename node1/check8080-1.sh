#!/bin/bash

if nc -z localhost 8080; then
    exit 0
else
    exit 1
fi