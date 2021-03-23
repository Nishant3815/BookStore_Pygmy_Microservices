from app import app
from flask import jsonify


@app.route('/health', methods=['GET'])
def health_check():
    """
    Route to do check health of application
    """

    return(jsonify({'healthy': True})), 200

