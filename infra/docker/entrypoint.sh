#!/bin/bash

echo "Waiting for PostgreSQL to be ready..."

until pg_isready -h db -p 5432 -U user; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Database is up! Starting application..."
exec "$@"
