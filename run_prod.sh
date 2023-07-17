#!/bin/bash

# Stopping running server instance if exists
kill -9 $(lsof -t -i:8000)

# Run server at background
nohup DEBUG=False python3 manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1&