class Companion:
    def __init__(self, description, age, height, personality, pet_preference, gender):
        str_parameters = [description, personality, pet_preference, gender]
        
        for parameter in str_parameters:
            if type(parameter) != str: raise TypeError(f"{parameter} must be a string.")

        if type(age) != int:
            raise TypeError("Age must be an integer")
        
        if type(height) not in [int, float]:
            raise TypeError("Height must be a number")
        
        self.description = description
        self.age = age
        self.height = height
        self.personality = personality
        self.pet_preference = pet_preference
        self.gender = gender

    def calculate_match(self, pref_age, pref_height, pref_personality, pref_pet, pref_gender):
        """Returns match percentage"""
        pref_matches = 0

        if pref_age[0] <= self.age <= pref_age[1]:
            pref_matches += 1

        if pref_height[0] <= self.height <= pref_height[1]:
            pref_matches += 1

        if pref_personality == pref_personality:
            pref_matches += 1

        if pref_pet == pref_pet:
            pref_matches += 1

        if pref_gender == pref_gender:
            pref_matches += 1

        return pref_matches / (0.5)


        