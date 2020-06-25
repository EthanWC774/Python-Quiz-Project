# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)
# Point totals should all be around 15 by the end of the quiz

# Sandwiches = 0
# Salad = 0
# Hamburgers = 0



# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    print(datetime.now())
    return render_template('index.html', time=datetime.now())
    
@app.route('/sendFood', methods=['GET','POST'])
def quiz():
    Pasta = 0
    Ramen = 0
    Sushi = 0
    Steak = 0
    choice1 = request.form["spice"] 
    if choice1 == "salt":
        Ramen = Ramen + 1
        Steak = Steak + 1
    elif choice1 == 'paprika':
        print()
    elif choice1 == 'pepper':
        Steak = Steak + 1
   
    top_food = 0
    top_word = ""
    if Pasta > top_food:
        top_food = Pasta
        top_word = 'Pasta'
    if Ramen > top_food:
        top_food = Ramen
        top_word = 'Ramen'
    if Sushi > top_food:
        top_food = Sushi
        top_word = 'Sushi'
    if Steak > top_food:
        top_food = Steak
        top_word = 'Steak'
    return (top_word)

# @app.route('/sendFood', methods=['GET','POST'])
# def results():
#     return 'hello there '
