from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect, session, url_for
from model import User, catalog, from_document_to_companion
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

new_user = True

# -- Routes section --
# HOME Route
@app.route('/')
@app.route('/home')
def home():
    # companions = mongo.db.companions

    # for companion in catalog:
    #     companions.insert_one(companion.to_document())
    return render_template('home.html', new_user=new_user)

#MATCH TEST Route
@app.route('/match-test', methods=['GET', 'POST'])
def match_test():
    if request.method == 'POST':
        companions = mongo.db.companions

        min_age = (int)(request.form["min_age"])
        max_age = (int)(request.form["max_age"])
        if min_age > max_age: min_age = max_age
        pref_age = [min_age, max_age]

        min_height = (int)(request.form["min_height"])
        max_height = (int)(request.form["max_height"])
        if min_height > max_height: min_height = max_height
        pref_height = [min_height, max_height]

        pref_personality = request.form["personality"]
        pref_pet = request.form["pet"]
        pref_sex = request.form['sex']
        
        max_score = -1
        for companion in companions.find():
            current_companion = from_document_to_companion(companion)
            score = current_companion.calculate_match(pref_age, pref_height, pref_personality, pref_pet, pref_sex)

            if score > max_score:
                if pref_sex == 'other':
                    best_match = companion
                    max_score = score
                    
                elif pref_sex == current_companion.sex:
                    best_match = companion
                    max_score = score
                        
        return render_template('match-test.html', new_user=new_user, companion=best_match)   
    else:
        return render_template('match-test.html', new_user=new_user)

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
            user = User(request.form['firstname'], request.form['lastname'], f"@{request.form['username']}", request.form['email'], request.form['phone_number'], request.form['password'])
            #add new user to database
            users.insert_one(user.to_document())
            #store username in session
            session['username'] = user.username
            global new_user 
            new_user = False
            return render_template('home.html', new_user=new_user)
        return 'Username/Email already registered. Try logging in.'
    return render_template('signup.html')
#LOGIN Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        login_user = users.find_one({'username': f"@{request.form['username']}"})

        #if username in database
        if login_user:
            if login_user['password'] == request.form['password']:
                global new_user 
                new_user = False
                return render_template('home.html', new_user=new_user)
            return 'Invalid username/password combination.'
        return 'User not found.'
    return render_template('login.html')

#browsing route
@app.route('/browsing')
def browsing():
    companions = mongo.db.companions
    return render_template('browsing.html',new_user=new_user, companions = companions) 

#static route
@app.route('/<path:path>')
def get_dir(path):
    #print("Hey now, your ", path) 
    return render_template(path) 

# new companion route
@app.route('/new-companion', methods = ['GET', 'POST'])
def new_comp():
    companions = mongo.db.companions
    if request.method == "GET":
        #render the form, with the companion list to populate the dropdown menu
        return render_template('new-companion.html', companions = companions)
    else:
        #assign form data to variables
        name = request.form['name']
        age = request.form['age']
        height = request.form['height']
        type = request.form['type']
        animal = request.form['animal']
        gender = request.form['gender']
        pic = request.form['pic']
        description = request.form['description']
                

        companions = mongo.db.library
        
        #insert an entry to the database using the variables declared above
        companions.insert_one({"name":name, "age":age, "height":height, "type": type, "animal": animal, "gender": gender, "pic": pic, "description": description})

        #redirect to the index route upon form submission
        return redirect('/')
# Adding function to run Flask by running current .py file
if __name__=='__main__':
    app.run(debug=True)
