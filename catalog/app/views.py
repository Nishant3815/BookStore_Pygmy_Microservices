from app import app
from flask import request, jsonify
from app.utils import db_healthcheck, query_db
import time

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

@app.route('/querydb',methods=['GET'])
def make_lookup_db():
    
    start_time = time.time()
    topic = request.args.get('topic',type=str)
    book_id = request.args.get('id',type=int)
    if topic:
        app.logger.info("Searching for the given topic....." + topic)
        books = query_db('select id,name from books where topic="'+str(topic) + '"')
        app.logfile.info('select id,name from books where topic='+str(topic))
        print("Logged query related to the topic")
        return jsonify(books)
    
    elif (book_id):
        print("Searching for the given id....")
        book_data = query_db('select * from books where id='+str(book_id))
        app.logfile.info('select * from books where topic='+str(book_id))
        print("Logged query related to id of the book")
        return jsonify(book_data)
    else:
        print("Topic/ID not found. Please consider modifying your search query")

@app.route('/updatedb',methods=['POST'])
def update_stock():
    start_time = time.time()
    book_id = request.json['id']
    #delta   = requests.json.get('delta')
    #cost_updated    = requests.json.get('cost_updated')
    
    ###### Making Updates to the stocks######
    # Update the query in the database below
    stock_query = query_db('select stock from books where id='+str(book_id))
    app.logfile.info('select stock from books where id='+str(book_id))
    updated_stock_count = stock_query[0]['stock'] - 1
    # Make changes to the database below
    update_query = query_db('update books set stock='+str(updated_stock_count)+' where id='+str(book_id))
    app.logfile.info('update books set stock='+str(updated_stock_count)+' where id='+str(book_id))
    app.logconsole.info(update_query)
    ###### Making Updates to the cost of items######
    #upd_cost = query_db('update books set cost='+str(cost_updated)+'where id='+str(id_book))
    #app.logfile.info('update books set cost='+str(cost_updated)+'where id='+str(id_book))
    ################################################
    
    return(jsonify({'buy': True})), 200 
