import requests

base_url = "http://services.runescape.com/m=itemdb_oldschool"

def getItemDetails(itemId):    
   url = base_url + "/api/catalogue/detail.json?item=" + str(itemId)    
   return url
   
def getCategoryDetails(startingLetter,pageNumber):
   url = base_url + "/api/catalogue/items.json?category=1&alpha="+ startingLetter + "&page=" + str(pageNumber)
   return url
   
   # itemID - The engine identifier of the item. See the above link to find an item you are looking for.
   # Returns a JSON response of data to generate a graph for an item. The data is in the format of "Epoch Time: Item Value"
   # /api/graph/itemID.json  
def getGraphData(itemId):
   url = base_url + "/api/graph/" + str(itemId) + ".json"
   return url