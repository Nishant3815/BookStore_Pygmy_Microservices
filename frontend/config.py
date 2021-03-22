from os import environ


class Config:
    """Set configuration vars from env variables"""

    LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')