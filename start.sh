#!/usr/bin/env bash

trap "kill 0" EXIT

echo "Starting backend..."
cd backend || exit
source venv/bin/activate
uvicorn app.main:app --reload &
BACKEND_PID=$!

echo "Starting frontend..."
cd ../frontend || exit
npm run dev &
FRONTEND_PID=$!

wait
