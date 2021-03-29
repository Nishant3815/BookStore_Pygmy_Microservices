from app import app
from flask import g, jsonify


def db_healthcheck() -> bool:
    """
    Checks if the sqlite database is reachable
    ---
    parameters: None
    returns: 
        - bool
            description: Indicates if health check passed or not
    """

    try:
        result = query_db("Select 1")
        app.logfile.info("Select 1")
        return True
    except ConnectionError as err:
        app.logger.error(err)
        return False

def query_product_details(query_key, query_type):
    """
    Searches for given query_key in the sqlite database
    ---
    parameters: 
        - name: query_key
          type: int
          required: true
          description: query_key to be searched in the db

        - name: query_type
          type: string
          required: true
          description: type of query this will change on if it was a lookup or a search
    returns: 
        - json
            description: All details regarding the available product/s
    """

    if query_type == "search":
        app.logconsole.info("Searching for products having topic: " + str(query_key))
        products = query_db('select id,name from books where topic="' + str(query_key) + '"')
        app.logfile.info('select id,name from books where topic=' + str(query_key))
        return jsonify(products)
    elif query_type == "lookup":
        app.logconsole.info("Looking up product having id: " + str(query_key))
        product = query_db('select * from books where id=' + str(query_key))
        app.logfile.info('select * from books where id=' + str(query_key))
        return jsonify(product)

def update_product_details(book_id):
    """
    Updates data for a product
    ---
    parameters: 
        - name: book_id
          type: int
          required: true
          description: product id whose details need to be updated
    returns: 
        - json
            description: Status of the operation
    """

    curr_stock_details = query_db('select stock from books where id='+str(book_id))
    app.logfile.info('select stock from books where id='+str(book_id))
    updated_stock_count = curr_stock_details[0]['stock'] - 1

    update_stock_details = update_db('update books set stock='+str(updated_stock_count)+' where id='+str(book_id))
    app.logfile.info('update books set stock='+str(updated_stock_count)+' where id='+str(book_id))

    return(jsonify({'buy': update_stock_details}))

def query_db(query, args=(), one=False):
    """
    Checks if the sqlite database is reachable
    ---
    parameters:
        - name: query (word=<your-word>)
          args: string
          one: boolean if only one result is needed
    """
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def update_db(query):
    try:
        g.db.cursor().executescript(query)
        g.db.commit()
        return True
    except:
        return False