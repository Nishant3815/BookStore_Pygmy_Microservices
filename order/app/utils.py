from requests.models import Response
from app import app
from flask import jsonify
import requests

def purchase_product(book_id):
    app.logconsole.info("Got request to buy product with id: " + str(book_id))
    try:
        query_response = requests.get("http://catalog:8080/querydb?id="+str(book_id))
        data = query_response.json()
        if (data[0]['stock'] > 0):
            update_url = 'http://catalog:8080/updatedb'
            payload = {'id': book_id}
            update_response = requests.post(update_url, json=payload)
            if update_response.status_code == 200:
                app.logconsole.info("Purchase successful and updated the stocks successfully")
            return(update_response.json())
        else:
           return(jsonify({"buy": False, "error": "Item no longer in stock"})), 200   
    except ConnectionError as err:
        app.logconsole.error(err)
        return False