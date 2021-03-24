from os import environ


class Config:
    """Set configuration vars from env variables"""

    LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')
    INITIAL_CATALOG = environ.get('CATALOG', '[]')
    SQLITE_DB_NAME = environ.get('SQLITE_DB_NAME', 'bookstore.db')
