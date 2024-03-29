import requests
import sys, getopt

def test_search_endpoint(test_input, test_output, test_case_num):
   print("Searching for topic: " + test_input)
   try:
      response = requests.get(FRONTEND_ENDPOINT + '/search?topic=' + str(test_input))
      print("Response: " + response.text)
      if response.text == str(test_output):
         print("Response matches expected output")
         print("Test case " + str(test_case_num) + " ....... Passed\n")
         return
      else:
         print("Response didn't match expected output")
   except ConnectionError as err:
      print("Request failed with error: " + err)
   print("Test case: " +str(test_case_num) + " ....... Failed\n")
   return

def test_lookup_endpoint(test_input, test_output, test_case_num):
   print("Performing lookup for book with bookId: " + test_input)
   try:
      response = requests.get(FRONTEND_ENDPOINT + '/lookup?id=' + str(test_input))
      print("Response: " + response.text)
      if response.text == str(test_output):
         print("Response matches expected output")
         print("Test case " + str(test_case_num) + " ....... Passed\n")
         return
      else:
         print("Response didn't match expected output")
   except ConnectionError as err:
      print("Request failed with error: " + err)
   print("Test case: " +str(test_case_num) + " ....... Failed\n")
   return

def test_buy_endpoint(test_input, test_output, test_case_num):
   print("Buying book with bookId: " + test_input)
   try:
      response = requests.post(FRONTEND_ENDPOINT + '/buy', json = {'id': test_input})
      print("Response: " + response.text.strip())
      if response.text.strip() == str(test_output):
         print("Response matches expected output")
         print("Test case " + str(test_case_num) + " ....... Passed\n")
         return
      else:
         print("Response didn't match expected output")
   except ConnectionError as err:
      print("Request failed with error: " + err)
   print("Test case: " +str(test_case_num) + " ....... Failed\n")
   return

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

   print("Starting Client Testing Script\n")

   # Testing Search Endpoint
   test_search_endpoint('Graduate School', [{'id': 3, 'name': 'Xen and the Art of Surviving Graduate School'}, {'id': 4, 'name': 'Cooking for the Impatient Graduate Student'}], 1)
   test_search_endpoint('Umass', [], 2)

   # Testing Lookup Endpoint
   test_lookup_endpoint('1', [{'cost': 200, 'id': 1, 'name': 'How to get a good grade in 677 in 20 minutes a day', 'stock': 200, 'topic': 'Distributed Systems'}], 3)
   test_lookup_endpoint('5', [] , 4)

   # Testing Buy Endpoint
   test_buy_endpoint('4', '{"buy":true}', 5)
   test_buy_endpoint('5', '{"buy":false,"error":"Product doesn\'t exist"}', 6)
