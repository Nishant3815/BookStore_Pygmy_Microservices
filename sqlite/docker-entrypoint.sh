#!/bin/sh

# Remove exiting db if exists
rm -f "$SQLITE_DB_NAME*"

sqlite3 "$SQLITE_DB_NAME" "VACUUM;"

exec tail -f /dev/null

