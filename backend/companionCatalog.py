
from Companion import Companion

class companionCatalog:
    def __init__(self):
        '''
        data strucuture that stores all companions and their relevant information. Each companion should have
        a name, description of personality, pet preference, and sex
        '''
        self.companions = [['Dylan OBrien', 'Still lives at home with his parents, but  at least hes off the streets', 'dog', 'male'],
        ['Amy Wind', 'Great at baking, but you have to wash the dishes', 'cat', 'female'],
        ['Steve Johnson', 'Can run a mile in 4 minutes, but he never shows up to a date on time','cat','male'],
        ['Stephanie Cheng', 'Looks like a kitten. Snores like a lion', 'cat', 'female'],
        ['Cristiano Lopez', 'Nice abs', 'dog', 'male'],
        ['Helena Rios', 'An aspiring dental student. She also is missing two teeth', 'dog', 'female'],
        ['Kim Tae-hyung', 'Loves to sing and dance. Has commitment issues', 'dog', 'male'],
        ['Stephanie Pierce', 'A cat lady, who is purrrrrfect', 'cat', 'female']]


    def addCompanion(self, new_companion):
        '''
        The addCompanion function enables users to be able to add a new companion to the catalog if they wish. 
        This functions gathers all information and then appends the newly created companion to the catalog.
        '''
        if (not isinstance(new_companion, Companion)):
            raise TypeError("new companion must be instance of Companion class")
        self.companions.append(new_companion) # add new companion to catalog 