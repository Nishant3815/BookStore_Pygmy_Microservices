from app import app
from flask import jsonify
from app.utils import db_healthcheck, query_db

@app.route('/health', methods=['GET'])
def health_check():
    """
    Route to do check health of application
    """
    response = db_healthcheck()
    if response:
        return(jsonify({'healthy': True})), 200
    else:
        return(jsonify({'healthy': False})), 500