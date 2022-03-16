from companion import Companion
from companion_catalog import CompanionCatalog
from user import User

class CLI:
    def __init__(self):  
        self.catalog = CompanionCatalog() # List of rentable dates
        self.user = None 
        self.menu_options = {
            1: 'Sign Up',
            2: 'Browse Catalog',
            3: 'Take Compatibility Test',
            4: 'Become A Companion',
        }

    def sign_up(self):
        # Prompts the user for information and creates a User object 
        firstname = input('First name:\n')
        lastname = input('Last name:\n')
        username = input('Username:\n')
        email = input('Email:\n')
        phone_number = input('Phone number:\n')
        password = input('Password:\n')

        self.user = User(firstname, lastname, username, email, phone_number, password)
        print('----------------------')
        print(f'Welcome {self.user.username}!')
        print('----------------------')

    def user_to_companion(self):
        # Prompts the user for information and creates a Companion object
        sex_input = input('You are:\n 1. Male\n 2. Female\n')
        sex = 'male' if sex_input == '1' else 'female'
        age = (int)(input("What is your age?\n"))
        height = (int)(input("What is your height?(cm)\n"))
        personality_input = input("Are you:\n1. Introverted\n2. Extroverted\n")
        personality = 'introvert' if personality_input == '1' else 'extrovert'
        pet_input = input("You are more like a:\n1. Dog person\n2. Cat person\n")
        pet_preference = 'dog' if pet_input == '1' else 'cat'
        name = f'{self.user.firstname} {self.user.lastname}'
        new_companion = Companion(name, age, height, personality, pet_preference, sex)

        self.user.become_companion(new_companion)
        self.catalog.addCompanion(new_companion)
        print('-----------------------------------------------------')
        print('You have successfully joined the Rent-A-Date catalog!')
        print('-----------------------------------------------------')


    def compatibility_test(self):
        # Displays the companion with highest match based on user information.
        print('What age range are you looking for in a partner?')
        age_lower = (int)(input('min: '))
        age_upper = (int)(input('max: '))
        pref_age = [age_lower, age_upper]
        print('What height range are you looking for in a partner?')
        height_lower = (int)(input('min:(cm) '))
        height_upper = (int)(input('max:(cm) '))
        pref_height = [height_lower, height_upper]
        sex_input = input('You would like your partner to be:\n 1. Male\n 2. Female\n')
        pref_sex = 'male' if sex_input == '1' else 'female'
        personality_input = input("You would like your partner to be more of a:\n1. Introvert\n2. Extrovert\n")
        pref_personality = 'introvert' if personality_input == '1' else 'extrovert'

        if self.user.companion_account:
            pref_pet = self.user.companion_account.pet_preference

        else:
            pet_input = input("You are more like a:\n1. Dog person\n2. Cat person\n")
            pref_pet = 'dog' if pet_input == '1' else 'cat'

        max_score = -1

        for companion in self.catalog.companions:
            score = companion.calculate_match(pref_age, pref_height, pref_personality, pref_pet, pref_sex)
            if score > max_score:
                best_match = companion
                max_score = score

        print('Here is our recommendation:')
        print('------------------------------------')
        print(best_match)
        print('------------------------------------')

    def display_catalog(self):
        # Prints all the companion objects from the database
        for companion in self.catalog.companions:
            print('------------------------------------')
            print(companion)
            print('------------------------------------')

    def display_menu(self):
        if self.user is None: # User has not signed up
            # Prints options 1, 2
            print('1.',self.menu_options[1],'\n2.',self.menu_options[2])

        elif not self.user.is_companion(): # User has signed up and is not companion
            # Prints options 2, 3, 4, 
            print('1.',self.menu_options[2],'\n2.',self.menu_options[3], '\n3.',self.menu_options[4])

        else: # User has signed up and is companion
            # Prints options 2, 3
            print('1.',self.menu_options[2],'\n2.',self.menu_options[3])
        
cli = CLI()

print(' -------------------- ')
print('|                    |')
print('|    Rent-A-Date     |')
print('|                    |')
print(' -------------------- ')

while(True):
    cli.display_menu()
    user_input = input()

    if cli.user is None:    

        if user_input == '1':
            cli.sign_up()
        elif user_input == '2':
            cli.display_catalog()
        else:
            print('Invalid input.')

    elif not cli.user.is_companion():

        if user_input == '1':
            cli.display_catalog()
        elif user_input == '2':
            cli.compatibility_test()
        elif user_input == '3':
            cli.user_to_companion()
        else:
            print('Invalid input.')        

    else:
        if user_input == '1':
            cli.display_catalog()
        elif user_input == '2':
            cli.compatibility_test()
        else:
            print('Invalid input.')