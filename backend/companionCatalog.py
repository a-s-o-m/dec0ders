
from Companion import Companion

class CompanionCatalog:
    def __init__(self):
        '''
        data strucuture that stores all companions and their relevant information.
        All companions listed below are ones we have initially had on our website for project 1
        Each companion should have a name, description of personality, pet preference, and sex
        '''
        self.companions = [Companion('Dylan OBrien', 25, 200, 'extrovert','dog', 'male'),
        Companion('Amy Wind', 24, 110, 'introvert', 'cat', 'female'),
        Companion('Steve Johnson', 35, 250, 'extrovert','cat','male'),
        Companion('Stephanie Cheng', 30, 101, 'extrovert', 'cat', 'female'),
        Companion('Cristiano Lopez', 32, 200, 'introvert', 'dog', 'male'),
        Companion('Helena Rios', 27, 175, 'introvert', 'dog', 'female'),
        Companion('Kim Tae-hyung', 26, 200, 'introvert', 'dog', 'male'),
        Companion('Stephanie Pierce', 19, 120, 'extrovert', 'cat', 'female')] 

        

    def add_companion(self, new_companion):
        '''
        The add_companion function enables users to be able to add a new companion to the catalog if they wish. 
        This functions gathers all information and then appends the newly created companion to the catalog.
        '''
        if (not isinstance(new_companion, Companion)):
            raise TypeError("new companion must be instance of Companion class")
        self.companions.append(new_companion) # add new companion to catalog 

    def remove_companion(self, del_companion):
        '''
        The remove_companion function enables companions to be taken off of the catalog. Their attributes and self within 
        the catalog will be deleted, and updated.
        '''
        if (not isinstance(del_companion, Companion)):
            raise TypeError("the companion in which you wish to delete must be instance of Companion class")
        if (self.companions.__contains__(del_companion)):
            self.companions.remove(del_companion) 