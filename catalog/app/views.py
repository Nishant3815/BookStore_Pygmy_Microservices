from app import app
from flask import jsonify
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
    topic = requests.args.get('topic',type='str')
    book_id = requests.args.get('id',type='int')
    if topic:
        print("Searching for the given topic.....")
        books = query_db('select name,id from books where topic='+str(topic))
        app.logfile.info('select name,id from books where topic='+str(topic))
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
    id_book = requests.json['id']
    #delta   = requests.json.get('delta')
    #cost_updated    = requests.json.get('cost_updated')
    
    ###### Making Updates to the stocks######
    # Update the query in the database below
    stock_count = query_db('select stock from books where id='+str(id_book))
    app.logfile.info('select stock from books where id='+str(id_book))
    upd_stock_count = stock_count-delta
    # Make changes to the database below
    upd = query_db('update books set stock='+str(upd_stock_count)+'where id='+str(id_book))
    app.logfile.info('update books set stock='+str(upd_stock_count)+'where id='+str(id_book))
    
    ###### Making Updates to the cost of items######
    upd_cost = query_db('update books set cost='+str(cost_updated)+'where id='+str(id_book))
    app.logfile.info('update books set cost='+str(cost_updated)+'where id='+str(id_book))
    ################################################
    
    # Not sure what should be returned..these are update operations only 
    return ("Updated the Pygmy Store database")


       
    
    