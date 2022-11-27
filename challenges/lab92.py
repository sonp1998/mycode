#!/usr/bin/env python3 

import requests 
import datetime
#Define URL 
URL = "http://api.open-notify.org/iss-now.json"

def main():
    #Call the webservice and trasnlate json into python. send get request, get a response. 
    resp = requests.get(URL).json()
    #Slice data into variables
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    time_epoch = resp["timestamp"]
    time_date = datetime.datetime.fromtimestamp(time_epoch)
    print("CURRENT LOCATION OF THE ISS:")
    print("Timestamp: " + str(time_date))
    print("Lon: " + lon)
    print("Lat: " + lat)

if __name__ == "__main__":
    main()
