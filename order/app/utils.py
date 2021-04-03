from requests.models import Response
from app import app
from flask import jsonify
import requests, datetime

def purchase_product(book_id):
    """
    Starts the process for purchasing a book
    ---
    parameters: 
        - name: book_id
          type: int
          required: true
          description: book id to be bought from the db 
    returns: 
        - json
            description: Status of the operation
    """

    app.logconsole.info("Got request to buy product with id: " + str(book_id))
    try:
        start_time = datetime.datetime.now()
        query_response = requests.get(app.config['CATALOG_SERVICE_ENDPOINT'] + "/query?id=" + str(book_id))
        data = query_response.json()

        if len(data) == 0:
            return(jsonify({"buy": False, "error": "Product doesn't exist"}))

        if (data[0]['stock'] > 0):
            update_url = app.config['CATALOG_SERVICE_ENDPOINT'] + '/update'
            payload = {'id': book_id, 'stock_delta': -1}
            update_response = requests.post(update_url, json=payload)
            update_response_data = update_response.json()

            if update_response_data['stock_updated']:
                app.logconsole.info("Purchase successful and updated the stocks successfully")
                end_time = datetime.datetime.now()
                request_latency = ((end_time - start_time).microseconds / 100000)
                app.logconsole.info("Time taken for buy: " + str(request_latency))
                return(jsonify({"buy": True}))
            else:
                app.logconsole.info("Purchase unsuccessful, catalog service unabled to update details")
                return(jsonify({"buy": False, "error": "Unexpected error"}))
        else:
           return(jsonify({"buy": False, "error": "Product no longer in stock"}))  
    except ConnectionError as err:
        app.logconsole.error(err)
        return False