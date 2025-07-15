#!/usr/bin/env bash

# Exit on any error
set -o errexit

# Build React frontend
cd frontend
npm install
npm run build

# Go back to root
cd ..

# Collect static files
python manage.py collectstatic --noinput
