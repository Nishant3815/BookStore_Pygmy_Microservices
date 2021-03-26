from app import app
from flask import request, jsonify
from app.utils import backend_healthcheck
import time, requests, json 

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

@app.route('/search',methods=['GET'])
def search():
    topic = request.args.get('topic',type=str)
    if (topic):
        print("Searching for the given topic from the database...")
        start_time = time.time()
        req = requests.get("http://catalog:8080/querydb?topic="+str(topic))
        end_time  = time.time()
        
    return (jsonify(req.text)), 200 

@app.route('/lookup',methods=['GET'])
def lookup():
    id_book = request.args.get('id',type=int)
    if id_book:
        print("Searching for the given id from the database...")
        start_time = time.time()
        req = requests.get("http://catalog:8080/querydb?id="+str(id_book))
        end_time = time.time()
    
    return (jsonify(req.text)), 200

@app.route('/buy',methods=['POST'])
def buy():
    data = request.json
    book_id = data['id']
    app.logger.info("Got request to buy book " + str(book_id))
    if book_id:
        print("Initiating a buy request for the given item")
        start_time = time.time()
        ## Update request to order microservice line here, functioonality in order to be updated 
        update_url = 'http://order:8080/purchase'
        payload = {'id': book_id}
        response = requests.post(update_url, json=payload) 
        end_time = time.time()
        return (response.json()), 200
