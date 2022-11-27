#!/usr/bin/env python3 
import requests


URL = "https://www.anapioficeandfire.com/api"

def main():
    #data converted from json to python 
    resp = requests.get(URL).json()
    print(resp)


if __name__ == "__main__":
    main()
