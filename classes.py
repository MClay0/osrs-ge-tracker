import requests

class api:
    gep_endpoints = "http://services.runescape.com/m=itemdb_oldschool"
    wiki_endpoints = "https://prices.runescape.wiki/api/v1/osrs"
    da_endpoints = "https://prices.runescape.wiki/api/v1/dmm"
    
    def __init__(self):
        pass
    
    def sendRequest(self,url):
        headers = {
        'User-Agent': 'GE Price Tacker Tool',
        'From': 'mason_clay@outlook.com', 
        'Discord':'tilt8079'
        }
        if url == None:
            print("Invalid URL")
            return None
        try:
            response = requests.get(url,headers=headers)
            
            if response.status_code == 200:
                return response.json()
            else:
                print('Error:', response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print('Error:', e)
            return None