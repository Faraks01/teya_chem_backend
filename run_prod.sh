#!/bin/bash

# Stopping running server instance if exists
PID=$(lsof -t -i:8000)

if [ -n "${PID}" ]; then
    echo "Stopping instance at pid: $PID"
    sudo kill -9 $PID
fi

# Run server at background
DEBUG=False nohup python3 manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1&