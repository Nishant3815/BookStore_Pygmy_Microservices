from app import app
from flask import g


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
        return True
    except ConnectionError as err:
        app.logger.error(err)
        return False

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