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
        ## Update database query line here, to be written in utils
        end_time  = time.time()
        
    return None #Jsonified item after database query

@app.route('/lookup',methods=['GET'])
def lookup():
    id_book = request.args.get('id',type='int')
    if id_book:
        print("Searching for the given id from the database...")
        start_time = time.time()
        ## Update database query line here, to be written in utils
        end_time = time.time()
    
    return None #Jsonified item after database query

@app.route('/buy',methods=['GET'])
def buy():
    id_book = request.args.get('id',type='int')
    if id_book:
        print("Initiating a buy request for the given item")
        start_time = time.time()
        ## Update request to order microservice line here, functioonality in order to be updated 
        req = requests.get("http://order:8080/purchase")
        end_time = time.time()
        return (jsonify(req.text)), 200

        
        
    
        
    
