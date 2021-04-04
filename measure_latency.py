import requests
import sys, getopt
import datetime

def measure_search_latency(test_input, test_output):
    request_latency = 0

    for i in range(1000): 
        try:
            start_time = datetime.datetime.now()
            response = requests.get(FRONTEND_ENDPOINT + '/search?topic=' + str(test_input))
            end_time = datetime.datetime.now()
            if response.text == str(test_output):
                request_latency += (end_time - start_time).microseconds
            else:
                print("Response didn't match expected output")
        except ConnectionError as err:
            print("Request failed with error: " + err)
    
    return (request_latency / 100000)

def measure_lookup_latency(test_input, test_output):
    request_latency = 0

    for i in range(1000): 
        try:
            start_time = datetime.datetime.now()
            response = requests.get(FRONTEND_ENDPOINT + '/lookup?id=' + str(test_input))
            end_time = datetime.datetime.now()
            if response.text == str(test_output):
                request_latency += (end_time - start_time).microseconds
            else:
                print("Response didn't match expected output")
        except ConnectionError as err:
            print("Request failed with error: " + err)
    
    return (request_latency / 100000)

def measure_buy_latency(test_input, test_output):
    request_latency = 0
    
    for i in range(1000):
        try:
            start_time = datetime.datetime.now()
            response = requests.post(FRONTEND_ENDPOINT + '/buy', json = {'id': test_input})
            end_time = datetime.datetime.now()
            if response.text.strip() == str(test_output):
                request_latency += (end_time - start_time).microseconds
            else:
                print("Response didn't match expected output")
        except ConnectionError as err:
            print("Request failed with error: " + err)

    return (request_latency / 100000)

if __name__ == "__main__":

    host = "localhost"
    port = "8000"

    # Parse arguments to set the frontend endpoint
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "h:p:", ["host=", "port="])
    except:
        print("python3 run_api_tests.py -h <host> -p <port>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg

    FRONTEND_ENDPOINT = "http://" + host + ":" + port

    print("Starting Latency Testing Script\n")

    # Testing Search Endpoint
    search_latency = measure_search_latency('Graduate School', [{'id': 3, 'name': 'Xen and the Art of Surviving Graduate School'}, {'id': 4, 'name': 'Cooking for the Impatient Graduate Student'}])
    print("Time taken for 1000 sequential search requests: " + str(search_latency) + "s")

    # Testing Lookup Endpoint
    lookup_latency = measure_lookup_latency('1', [{'cost': 200, 'id': 1, 'name': 'How to get a good grade in 677 in 20 minutes a day', 'stock': 200, 'topic': 'Distributed Systems'}])
    print("Time taken for 1000 sequential lookup requests: " + str(lookup_latency) + "s")

    # Testing Buy Endpoint
    buy_latency = measure_buy_latency('4', '{"buy":true}')
    print("Time taken for 1000 sequential buy requests: " + str(buy_latency) + "s")