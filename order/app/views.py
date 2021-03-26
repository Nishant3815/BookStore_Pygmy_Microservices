from app import app
from flask import request, jsonify
import time, json, requests


@app.route('/health', methods=['GET'])
def health_check():
    """
    Route to do check health of application
    """

    return(jsonify({'healthy': True})), 200

@app.route('/purchase',methods=['POST'])
def make_purchase():
    start_time = end_time = time.time()
    book_id = request.json['id']
    app.logconsole.info("Got request to buy book " + str(book_id))
    response = requests.get("http://catalog:8080/querydb?id="+str(book_id))
    data = response.json()
    if (data[0]['stock'] > 0):
        update_url = 'http://catalog:8080/updatedb'
        payload = {'id': book_id}
        upd_req = requests.post(update_url, json=payload)
        if upd_req.status_code==200:
           app.logconsole.info("Purchase successful and updated the stocks successfully")
        end_time = time.time()
        return(upd_req.json()), 200
    else:
        return(jsonify({"error": "Item no longer in stock"})), 200
    
    
