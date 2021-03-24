import sqlite3
from flask import g, Flask
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

DATABASE = '/db/' + app.config['SQLITE_DB_NAME']

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    g.db = connect_db()
    with app.open_resource('/db/schema.sql', mode='r') as f:
        app.logger.info("Initializing database")
        g.db.cursor().executescript(f.read())
    g.db.commit()
    if hasattr(g, 'db'):
        g.db.close()

with app.app_context():
    init_db()

@app.before_request
def before_request():
    g.db = connect_db()
    
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


from app import views
