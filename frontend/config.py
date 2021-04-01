from os import environ


class Config:
    """Set configuration vars from env variables"""

    LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')
    CATALOG_SERVICE_ENDPOINT = environ.get('CATALOG_SERVICE_ENDPOINT', 'http://catalog:8080')
    ORDER_SERVICE_ENDPOINT = environ.get('ORDER_SERVICE_ENDPOINT', 'http://order:8080')