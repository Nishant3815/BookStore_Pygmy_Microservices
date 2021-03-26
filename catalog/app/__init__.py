import sqlite3, logging
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
        'console': { 
            'level': app.config['LOG_LEVEL'],
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': app.config['LOG_LEVEL'],
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': '/logs/' + app.config['DB_QUERY_LOG']
        }
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'file'],
            'level': app.config['LOG_LEVEL']           
        },
        'console': {
            'handlers': ['console'],
            'level': app.config['LOG_LEVEL']
        },
        'file': {
            'handlers': ['file'],
            'level': app.config['LOG_LEVEL']
        }
    }
}
dictConfig(LOGGING_CONFIG)
app.logfile    = logging.getLogger('file')
app.logconsole = logging.getLogger('console')

DATABASE = '/db/' + app.config['SQLITE_DB_NAME']

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    g.db = connect_db()
    with app.open_resource('/db/schema.sql', mode='r') as f:
        app.logconsole.info("Initializing database")
        for line in f:
            g.db.cursor().executescript(line.strip())
            app.logfile.info(line.strip())
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
