import requests
#API guide at https://www.reddit.com/r/2007scape/comments/3g06rq/guide_using_the_old_school_ge_page_api/
base_url = "http://services.runescape.com/m=itemdb_oldschool"



# Returns a JSON response of details about the item based on the ID. 
# Data includes: a small and large icon, the name, description, and price trends.
# /api/catalogue/detail.json?item=itemId
def getItemDetails(itemId):    
   url = base_url + "/api/catalogue/detail.json?item=" + str(itemId)    
   try:
      response = requests.get(url)

      if response.status_code == 200:
         itemDetails = response.json()
         return itemDetails
      else:
         print('Error:', response.status_code)
         return None     
   except requests.exceptions.RequestException as e:
      print('Error:', e)
      return None
   

   # startingLetter, y - The alphabetical letter that all items must start with in the results. Use "%23" to get items which start with a  number.
   # pageNumber, z - The page number to reference. There are 12 results per page.
   # /api/catalogue/items.json?category=1&alpha=y&page=z
def getCategoryDetails(startingLetter,pageNumber):
   url = base_url + "/api/catalogue/items.json?category=1&alpha="+ startingLetter + "&page=" + str(pageNumber)
   try:
      response = requests.get(url)

      if response.status_code == 200:
         categoryDetails = response.json()
         return categoryDetails
      else:
         print('Error:', response.status_code)
         return None     
   except requests.exceptions.RequestException as e:
      print('Error:', e)
      return None
   
   # itemID - The engine identifier of the item. See the above link to find an item you are looking for.
   # Returns a JSON response of data to generate a graph for an item. The data is in the format of "Epoch Time: Item Value"
   # /api/graph/itemID.json  
def getGraphData(itemId):
   url = base_url + "/api/graph/" + str(itemId)                 + ".json"
   try:
      response = requests.get(url)

      if response.status_code == 200:
         graphDetails = response.json()
         return graphDetails
      else:
         print('Error:', response.status_code)
         return None     
   except requests.exceptions.RequestException as e:
      print('Error:', e)
      return None