import requests

base_url = "http://services.runescape.com/m=itemdb_oldschool"

def getItemDetails(itemId):    
   url = base_url + "/api/catalogue/detail.json?item=" + str(itemId)    
   return url
   
def getCategoryDetails(startingLetter,pageNumber):
   url = base_url + "/api/catalogue/items.json?category=1&alpha="+ startingLetter + "&page=" + str(pageNumber)
   return url
   
def getGraphData(itemId):
   url = base_url + "/api/graph/" + str(itemId) + ".json"
   return url