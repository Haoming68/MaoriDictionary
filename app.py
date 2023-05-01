from flask import Flask, render_template
import sqlite3
from sqlite3 import Error


DATABASE = "C:/Users/68/Desktop/Maori Dictionary/maori.db"

app = Flask(__name__)

@app.route('/')
def render_homepage():  # put application's code here
    return render_template('home.html')



app.run(host='0.0.0.0',debug=True)