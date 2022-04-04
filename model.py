class Companion:
    def __init__(self, name: str, age: int, height: float, personality: str, pet_preference: str, sex: str, picture: str, description: str):
        '''
        Holds the information for the rentable dates

        Arguments:
        name: Between 2 and 30 characters long.
        age: Between 18 and 100.
        height:  Geight in centimeters. Between 100 and 270
        personality:  "Introverted" or "Extroverted". Case-insensitve.
        pet:  Pet preference; "Dog" or "Cat". Case-insensitive.
        sex:  "Male" or "Female". Case-insensitive.
        '''
        str_parameters = [name, personality, pet_preference, sex, picture, description]
        
        for parameter in str_parameters:
            if type(parameter) != str: raise TypeError(f'{parameter} must be a string.')

        if type(age) != int:
            raise TypeError('age must be an integer.')
        
        if type(height) not in [int, float]:
            raise TypeError('height must be a number.')
        
        personality = personality.lower()
        pet_preference = pet_preference.lower()
        sex = sex.lower()

        if len(description) > 100: raise ValueError('description should be less than 100 characters.')
        if not 2 <= len(name) <= 30: raise ValueError('name should be between 2 and 30 characters long.') 
        if not 18 <= age <= 100: raise ValueError('Minimum age should be higher than 18, maximum age should be lower or equal to 100.')
        if not 100 <= height <= 270: raise ValueError('Minimum height should be higher than 100cm, maximum height should be lower or equal to 270cm.')
        if personality not in ['introvert','extrovert']: raise ValueError('Personality should be either "introvert" or "extrovert" (Case-insensitive).')
        if pet_preference not in ['dog','cat']: raise ValueError('Pet preference should be either "dog" or "cat" (Case-insensitive).')
        if sex not in ['male','female']: raise ValueError('Sex should be either "male" or "female" (Case-insensitive).')
        
        self.name = name
        self.age = age
        self.height = height 
        self.personality = personality
        self.pet_preference = pet_preference
        self.sex = sex
        self.description = description
        self.picture = picture

    def to_document(self):
        return {
            "name": self.name,
            "age" : (str)(self.age),
            "height": (str)(self.height),
            "type": self.personality,
            "animal": self.pet_preference,
            "gender": self.sex,
            "pic": self.picture,
            "description": self.description,
        }

    def from_document(self, document):
        self.name = document["name"]
        self.age = document["age"]
        self.height = document["height"]
        self.personality = document["type"]
        self.pet_preference = document["animal"]
        self.sex = document["gender"]
        self.picture = document["pic"]
        self.description = document["description"]

    def calculate_match(self, pref_age: [int], pref_height: [float], pref_personality: str, pref_pet: str, pref_sex: str) -> int:
        '''
        Calculates the match percentage to the current Companion object with the given arguments.

        Arguments:
        pref_age:  a list of two int values, represents the user's preferred age range (18-100). Values are inclusive.
        pref_height:  a list of two float values, represents the user's preferred height range in centimeters (100-270). Values are inclusive.
        pref_personality:  a str representing the user's preferred personality; "Introverted" or "Extroverted". Case-insensitve.
        pref_pet:  a str representing the user's preferred Companion's pet preference; "Dog" or "Cat". Case-insensitive.
        pref_sex:  a str representing the user's preferred Companion's sex; "Male" or "Female". Case-insensitive.

        Returns an int value representing the match percentage. e.g, 20, 80, 100
        '''

        str_parameters = [pref_personality, pref_pet, pref_sex]
        for parameter in str_parameters:
            if type(parameter) != str: raise TypeError(f'{parameter} must be a string.')
        
        if len(pref_age) != 2: raise TypeError('pref_age list should contain 2 int values.')
        if len(pref_height) != 2: raise TypeError('pref_height list should contain 2 float or int values')

        pref_personality = pref_personality.lower()
        pref_pet = pref_pet.lower()
        pref_sex = pref_sex.lower()

        if pref_age[0] < 18 or pref_age[1] > 100: raise ValueError('pref_age should be between 18 and 100.')
        if pref_age[0] > pref_age[1]: raise ValueError('pref_age: first value must be less than or equal to the second value') 
        if pref_height[0] < 100 or pref_height[1] > 270: raise ValueError('pref_height should be between 100cm and 270cm')
        if pref_height[0] > pref_height[1]: raise ValueError('pref_height: first value must be less than or equal to the second value')
        if pref_personality not in ['introvert','extrovert']: raise ValueError('pref_personality should be either "introvert" or "extrovert" (Case-insensitive).')
        if pref_pet not in ['dog','cat']: raise ValueError('pref_pet should be either "dog" or "cat" (Case-insensitive).')
        if pref_sex not in ['male','female']: raise ValueError('pref_sex should be either "male" or "female" (Case-insensitive).')

        matches = 0

        if pref_age[0] <= self.age <= pref_age[1]:
            matches += 1

        if pref_height[0] <= self.height <= pref_height[1]:
            matches += 1

        if pref_personality == self.personality:
            matches += 1

        if pref_pet == self.pet_preference:
            matches += 1

        if pref_sex == self.sex:
            matches += 1

        return matches / (0.05)

class CompanionCatalog:
    def __init__(self):
        '''
        data strucuture that stores all companions and their relevant information.
        All companions listed below are ones we have initially had on our website for project 1
        Each companion should have a name, description of personality, pet preference, and sex
        '''
        self.companions = [Companion('Dylan OBrien', 25, 200, 'extrovert','dog', 'male',"static/assets/man1.jpg", "" ),
        Companion('Amy Wind', 24, 110, 'introvert', 'cat', 'female', "static/assets/woman1.jpg", ""),
        Companion('Steve Johnson', 35, 250, 'extrovert','cat','male', "static/assets/man2.jpg", ""),
        Companion('Stephanie Cheng', 30, 101, 'extrovert', 'cat', 'female', "static/assets/woman2.jpg", ""),
        Companion('Cristiano Lopez', 32, 200, 'introvert', 'dog', 'male', "static/assets/men3.jpg", ""),
        Companion('Helena Rios', 27, 175, 'introvert', 'dog', 'female', "static/assets/woman3.jpg", ""),
        Companion('Kim Tae-hyung', 26, 200, 'introvert', 'dog', 'male', "static/assets/man4.jpg", ""),
        Companion('Stephanie Pierce', 19, 120, 'extrovert', 'cat', 'female', "static/assets/woman4.jpg", ""),
        Companion('Shyla Vihaan', 30, 205,'extrovert', 'cat', 'male', "static/assets/men5.jpg", "")] 

    def addCompanion(self, new_companion):
        '''
        The add_companion function enables users to be able to add a new companion to the catalog if they wish. 
        This functions gathers all information and then appends the newly created companion to the catalog.
        '''
        if (not isinstance(new_companion, Companion)):
            raise TypeError("new companion must be instance of Companion class")
        self.companions.append(new_companion) # add new companion to catalog 
