import unittest

from companion import Companion

# data for test_init_types and for test_init_values
description = ''
age = 18
height = 180
personality = 'introvert'
pet_preference = 'dog'
gender = 'male'
name = 'Dylan Obrien'
companion = Companion(name, age, height, personality, pet_preference, gender)

# data for match test
pref_age = [20,25]
pref_height = [180,200]
pref_personality = 'introvert'
pet_preference = 'dog'
sex_preference = 'male'


class TestCompanion(unittest.TestCase):

    def test_init_types(self):
        # description, personality, pet_preference, gender must be strings
        self.assertRaises(TypeError, Companion, 'Billy Stewart', 18, 150, False, 'cat', 'male') # personality trait must be string
        self.assertRaises(TypeError, Companion, 'Timia Northcutt', 27, 'old', 'introvert', 1200, 'female') # animal preference must be string. age must be an int
        self.assertRaises(TypeError, Companion, 'Kousei Richeson', 27, '25', 'extrovert', 'dog', 'male') # height must be int or float
        self.assertRaises(TypeError, Companion, 'Vivian Alcala', '21', 175, 'introvert', 'dog', 'female') # age must be int
        self.assertRaises(TypeError, Companion, 'Luis Montes', 27, 175, 'introvert', 89, 'female') # animal preference must be string
        self.assertRaises(TypeError, Companion, 'Renee Catanach', 27, 175, 'introvert', 'dog', False) # sex must be a string 
       

    def test_init_values(self):
        # age must be >= 18
        self.assertRaises(ValueError, Companion,'Helena Rios', -52, 175, 'introvert', 'dog', 'female')
        # age cannnot be negative 
        self.assertRaises(ValueError, Companion, 'Helena Rios', 101, 175, 'introvert', 'dog', 'female')
        # age must range from 18-100
        self.assertRaises(ValueError, Companion,'Helena RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR', 101, 175, 'introvert', 'dog', 'female')
        # name should be between 2 and 30 characters long
        self.assertRaises(ValueError, Companion, 'Helena Rios', 101, 1, 'introvert', 'dog', 'female')
        # Minimum height should be higher than 100cm, maximum height should be lower or equal to 270cm
        self.assertRaises(ValueError, Companion, 'Helena Rios', 101, 1, 'fun', 'dog', 'female')
        # Personality should be either "introvert" or "extrovert"
        self.assertRaises(ValueError, Companion,'Helena Rios', 101, 1, 'introvert', 'fish', 'female')
        # Pet preference should be either "dog" or "cat" (Case-insensitive)
        self.assertRaises(ValueError, Companion,'Helena Rios', 101, 1, 'introvert', 'fish', 'dog')
        # Sex should be either "male" or "female" (Case-insensitive)

    def test_match(self):
        self.assertAlmostEqual(companion.calculate_match(pref_age, pref_height, pref_personality, pet_preference, sex_preference),80) 
        

# if __name__ == "__main__":
#     unittest.main() 
# python3 -m unittest test_companion --> command line 