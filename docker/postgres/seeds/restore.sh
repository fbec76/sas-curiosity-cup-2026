#!/bin/bash
set -e
if [ -f /docker-entrypoint-initdb.d/nba_stats.dump ]; then
  echo "Restoring nba_stats database from dump..."
  pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" /docker-entrypoint-initdb.d/nba_stats.dump
fi