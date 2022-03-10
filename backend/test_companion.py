import unittest

from Companion import Companion

# data for tests
description = ''
age = 18
height = "6'1"
personality = 'introvert'
pet_preference = 'dog'
gender = 'male'

companion = Companion(description, age, height, personality, pet_preference, gender)

# python3 -m unittest test_companion
class TestCompanion(unittest.TestCase):

    def test_init_types(self):
        # description, personality, pet_preference, gender must be strings
        self.assertRaises(TypeError, 'Billy Stewart', 18, 150, False, 'cat', 'male') # personality trait must be string
        self.assertRaises(TypeError, 'Timia Northcutt', 27, 'old', 'introvert', 1200, 'female') # animal preference must be string. age must be an int
        self.assertRaises(TypeError, 'Kousei Richeson', 27, '25', 'extrovert', 'dog', 'male') # height must be int or float
        self.assertRaises(TypeError, 'Vivian Alcala', '21', 175, 'introvert', 'dog', 'female') # age must be int
        self.assertRaises(TypeError, 'Luis Montes', 27, 175, 'introvert', 89, 'female') # animal preference must be string
        self.assertRaises(TypeError,'Renee Catanach', 27, 175, 'introvert', 'dog', False) # sex must be a string 
       

    def test_init_values(self):
        # age must be >= 18
        self.assertRaises(ValueError, 'Helena Rios', -52, 175, 'introvert', 'dog', 'female')
        # age cannnot be negative
        self.assertRaises(ValueError, 'Helena Rios', 101, 175, 'introvert', 'dog', 'female')
        # age must range from 18-100
        self.assertRaises(ValueError, 'Helena RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 101, 175, 'introvert', 'dog', 'female')
        # name should be between 2 and 30 characters long
        self.assertRaises(ValueError, 'Helena Rios', 101, 1, 'introvert', 'dog', 'female')
        # Minimum height should be higher than 100cm, maximum height should be lower or equal to 270cm
        self.assertRaises(ValueError, 'Helena Rios', 101, 1, 'fun', 'dog', 'female')
        # Personality should be either "introvert" or "extrovert"
        self.assertRaises(ValueError, 'Helena Rios', 101, 1, 'introvert', 'fish', 'female')
        # Pet preference should be either "dog" or "cat" (Case-insensitive)
        self.assertRaises(ValueError, 'Helena Rios', 101, 1, 'introvert', 'fish', 'dog')
        # Sex should be either "male" or "female" (Case-insensitive)

    def test_match(self):
        self.assertAlmostEqual(companion.calculate_match([20,25], [180,200], 'introvert', 'dog', 'male'),5555) 
        # TODO: ask angel about match function

# if __name__ == "__main__":
#     unittest.main() 