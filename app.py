from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from flask import request, redirect, session, url_for
from backend import user
import secrets
import os


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
# Accessed from CONFIG VARS
secret_key = os.environ.get('MONGO_URI')
app.config['MONGO_URI'] = secret_key

#Initialize PyMongo
mongo = PyMongo(app)

# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')

# -- Routes section --
# INDEX Route

#SIGNUP Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        existing_user = users.find_one({'username': request.form['username']})

        #if user not in database
        if not existing_user:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            username = request.form['username']
            email = request.form['email']
            phone_number = request.form['phone_number']
            password = request.form['password']
            user = user.User(firstname, lastname, username, email, phone_number, password)
            #encode password for hashing
            password = request.form['password'].encode("utf-8")
            # create new user

            # #hash password
            # salt = bcrypt.gensalt()
            # hashed = bcrypt.hashpw(password, salt)
            #add new user to database
            # users.insert_one({'name': username, 'password': hashed})
            #store username in session
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        else:
            return 'Username already registered.  Try logging in.'
    
    else:
        return render_template('signup.html')
#LOGIN Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        login_user = users.find_one({'name': request.form['username']})

        #if username in database
        if login_user:
            db_password = login_user['password']
            #encode password
            password = request.form['password'].encode("utf-8")
            #compare username in database to username submitted in form
            # if bcrypt.checkpw(password, db_password):
            #     #store username in session
            #     session['username'] = request.form['username']
            #     return redirect(url_for('index'))
            # else:
            #     return 'Invalid username/password combination.'
        else:
            return 'User not found.'
    else:
        return render_template('login.html')
