import unittest
from companion import Companion
from companion_catalog import CompanionCatalog
from user import User

# python3 -m unittest test_companion_catalog.py
class TestCompanion(unittest.TestCase):
    
    def test_add_companion(self):
        user = User('Johnny', 'Test', 'jtest', 'jt@mail.com', '0123456789', '12345')
        # shoudln't be able to add object that isnt a companion to companions list.
        self.assertRaises(TypeError, CompanionCatalog.addCompanion, user)
        self.assertRaises(TypeError, CompanionCatalog.addCompanion, '')
        self.assertRaises(TypeError, CompanionCatalog.addCompanion, False)
        catalog = CompanionCatalog()
        catalogSize = len(catalog.companions)
        # create companion account for user
        user.become_companion(Companion(user.fullname, 65, 150, 'introvert', 'dog', 'male'))
        catalog.addCompanion(user.companion_account)
        # check if companions list is sucessfully updated when a companion is added.
        self.assertEqual(catalogSize+1, len(catalog.companions))
    
    def test_remove_companion(self):
        user = User('Johnny', 'Test', 'jtest', 'jt@mail.com', '0123456789', '12345')
        # shoudln't be able to remove object that isnt a companion.
        self.assertRaises(TypeError, CompanionCatalog.removeCompanion, user)
        self.assertRaises(TypeError, CompanionCatalog.removeCompanion, '')
        self.assertRaises(TypeError, CompanionCatalog.removeCompanion, False)
        catalog = CompanionCatalog()
        catalogSize = len(catalog.companions)
        # nothing should be removed
        catalog.removeCompanion(Companion(user.fullname, 65, 150, 'introvert', 'dog', 'male'))
        self.assertEqual(catalogSize, len(catalog.companions))
        catalog.removeCompanion(catalog.companions[-1])
        # check if companions list is sucessfully updated when a companion is removed.
        self.assertEqual(catalogSize-1, len(catalog.companions))