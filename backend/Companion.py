class Companion:
    def __init__(self, description, age, height, extraversion, dog_person, gender):
        self.description = description
        self.age = age
        self.height = height
        self.extraversion = extraversion
        self.dog_person = dog_person
        self.gender = gender

    def calculate_match(pref_age, preg_height, pref_personality, pref_pet, pref_gender):
        """Returns match percentage"""
        total = 0
        