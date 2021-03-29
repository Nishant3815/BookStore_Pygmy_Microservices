import requests

print("Starting Testing Script")

def test_search_endpoint(test_input, test_output, test_case_num):
   try:
      response = requests.get('http://localhost:8000/search?topic=' + str(test_input))
      if response.text == str(test_output):
          print("Test case " + str(test_case_num) + " ....... Passed")
          return
   except ConnectionError as err:
      print(err)
   print("Test case: " +str(test_case_num) + " ....... Failed")
   return


test_search_endpoint('Graduate School', [{'id': 3, 'name': 'Xen and the Art of Surviving Graduate School'}, {'id': 4, 'name': 'Cooking for the Impatient Graduate Student'}], 1) 
#test_search_endpoint('Disributed Systems', [{'id': 3, 'name': 'Xen and the Art of Surviving Graduate School'}, {'id': 4, 'name': 'Cooking for the Impatient Graduate Student'}], 2)  
    
def test_lookup_endpoint(input, output, test_case_num):

   try:
      response = requests.get('http://localhost:8000/search?id=input')
      if response == output:
          print("Test case " + test_case_num + " passed")
          return
   except ConnectionError as err:
      print(err)
      print("Test case " + test_case_num + " failed")
   return



#test_lookup_endpoint('4', [{'cost': 200, 'id': 4, 'name': 'Cooking for the Impatient Graduate Student', 'stock': 200, 'topic': 'Graduate School'}], 3)
#test_lookup_endpoint('1', [{'cost': 200, 'id': 4, 'name': 'Cooking for the Impatient Graduate Student', 'stock': 200, 'topic': 'Graduate School'}] , 4)





def test_buy_endpoint(input, output, test_case_num):

   try:
      response = requests.post('http://localhost:8000/buy', data = {'id':'2'})
      if response == {'buy':'true'}:
          print("Test case " + test_case_num + " passed")
          return
   except ConnectionError as err:
      print(err)
      print("Test case " + test_case_num + " failed")
   return


#test_buy_endpoint
