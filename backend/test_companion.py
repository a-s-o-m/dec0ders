import unittest
from Companion import Companion

# data for tests
description = ''
age = 18
height = "6'1"
personality = ''
pet_preference = 'dog'
gender = 'M'

companion = Companion(description, age, height, personality, pet_preference, gender)

# python3 -m unittest test_companion
class TestCompanion(unittest.TestCase):

    def test_init_types(self):
        # description, personality, pet_preference, gender must be strings
        self.assertRaises(TypeError, Companion, 0, age, height, personality, pet_preference, gender)
        self.assertRaises(TypeError, Companion, description, age, height, None, pet_preference, gender)
        self.assertRaises(TypeError, Companion, description, age, height, personality, False, gender)
        self.assertRaises(TypeError, Companion, description, age, height, personality, pet_preference, -1)
        # age must be an int
        self.assertRaises(TypeError, Companion, description, '5', height, personality, pet_preference, gender)
        self.assertRaises(TypeError, Companion, description, 5.5, height, personality, pet_preference, gender)
        # height must be an ....?
        # TODO: ask angel how he plans on measuring height

    def test_init_values(self):
        # age must be >= 18
        self.assertRaises(ValueError, Companion, description, 10, height, personality, pet_preference, gender)
        # age cannnot be negative
        self.assertRaises(ValueError, Companion, description, -1, height, personality, pet_preference, gender)
        # TODO: ask angel about other init values

    def test_match(self):
        pass
        # TODO: ask angel about match function

# if __name__ == "__main__":
#     unittest.main()