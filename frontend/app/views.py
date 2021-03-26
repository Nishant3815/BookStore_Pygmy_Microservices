from app import app
from flask import jsonify
from app.utils import backend_healthcheck
import time 

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
    retrieve_topic = request.args.get('topic',type=str)
    if (topic):
        print("Searching for the given topic from the database...")
        start_time = time.time()
        req = requests.args.get("http://catalog:8080/querydb?topic="+str(topic))
        end_time  = time.time()
        
    return (jsonify(req.text)), 200 

@app.route('/lookup',methods=['GET'])
def lookup():
    id_book = request.args.get('id',type='int')
    if id_book:
        print("Searching for the given id from the database...")
        start_time = time.time()
        req = requests.args.get("http://catalog:8080/querydb?id="+str(id_book))
        end_time = time.time()
    
    return (jsonify(req.text)), 200

@app.route('/buy',methods=['POST'])
def buy():
    data = request.json
    id_book = data['id']
    if id_book:
        print("Initiating a buy request for the given item")
        start_time = time.time()
        ## Update request to order microservice line here, functioonality in order to be updated 
        req = requests.get("http://order:8080/purchase") #payload 
        end_time = time.time()
        return (id_book), 200

        
        
    
        
    
