from app import app
from flask import jsonify
import time


@app.route('/health', methods=['GET'])
def health_check():
    """
    Route to do check health of application
    """

    return(jsonify({'healthy': True})), 200

@app.route('/purchase',methods=['POST'])
def make_purchase():
    start_time = time.time()
    book_id = request.args.get('id',type=int)
    req = requests.get("http://catalog:8080/querydb?id="+str(id_book))
    print(req) #See the output structure and modify the loop below
    if (req['books'][0]['stock']>0):
        #upd_req = requests.post("http://catalog:8080/updatedb?id="+str(id_book),json={'delta':-1,'cost_updated':200})
        update_url = 'http://catalog:8080/updatedb'
        payload = {'id': book_id}
        upd_req = requests.post(update_url, json.dumps(payload))
        if upd_req.status_code==200:
            print("Purchase successful and updated the stocks successfully")
    end_time = time.time()
    return ("Purchased"+req['books'][0]['name'])
    else:
        print("Item Sold Out")
    
    
