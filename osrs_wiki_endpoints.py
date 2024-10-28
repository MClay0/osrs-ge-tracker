import requests

wiki_endpoint = "https://prices.runescape.wiki/api/v1/osrs"
da_endpoint = "https://prices.runescape.wiki/api/v1/dmm"

def getLatestPrice(itemId=None):
    if itemId == None:
        url = wiki_endpoint+"/latest"
        return url
    else:
        url = wiki_endpoint + "/latest?id=" + str(itemId)
        return url
    
def getWikiMap():
    url = wiki_endpoint + "/mapping"
    return url
    
def getFiveMinPrices(timestamp=None):
    if timestamp == None:
            url = wiki_endpoint+"/5m"
            return url
    else:
        url = wiki_endpoint + "/5m?timestamp=" + str(timestamp)
        return url

def getOneHourPrices(timestamp=None):
    if timestamp == None:
        url = wiki_endpoint+"/1h"
        return url
    else:
        url = wiki_endpoint + "/1h?timestamp=" + str(timestamp)
        return url
        
def getTimeseries(itemId,timestep):
    if timestep not in ["5m","1h","6h","24h"]:
        print('Error: Invalid time interval')
        return None
    url = wiki_endpoint + "/timeseries?timestep=" + timestep + "&id=" + str(itemId)         
    return url