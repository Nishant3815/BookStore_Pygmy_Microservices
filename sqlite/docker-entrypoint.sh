#!/bin/sh

# Remove exiting db if exists
rm -f "$SQLITE_DB_NAME"

sqlite3 "$SQLITE_DB_NAME" "VACUUM;"
chmod 666 "$SQLITE_DB_NAME"

exec tail -f /dev/null

