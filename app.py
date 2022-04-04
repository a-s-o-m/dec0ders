from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect, session, url_for
from seed_library import seed_companions
from backend.user import User
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
companions = seed_companions
# -- Routes section --
# HOME Route
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', new_user=new_user)
#MATCH TEST Route
@app.route('/match-test', methods=['GET', 'POST'])
def match_test():
    return render_template('match-test.html')

#SIGNUP Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        users = mongo.db.users
        #search for username/email in database
        existing_user = users.find_one({'$or': [{'username': request.form['username']},
                     {'email': request.form['email']}]})
        
        #if user not in database
        if not existing_user:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            username = request.form['username']
            email = request.form['email']
            phone_number = request.form['phone_number']
            password = request.form['password']
            user = User(firstname, lastname, username, email, phone_number, password)
            #encode password for hashing
            # password = request.form['password'].encode("utf-8")
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
        login_user = users.find_one({'username': request.form['username']})

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
    #collection = mongo.db.library
    return render_template('browsing.html', companions = companions, new_user = new_user) 

#static route
@app.route('/<path:path>')
def get_dir(path):
    #collection = mongo.db.library
    #print("Hey now, your ", path) 
    return render_template(path) 

# new companion route
@app.route('/new_companion', methods = ['GET', 'POST'])
def new_book():
    if request.method == "GET":
        #render the form, with the companion list to populate the dropdown menu
        return render_template('new_companion.html', companions = companions)
    else:
        #assign form data to variables
        name = request.form['name']
        age = request.form['age']
        height = request.form['height']
        type = request.form['type']
        animal = request.form['animal']
        gender = request.form['gender']
        pic = request.form['pic']
        
        #retrieve username from session data if present
        if session:
            user = session['username']
        else:
            user = None

        #insert an entry to the database using the variables declared above
        companions.append({"name":name, "age":age, "height":height, "type": type, "animal": animal, "gender": gender, "pic": pic})
    return redirect('/')
# Adding function to run Flask by running current .py file
if __name__=='__main__':
    app.run(debug=True)