from app import app
import requests, datetime

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
        result = requests.get(app.config['CATALOG_SERVICE_ENDPOINT'] + "/health")
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
          type: string
          required: true
          description: topic to be searched in the topic column of the sqlite db 
    returns: 
        - array
            description: All rows in the sqlite db which belong to the specified topic
    """

    app.logconsole.info("Searching for topic " + topic)
    try:
        start_time = datetime.datetime.now()
        response = requests.get(app.config['CATALOG_SERVICE_ENDPOINT'] + "/query?topic=" + str(topic))
        app.logconsole.info("Got response: " + response.text.strip())
        end_time = datetime.datetime.now()
        request_latency = ((end_time - start_time).microseconds / 100000)
        app.logconsole.info("Time taken for search: " + str(request_latency))
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
          type: int
          required: true
          description: book id to be searched in the db 
    returns: 
        - json
            description: All details regarding the book id
    """

    app.logconsole.info("Searching for product with productId " + str(book_id))
    try:
        start_time = datetime.datetime.now()
        response = requests.get(app.config['CATALOG_SERVICE_ENDPOINT'] + "/query?id=" + str(book_id))
        app.logconsole.info("Got response: " + response.text.strip())
        end_time = datetime.datetime.now()
        request_latency = ((end_time - start_time).microseconds / 100000)
        app.logconsole.info("Time taken for lookup: " + str(request_latency))
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
          type: int
          required: true
          description: book id of the book which needs to be purchased 
    returns: 
        - json
            description: status of whether buy was successful or not
    """

    app.logconsole.info("Buying product with productId " + str(book_id))
    update_url = app.config['ORDER_SERVICE_ENDPOINT'] + '/purchase'
    payload = {'id': book_id}
    try:
        start_time = datetime.datetime.now()
        response = requests.post(update_url, json=payload)
        if response.json()["buy"]:
            app.logconsole.info("Bought book with bookId: " + str(book_id))
            end_time = datetime.datetime.now()
            request_latency = ((end_time - start_time).microseconds / 100000)
            app.logconsole.info("Time taken for buy: " + str(request_latency))
        else:
            app.logconsole.info("Unable to buy book with bookId: " + str(book_id))
        return response.json()
    except ConnectionError as err:
        app.logconsole.error(err)
        return False