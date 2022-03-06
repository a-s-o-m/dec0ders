import re

class User:
    def __init__(self, firstname, lastname, username, email, phone_number, password):
        str_params = [firstname, lastname, username, email, phone_number, password]
        
        for parameter in str_params:
            if type(parameter) != str: 
                raise TypeError(f'{parameter} must be a string.')

        if len(firstname.split()) > 1:
            raise ValueError('only input your firstname here')

        if len(lastname.split()) > 1:
            raise ValueError('only input your lastname here')

        if len(username) < 3:
            raise ValueError('username should be at least 3 characters')

        if not self.validate_email(email):
            raise ValueError('email address is not valid')

        if len(phone_number) > 10:
            raise ValueError('US phone numbers only')
        elif len(phone_number) < 10:
            raise ValueError('invalid phone number')

        if len(password) < 5:
            raise ValueError('password should be at least 5 characters')

        self.firstname = firstname
        self.lastname = lastname
        self.username = f'@{username}'
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.fullname = f'{self.firstname} {self.lastname}'
        self.is_companion = False

    def become_companion(self):
        pass

    def validate_email(self, email):
        regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
        if regex.match(email):
            return True
        else:
            return False
        




