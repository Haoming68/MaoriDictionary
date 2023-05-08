from flask import Flask, render_template
import sqlite3
from sqlite3 import Error


DATABASE = "C:/Users/68/Desktop/Maori Dictionary/maori.db"

app = Flask(__name__)

@app.route('/')
def render_home_page():  # home page
    return render_template('home.html')

@app.route('/login')
def render_login_page():  # login page
    return render_template('login.html')

@app.route('/signup')
def render_signup_page():  # signup page
    return render_template('signup.html')

@app.route('/learning')
def render_learning_page():  # learning (word list) page
    return render_template('learning.html')

@app.route('/resetpassword')
def render_resetpassword_page():  # resetpassword page
    return render_template('resetpassword.html')

app.run(host='0.0.0.0',debug=True)