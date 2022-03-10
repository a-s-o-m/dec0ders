import unittest
from Companion import Companion
from companionCatalog import CompanionCatalog
from user import User

# python3 -m unittest test_companion_catalog.py
class TestCompanion(unittest.TestCase):

    def test_add_companion(self):
        user = User('Johnny', 'Test', 'jtest', 'jt@mail.com', '0123456789', '12345')
        # shoudln't be able to add object that isnt a companion to companions list.
        self.assertRaises(TypeError, CompanionCatalog.addCompanion, user)
        self.assertRaises(TypeError, CompanionCatalog.addCompanion, '')
        self.assertRaises(TypeError, CompanionCatalog.addCompanion, False)
        # transform user to companion
        catalog = CompanionCatalog()
        catalogSize = len(catalog.companions)
        user.become_companion(Companion(user.fullname, 65, 150, 'introvert', 'cat', 'male'))
        catalog.addCompanion(user.companion_account)
        # check if companions list is sucessfully updated when a companion is added.
        self.assertEqual(catalogSize+1, len(catalog.companions))
    