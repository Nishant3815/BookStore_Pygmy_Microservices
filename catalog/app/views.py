from app import app
from flask import request, jsonify
from app.utils import db_healthcheck, query_product_details, update_product_details

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

@app.route('/query',methods=['GET'])
def query():
    topic = request.args.get('topic',type=str)
    book_id = request.args.get('id',type=int)

    if topic:
        result = query_product_details(topic, "search")
    elif book_id:
        result = query_product_details(book_id, "lookup")
    else:
        return(jsonify({'error': 'API Usage is /query?id|topic=<book id|topic>'})), 400
    
    if result:
        return result, 200
    else:
        return 503

@app.route('/update',methods=['POST'])
def update():
    data = request.json
    if 'id' in data:
        book_id = data['id']
        result = update_product_details(book_id)
        if result:
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /buy with payload {"id": 1}'})), 400
