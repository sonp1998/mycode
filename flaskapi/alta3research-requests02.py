#!/usr/bin/env python3

import requests 

URL = "https://0.0.0.0:2224/quotes/all/json"

resp = requests.get(URL).json()
print(resp)




