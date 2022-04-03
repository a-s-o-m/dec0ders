from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect, session, url_for
import secrets
import os


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
# Accessed from CONFIG VARS
app.config['MONGO_URI'] = "mongodb+srv://saulotero:9RZJoVZ9w8baMYgY@cluster0.kflcs.mongodb.net/dec0ders?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)

# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')
new_user = True
# -- Routes section --
# HOME Route
@app.route('/')
def home():
    return render_template('home.html', new_user=new_user)

#SIGNUP Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        existing_user = users.find_one({'username': request.form['username']})

        #if user not in database
        if not existing_user:
            username = request.form['username']
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

#browsing route
@app.route('/browsing')
def browsing():
    #rows = Companion.query.all()
    return render_template('browsing.html') 
    


# Adding function to run Flask by running current .py file
if __name__=='__main__':
    app.run(debug=True)