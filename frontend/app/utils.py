from app import app
import requests

def backend_healthcheck() -> bool:
    """
    Checks if the sqlite database is reachable
    ---
    parameters: None
    returns: 
        - bool
            description: Indicates if health check passed or not
    """

    try:
        result = requests.get("http://catalog:8080/health")
        app.logconsole.info(result)
        return True
    except ConnectionError as err:
        app.logconsole.error(err)
        return False

def search_topic(topic):
    """
    Searches for given topic in the sqlite database
    ---
    parameters: 
        - name: topic
        - type: string
        - required: true
        - description: topic to be searched in the topic column of the sqlite db 
    returns: 
        - array
            description: All rows in the sqlite db which belong to the specified topic
    """

    app.logconsole.info("Searching for topic " + topic)
    try:
        response = requests.get("http://catalog:8080/querydb?topic="+str(topic))
        return str(response.json())
    except ConnectionError as err:
        app.logconsole.error(err)
        return False

def search_product(book_id):
    """
    Searches for given book in the sqlite database
    ---
    parameters: 
        - name: book_id
        - type: int
        - required: true
        - description: book id to be searched in the db 
    returns: 
        - json
            description: All details regarding the book id
    """

    app.logconsole.info("Searching for product with productId " + str(book_id))
    try:
        response = requests.get("http://catalog:8080/querydb?id="+str(book_id))
        return str(response.json())
    except ConnectionError as err:
        app.logconsole.error(err)
        return False

def buy_product(book_id):
    """
    Searches for given book in the sqlite database
    ---
    parameters: 
        - name: book_id
        - type: int
        - required: true
        - description: book id of the book which needs to be purchased 
    returns: 
        - json
            description: status of whether buy was successful or not
    """

    app.logconsole.info("Buying product with productId " + str(book_id))
    update_url = 'http://order:8080/purchase'
    payload = {'id': book_id}
    try:
        response = requests.post(update_url, json=payload)
        return response.json()
    except ConnectionError as err:
        app.logconsole.error(err)
        return False