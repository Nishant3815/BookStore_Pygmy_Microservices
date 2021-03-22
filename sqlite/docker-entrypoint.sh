#!/bin/sh

# Remove exiting db if exists
rm -f "$SQLITE_DB_NAME"

# Initializing new db with initial entries
sqlite3 "$SQLITE_DB_NAME" <<'HEREDOC'
    create table books(id INTEGER PRIMARY KEY, name TEXT, topic TEXT, cost INTEGER, stock INTEGER);
HEREDOC

