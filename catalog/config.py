from os import environ


class Config:
    """Set configuration vars from env variables"""

    LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')
    SQLITE_DB_NAME = environ.get('SQLITE_DB_NAME', 'bookstore.db')
    DB_QUERY_LOG = environ.get('DB_QUERY_LOG', 'catalog.log')
