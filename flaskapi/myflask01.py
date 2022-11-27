#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
import random
#from the entire flas module, ONLY give me the Flask class, please & thanks. Out of entire toolbox, only want Flask tool.


# variable "app" represents our entire api!
# Flask constructor takes the name of current
# module (__name__) as argument
# this whole script is "teaching" our little app object how to behave. Teaching app to look at this file to learn how to behave
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/welcome") #This is decorator 
def hello_welcome():
    return "Hello, Welcome! Here are the list of endpoints: "

@app.route("/philip")
def world_hello():
    return {"name": "philip",
            "lastname":"son",
            "generation":"1"}

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

