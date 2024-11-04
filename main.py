from ge_page_endpoints import *
from osrs_wiki_endpoints import *   
from classes import api     
from dbConnect import cursor,dbConn
import psycopg2
import json 

if __name__ == "__main__":
    endpoints = api() # Establishes api object to make requests
    basicData = endpoints.sendRequest("https://chisel.weirdgloop.org/gazproj/gazbot/os_dump.json") # Initialize basic data table
    tradeableItems = endpoints.sendRequest(getLatestPrice())

    del basicData["%UPDATE_DETECTED%"] 
    del basicData["%JAGEX_TIMESTAMP%"]
    
    for item in basicData:                              #Inputs Data Into The 
        if item in tradeableItems['data'].keys():
            item_id = item
            item_name = basicData[item]['name']
            item_description = basicData[item]['examine']
            command = """INSERT INTO items(item_id,name,description) VALUES(%s,%s,%s)"""
            cursor.execute(command,(item_id,item_name,item_description))
            dbConn.commit()