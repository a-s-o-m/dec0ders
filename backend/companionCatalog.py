
from Companion import Companion

class CompanionCatalog:
    def __init__(self):
        '''
        data strucuture that stores all companions and their relevant information. Each companion should have
        a name, description of personality, pet preference, and sex
        '''
        self.companions = [Companion('Dylan OBrien', 25, 200, 'extrovert','dog', 'male'),
        Companion('Amy Wind', 24, 110, 'introvert', 'cat', 'female'),
        Companion('Steve Johnson', 35, 250, 'extrovert','cat','male'),
        Companion('Stephanie Cheng', 30, 101, 'extrovert', 'cat', 'female'),
        Companion('Cristiano Lopez', 32, 200, 'introvert', 'dog', 'male'),
        Companion('Helena Rios', 27, 175, 'introvert', 'dog', 'female'),
        Companion('Kim Tae-hyung', 26, 200, 'introvert', 'dog', 'male'),
        Companion('Stephanie Pierce', 19, 120, 'extrovert', 'cat', 'female')]


    def addCompanion(self, new_companion):
        '''
        The addCompanion function enables users to be able to add a new companion to the catalog if they wish. 
        This functions gathers all information and then appends the newly created companion to the catalog.
        '''
        if (not isinstance(new_companion, Companion)):
            raise TypeError("new companion must be instance of Companion class")
        self.companions.append(new_companion) # add new companion to catalog 