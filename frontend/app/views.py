from app import app
from flask import jsonify
# from app.utils import redis_healthcheck, redis_add_word, redis_autocomplete_word, validate_input


@app.route('/health', methods=['GET'])
def health_check():
    """
    Route to do check health of application
    """

    return(jsonify({'healthy': True})), 200
