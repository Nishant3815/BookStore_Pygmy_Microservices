from app import app
from flask import jsonify
from app.utils import backend_healthcheck

@app.route('/health', methods=['GET'])
def health_check():
    """
    Route to do check health of application
    """

    response = backend_healthcheck()
    if response:
        return(jsonify({'healthy': True})), 200
    else:
        return(jsonify({'healthy': False})), 500

