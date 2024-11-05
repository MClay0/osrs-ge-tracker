from ge_page_endpoints import *
from osrs_wiki_endpoints import *   
from classes import api     
from dbConnect import cursor,dbConn
import psycopg2
import json 
import time
import datetime

if __name__ == "__main__":
    endpoints = api() # Establishes api object to make requests
    basicData = endpoints.sendRequest("https://chisel.weirdgloop.org/gazproj/gazbot/os_dump.json") # Initialize basic data table
    tradeableItems = endpoints.sendRequest(getLatestPrice())
    tradeableItems = tradeableItems['data']
    del basicData["%UPDATE_DETECTED%"] 
    del basicData["%JAGEX_TIMESTAMP%"]
    
    for item in basicData:                              #Inputs data into the items table
        try:
            if item in tradeableItems.keys():
                item_id = item
                item_name = basicData[item]['name']
                item_description = basicData[item]['examine']
                command = """INSERT INTO items(item_id,name,description) VALUES(%s,%s,%s)"""
                cursor.execute(command,(item_id,item_name,item_description))
                dbConn.commit()
        finally:
            continue

    try:       
        while True:
            try:
                print("new query")
                e1 = endpoints.sendRequest(getFiveMinPrices())  #avgHighPrice,highPriceVolume,avgLowPrice,lowPriceVolume
                e1 = e1['data']
                e2 = endpoints.sendRequest(getLatestPrice())    #high,highTime,low,lowTime
                e2 = e2['data']
                for item in e2:
                    if item in e1:
                        e1[item] = {**e1[item],**e2[item]}
                for item in e1:
                    currentItem = e1[item]
                    item_id = item
                    avgHighPrice = currentItem['avgHighPrice']
                    highPriceVolume = currentItem['highPriceVolume']
                    avgLowPrice = currentItem['avgLowPrice']
                    lowPriceVolume = currentItem['lowPriceVolume']   
                    high = currentItem['high']
                    highTime = str(datetime.datetime.fromtimestamp(currentItem['highTime']))
                    low = currentItem['low']
                    lowTime = str(datetime.datetime.fromtimestamp(currentItem['lowTime']))
                    if avgLowPrice is None or avgHighPrice is None:
                        continue
                    command = """INSERT INTO prices(item_id,low,low_time,high,high_time,avg_high_price,high_price_volume,avg_low_price,low_price_volume) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                    try:
                        cursor.execute(command,(item_id,low,lowTime,high,highTime,avgHighPrice,highPriceVolume,avgLowPrice,lowPriceVolume))
                    except Exception as err:
                        print(err)
                    dbConn.commit()
            except Exception as err:
                print(err)
                exit
            time.sleep(300)
    except KeyboardInterrupt:
        cursor.close()
        dbConn.close()
        print("Process Killed")