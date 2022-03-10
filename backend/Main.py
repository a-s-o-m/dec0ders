from Companion import Companion
from user import User
from companionCatalog import CompanionCatalog

class Main:
    def __init__(self):
        
        #Ask user if they want to become a user
        newUSerQuestion = input("Do you want to become a new user (Y/y/Yes/yes)")
        if newUSerQuestion == "y" or newUSerQuestion == "Y" or newUSerQuestion == "yes" or newUSerQuestion == "Yes":
            self.user = self.createNewUser()
            print(f"Welcome, {self.user.username}!")
        else:
            self.user = None
            print("User is not created")


    def createNewUser(self):
        firstName = input("Enter your first name")
        lastName = input("Enter your last name")
        userName = input("Create a username")
        email = input("Enter your email")
        phoneNumber = input("Enter your phone number")
        password = input("Create a password")
        newUser = User(firstName, lastName, userName, email, phoneNumber, password)
        return newUser

    def makeUserCompanion(self, user):
        age = input("Enter your age")
        height = input("Enter your height")       
        personality = input("Enter your personality type")
        pet_preference = input("Enter your pet preference")
        sex = input("Enter your sex")

        #Create a new companion.
        companion = Companion(user.name, age, height, personality, pet_preference, sex)

        #Add new companion to the companion catalog.
        catalog = CompanionCatalog()
        catalog.addCompanion(companion)

        return companion

    