import requests
#API guide at https://www.reddit.com/r/2007scape/comments/3g06rq/guide_using_the_old_school_ge_page_api/
headers = {
    'User-Agent': 'GE Price Tacker Tool',
    'From': 'mason_clay@outlook.com', 
    'Discord':'tilt8079'
}

wiki_endpoint = "https://prices.runescape.wiki/api/v1/osrs"
da_endpoint = "https://prices.runescape.wiki/api/v1/dmm"


# Get the latest high and low prices for the items that we have data for, and the Unix timestamp when that transaction took place.
# Map from itemId (see here for a reference) to an object of {high, highTime, low, lowTime}. If we've never seen an item traded, it won't be in the 
# response. If we've never seen an instant-buy price, then high and highTime will be null (and similarly for low and lowTime 
# if we've never seen an instant-sell).

#If itemId is provided then only the info for that item will be returned
def getLatestPrice(itemId=None):
    if itemId == None:
        url = wiki_endpoint+"/latest"
        try: 
            response = requests.get(url,headers=headers)

            if response.status_code == 200:
                latestPrice = response.json()
                return latestPrice
            else:
                print('Error:', response.status_code)
                return None     
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None
    else:
        url = wiki_endpoint + "/latest?id=" + str(itemId)
        try:
            response = requests.get(url,headers=headers)

            if response.status_code == 200:
                latestPrice = response.json()
                return latestPrice
            else:
                print('Error:', response.status_code)
                return None     
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None
    


# Gives a list of objects containing the name, id, examine text, members status, lowalch, highalch, GE buy limit, icon file name (on the wiki).
def getWikiMap():
    url = wiki_endpoint + "/mapping"
    try:
        response = requests.get(url,headers=headers)

        if response.status_code == 200:
            itemMap = response.json()
            return(itemMap)
        else:
            print('Error:',e)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:',e)
        return None
    

# Gives 5-minute average of item high and low prices as well as the number traded for the items that we have data on. 
# Comes with a Unix timestamp indicating the 5 minute block the data is from.

#timestamp - (optional) Timestep to return prices for. If provided, will display 5-minute averages for all items 
# we have data on for this time. The timestamp field represents the beginning of the 5-minute period being averaged.
def getFiveMinPrices(timestamp=None):
    if timestamp == None:
            url = wiki_endpoint+"/5m"
            try: 
                response = requests.get(url,headers=headers)

                if response.status_code == 200:
                    fiveMinPrices = response.json()
                    return fiveMinPrices
                else:
                    print('Error:', response.status_code)
                    return None     
            except requests.exceptions.RequestException as e:
                print('Error:', e)
                return None
    else:
        url = wiki_endpoint + "/5m?timestamp=" + str(timestamp)
        try:
            response = requests.get(url,headers=headers)

            if response.status_code == 200:
                latestPrice = response.json()
                return latestPrice
            else:
                print('Error:', response.status_code)
                return None     
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None

# Gives 1-hour average of item high and low prices as well as the number traded for the items that we have data on. 
# Comes with a Unix timestamp indicating the 1 hour block the data is from.

#timestamp - (optional) Timestep to return prices for. If provided, will display 1-hour averages for all items 
# we have data on for this time. The timestamp field represents the beginning of the 1-hour period being averaged. 
def getOneHourPrices(timestamp=None):
    if timestamp == None:
            url = wiki_endpoint+"/1h"
            try: 
                response = requests.get(url,headers=headers)

                if response.status_code == 200:
                    fiveMinPrices = response.json()
                    return fiveMinPrices
                else:
                    print('Error:', response.status_code)
                    return None     
            except requests.exceptions.RequestException as e:
                print('Error:', e)
                return None
    else:
        url = wiki_endpoint + "/1h?timestamp=" + str(timestamp)
        try:
            response = requests.get(url,headers=headers)

            if response.status_code == 200:
                latestPrice = response.json()
                return latestPrice
            else:
                print('Error:', response.status_code)
                return None     
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None
        
def getTimeseries(itemId,timestep):
    if timestep not in ["5m","1h","6h","24h"]:
        print('Error: Invalid time interval')
        return None
    url = wiki_endpoint + "/timeseries?timestep=" + timestep + "&id=" + str(itemId)         
    try:
        response = requests.get(url,headers=headers)

        if response.status_code == 200:
            timeseries = response.json()
            return(timeseries)
        else:
            print('Error:',e)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:',e)
        return None