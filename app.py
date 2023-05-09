from flask import Flask, render_template, redirect
import sqlite3
from sqlite3 import Error


DATABASE = "C:/Users/68/Desktop/Maori Dictionary/maori.db"

app = Flask(__name__)

@app.route('/')
def render_home():  # home page
    return render_template('home.html')

@app.route('/login',methods=['POST', 'GET'])
def render_login():  # login page
    return render_template('login.html')

@app.route('/signup',methods=['POST', 'GET'])
def render_signup():  # signup page
    if request.method == 'POST':
        print (request.form)
        firstname= request.form.get ('firstname').title().strip()
        lastname = request.form.get('lastname').title().strip()
        email = request.form.get('email').lower().strip()
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if password != password2:
            return redirect('signup?error=Password+do+not+match')

        if len(password) < 8:
            return redirect('signup?error=Password+must+longer+than+8')

        con = open_database(DATABASE)

@app.route('/learning')
def render_learning():  # learning (word list) page
    return render_template('learning.html')

@app.route('/resetpassword')
def render_resetpassword():  # resetpassword page
    return render_template('resetpassword.html')

app.run(host='0.0.0.0',debug=True)