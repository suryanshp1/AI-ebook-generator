#!/bin/bash

# Start the Gunicorn server with 4 worker processes using UvicornWorker and bind to 0.0.0.0:8000
gunicorn app.main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000
