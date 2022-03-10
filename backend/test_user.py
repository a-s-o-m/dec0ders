import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.firstname = 'Elliot'
        self.lastname = 'Alderson'
        self.username = 'samsepiol'
        self.email = 'elliotalderson@protonmail.ch'
        self.phone_number = '2125550179'
        self.password = 'pass123'

    def test_init_types(self):
        # Check parameters when they are not str
        self.assertRaises(TypeError, User, 1, self.lastname, self.username, self.email, self.phone_number, self.password)
        self.assertRaises(TypeError, User, self.firstname, False, self.username, self.email, self.phone_number, self.password)
        self.assertRaises(TypeError, User, self.firstname, self.lastname, +3, self.email, self.phone_number, self.password)
        self.assertRaises(TypeError, User, self.firstname, self.lastname, self.username, None, self.phone_number, self.password)
        self.assertRaises(TypeError, User, self.firstname, self.lastname, self.username, self.email, 0.0, self.password)
        self.assertRaises(TypeError, User, self.firstname, self.lastname, self.username, self.email, self.phone_number, -1)

    def test_init_values(self):
        # Check when firstname is two names
        self.assertRaises(ValueError, User, 'Elliot Alderson', self.lastname, self.username, self.email, self.phone_number, self.password)
        # Check when fist name contains numbers
        self.assertRaises(ValueError, User, 'Elliot1', self.lastname, self.username, self.email, self.phone_number, self.password)
        # Check when lastname are two names
        self.assertRaises(ValueError, User, self.firstname, 'Elliot Alderson', self.username, self.email, self.phone_number, self.password)
        # Check when lastname contains numbers
        self.assertRaises(ValueError, User, self.firstname, 'Alderson1', self.username, self.email, self.phone_number, self.password)
        # Check when len(username) < 3
        self.assertRaises(ValueError, User, self.firstname, self.lastname, 'fo', self.email, self.phone_number, self.password)
        # Check when username contains '@'
        self.assertRaises(ValueError, User, self.firstname, self.lastname, 'foo@bar', self.email, self.phone_number, self.password)
        # Check when email is not valid
        self.assertRaises(ValueError, User, self.firstname, self.lastname, self.username, 'foobar.com', self.phone_number, self.password)
        # Check when len(phone_number) > 10
        self.assertRaises(ValueError, User, self.firstname, self.lastname, self.username, self.email, '12345678910', self.password)
        # Check when len(phone_number) < 10
        self.assertRaises(ValueError, User, self.firstname, self.lastname, self.username, self.email, '123', self.password)
        # Check when phone_number contains letters
        self.assertRaises(ValueError, User, self.firstname, self.lastname, self.username, self.email, '21255b0179', self.password)
        # Check when len(password) < 5
        self.assertRaises(ValueError, User, self.firstname, self.lastname, self.username, self.email, self.phone_number, 'abc1')

    def test_become_companion(self):
        test_user = User(self.firstname, self.lastname, self.username, self.email, self.phone_number, self.password)
        test_object = set()
        
        # Check when non-Companion object is passed as parameter
        self.assertRaises(TypeError, test_user.become_companion, test_object)