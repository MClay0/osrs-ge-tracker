from ge_page_endpoints import *
from osrs_wiki_endpoints import *   
from classes import api     
import json 

if __name__ == "__main__":
    endpoints = api()
    newestData = endpoints.sendRequest(getLatestPrice())
    pass
