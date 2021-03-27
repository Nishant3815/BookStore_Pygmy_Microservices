from app import app
from flask import request, jsonify
from app.utils import backend_healthcheck, search_topic, search_product 

@app.route('/health', methods=['GET'])
def health_check():
    response = backend_healthcheck()
    if response:
        return(jsonify({'healthy': True})), 200
    else:
        return(jsonify({'healthy': False})), 500

@app.route('/search',methods=['GET'])
def search():
    topic = request.args.get('topic',type=str)
    if (topic):
        result = search_topic(topic)
        if result:
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /search?topic=<search topic>'})), 400

@app.route('/lookup',methods=['GET'])
def lookup():
    book_id = request.args.get('id',type=int)
    if book_id:
        result = search_product(book_id)
        if result:
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /lookup?id=<book id>'})), 400

@app.route('/buy',methods=['POST'])
def buy():
    data = request.json
    if id in data:
        book_id = data['id']
        result = search_product(book_id)
        if result:
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /buy with payload {"id": 1}'})), 400
