from app import app
from flask import request, jsonify
from app.utils import purchase_product
import datetime

@app.route('/health', methods=['GET'])
def health_check():
    """
    Route to do check health of application
    """

    return(jsonify({'healthy': True})), 200

@app.route('/purchase',methods=['POST'])
def purchase():
    start_time = datetime.datetime.now()
    data = request.json
    if 'id' in data:
        book_id = data['id']
        result = purchase_product(book_id)
        if result:
            end_time = datetime.datetime.now()
            request_latency = ((end_time - start_time).microseconds / 100000)
            app.logconsole.info("Time taken for buy: " + str(request_latency))
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /purchase with payload {"id": 1}'})), 400
    
    
