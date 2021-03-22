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
        'default': { 
            'level': app.config['LOG_LEVEL'],
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': { 
        '': {
            'handlers': ['default'],
            'level': app.config['LOG_LEVEL']
        }
    }
}
dictConfig(LOGGING_CONFIG)

from app import views
