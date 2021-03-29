from requests.models import Response
from app import app
from flask import jsonify
import requests

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
        query_response = requests.get("http://catalog:8080/query?id="+str(book_id))
        data = query_response.json()

        if len(data) == 0:
            return(jsonify({"buy": False, "error": "Product doesn't exist"}))

        if (data[0]['stock'] > 0):
            update_url = 'http://catalog:8080/update'
            payload = {'id': book_id}
            update_response = requests.post(update_url, json=payload)
            if update_response.status_code == 200:
                app.logconsole.info("Purchase successful and updated the stocks successfully")
            return(update_response.json())
        else:
           return(jsonify({"buy": False, "error": "Product no longer in stock"}))  
    except ConnectionError as err:
        app.logconsole.error(err)
        return False