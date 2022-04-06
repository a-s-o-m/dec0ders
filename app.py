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

logged_in_user = None

# -- Routes section --
# HOME Route
@app.route('/')
@app.route('/home')
def home():
    # companions = mongo.db.companions

    # for companion in catalog:
    #     companions.insert_one(companion.to_document())
    return render_template('home.html', logged_in_user=logged_in_user)

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
                        
        return render_template('match-test.html', logged_in_user=logged_in_user, companion=best_match)   
    else:
        return render_template('match-test.html', logged_in_user=logged_in_user)

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
            try:
                user = User(request.form['firstname'], request.form['lastname'], f"@{request.form['username']}", request.form['email'], request.form['phone_number'], request.form['password'])
            except Exception as err:
                return render_template('signup.html', error=err)
            #add new user to database
            users.insert_one(user.to_document())
            #store username in session
            global logged_in_user 
            logged_in_user = user.to_document()
            return render_template('home.html', logged_in_user=logged_in_user)
        return render_template('signup.html', error='Username/Email already registered. Try logging in.')
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
                global logged_in_user 
                logged_in_user = login_user
                # user = User.from_document(login_user)
                return render_template('home.html', logged_in_user=logged_in_user)
            return render_template('login.html', error='Invalid username/password combination.')
        return render_template('login.html', error='User not found.')
    return render_template('login.html')

#browsing route
@app.route('/browsing')
def browsing():
    companions = mongo.db.companions
    return render_template('browsing.html',logged_in_user=logged_in_user, companions = companions) 

#about-us route
@app.route('/about-us')
def about_us():
    return render_template('about-us.html',logged_in_user=logged_in_user)

#static route
@app.route('/<path:path>')
def get_dir(path):
    #print("Hey now, your ", path) 
    return render_template(path) 

# new companion route
@app.route('/new-companion', methods = ['GET', 'POST'])
def new_comp():
    companions = mongo.db.companions
    print("im here you fool")
    for companion in companions.find({}):
        print(companion)
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

        if session:
            user = session['username']
        else:
            user = None     

        companions = mongo.db.companions
        
        #insert an entry to the database using the variables declared above
        companions.insert_one({"name":name, "age":age, "height":height, "type": type, "animal": animal, "gender": gender, "pic": pic, "description": description})

        #redirect to the index route upon form submission
        return redirect('/')
# Adding function to run Flask by running current .py file
if __name__=='__main__':
    app.run(debug=True)
