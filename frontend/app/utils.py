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
        app.logger.info(result)
        return True
    except ConnectionError as err:
        app.logger.error(err)
        return False