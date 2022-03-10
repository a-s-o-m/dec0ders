import unittest
from Main import Main

class Test_Main(unittest.TestCase):
    def setUp(self):
        firstname = 'Elliot'
        lastname = 'Alderson'
        username = 'samsepiol'
        email = 'elliotalderson@protonmail.ch'
        phone_number = '2125550179'
        password = 'pass123'
    
    def test_become_user(self):
        mainObject = Main()
        mainObject.createNewUser()
