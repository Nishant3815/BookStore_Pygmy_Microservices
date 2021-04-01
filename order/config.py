from os import environ


class Config:
    """Set configuration vars from env variables"""

    LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')
    DB_QUERY_LOG = environ.get('DB_QUERY_LOG', 'order.log')
    CATALOG_SERVICE_ENDPOINT = environ.get('CATALOG_SERVICE_ENDPOINT', 'http://catalog:8080')