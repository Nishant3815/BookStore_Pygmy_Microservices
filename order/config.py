from os import environ


class Config:
    """Set configuration vars from env variables"""

    LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')
    DB_QUERY_LOG = environ.get('DB_QUERY_LOG', 'catalog.log')