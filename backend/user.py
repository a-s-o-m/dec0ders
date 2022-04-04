import re

from backend.companion import Companion

class User:
    def __init__(self, firstname, lastname, username, email, phone_number, password):
        str_params = [firstname, lastname, username, email, phone_number, password]
        
        for parameter in str_params:
            if type(parameter) != str: 
                raise TypeError(f'{parameter} must be a string.')

        if len(firstname.split()) > 1:
            raise ValueError('only input your firstname here')
        elif not firstname.isalpha():
            raise ValueError('your firstname should not contain a number')

        if len(lastname.split()) > 1:
            raise ValueError('only input your lastname here')
        elif not lastname.isalpha():
            raise ValueError('your lastname should not contain a number')

        if len(username) < 3:
            raise ValueError('username should be at least 3 characters')
        elif '@' in username:
            raise ValueError('username should not contain @ symbol as it will be added afterwards by our system')

        if not self.validate_email(email):
            raise ValueError('email address is not valid')

        if len(phone_number) > 10:
            raise ValueError('US phone numbers only')
        elif len(phone_number) < 10:
            raise ValueError('phone number cannot be less than 10 numbers')
        elif not phone_number.isnumeric():
            raise ValueError('phone number contains characters that are not numbers')

        if len(password) < 5:
            raise ValueError('password should be at least 5 characters')

        self.firstname = firstname
        self.lastname = lastname
        self.username = f'@{username}'
        self.email = email
        self.phone_number = phone_number
        # self.password = password
        self.fullname = f'{self.firstname} {self.lastname}'
        self.companion_account = None

    def become_companion(self, companion_config):
        # prompt companion cli
        # create companion account for user
        if (not isinstance(companion_config, Companion)):
            raise TypeError('account must be instance of Companion class')
        self.companion_account = companion_config
    
    def is_companion(self):
        if self.companion_account == None:
            return False
        return True

    def validate_email(self, email):
        regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
        if regex.match(email):
            return True
        else:
            return False