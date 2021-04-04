from app import app
from flask import request, jsonify
from app.utils import backend_healthcheck, search_topic, search_product, buy_product
import datetime

@app.route('/health', methods=['GET'])
def health_check():
    response = backend_healthcheck()
    if response:
        return(jsonify({'healthy': True})), 200
    else:
        return(jsonify({'healthy': False})), 500

@app.route('/search',methods=['GET'])
def search():
    start_time = datetime.datetime.now()
    topic = request.args.get('topic',type=str)
    if (topic):
        result = search_topic(topic)
        if result:
            end_time = datetime.datetime.now()
            request_latency = ((end_time - start_time).microseconds / 100000)
            app.logconsole.info("Time taken for search: " + str(request_latency))
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /search?topic=<search topic>'})), 400

@app.route('/lookup',methods=['GET'])
def lookup():
    start_time = datetime.datetime.now()
    book_id = request.args.get('id',type=int)
    if book_id:
        result = search_product(book_id)
        if result:
            end_time = datetime.datetime.now()
            request_latency = ((end_time - start_time).microseconds / 100000)
            app.logconsole.info("Time taken for lookup: " + str(request_latency))
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /lookup?id=<book id>'})), 400

@app.route('/buy',methods=['POST'])
def buy():
    start_time = datetime.datetime.now()
    data = request.json
    if 'id' in data:
        book_id = data['id']
        result = buy_product(book_id)
        if result:
            end_time = datetime.datetime.now()
            request_latency = ((end_time - start_time).microseconds / 100000)
            app.logconsole.info("Time taken for buy: " + str(request_latency))
            return result, 200
        else:
            return 503
    else:
        return(jsonify({'error': 'API Usage is /buy with payload {"id": 1}'})), 400
