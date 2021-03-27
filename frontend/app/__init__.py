import logging
from flask import Flask
from config import Config
from logging.config import dictConfig

app = Flask(__name__)
app.config.from_object(Config)

LOGGING_CONFIG = { 
    'version': 1,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': { 
        'console': { 
            'level': app.config['LOG_LEVEL'],
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': app.config['LOG_LEVEL']           
        },
        'console': {
            'handlers': ['console'],
            'level': app.config['LOG_LEVEL']
        }
    }
}
dictConfig(LOGGING_CONFIG)
app.logconsole = logging.getLogger('console')

from app import views
