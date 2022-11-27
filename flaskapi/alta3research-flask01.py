#!/usr/bin/env python3 
from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

quotes = [
    "Never forget what you are. The rest of the world will not. Wear it like armor, and it can never be used to hurt you. -Tyrion Lannister (Peter Dinklage)",
    "Any man who must say, 'I am the king,' is no true king. I'll make sure you understand that when I've won your war for you. - Patriarch Tywin Lannister (Charles Dance)", 
    "The things I do for love. - Jaime Lannister (Nikolaj Coster-Waldau)",
    "There is only one thing we say to death: Not today. - Syrio Forel (Maisie Williams)", 
    "If you think this has a happy ending, you haven't been paying attention. - Ramsay Bolton (Iwan Rheon)",
    "You're going to die tomorrow, Lord Bolton. Sleep well. - Sansa Stark's (Sophie Turner)", 
    "That's what I do: I drink and I know things. -Tyrion Lannister (Peter Dinklage)", 
    "Yes. All men must die, but we are not men. - Daenerys Targaryen (Emilia Clarke)",
    "The man who passes the sentence should swing the sword. - Ned Stark (Sean Bean) ", 
    "Chaos isn't a pit. Chaos is a ladder. - Littlefinger (Aidan Gillen)", 
    "Tell Cersei. I want her to know it was me. - Olenna Tyrell (Diana Rigg)",
    "I don't plan on knitting by the fire while men fight for me. I might be small, Lord Glover, and I might be a girl, but I am every bit as much a Northerner as you… and I don't need your permission to defend the North. - Lyanna Mormont (Bella Ramsey)",
    "You know nothing, Jon Snow. - Ygritte's (Rose Leslie)",
    "Winter is coming. - Anyone who's anyone",
    "When you play the game of thrones, you win or you die. There is no middle ground. - Cersei"
    ]

@app.route("/quotes")
def function1():
    return random.choice(quotes)

@app.route("/quotes/all")
def function2():
    return render_template("mytemplate.html", x = quotes)

@app.route("/quotes/all/json")
def function3():
    return quotes

# host = localhost:         2224 /55,565 port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
