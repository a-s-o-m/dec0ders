
from Companion import Companion

class companionCatalog:
    def __init__(self):
    '''
    data strucuture that stores all companions and their relevant information
    '''
        self.companions = []


    def addCompanion(self, new_companion):
        if (not isinstance(new_companion, Companion)):
            raise TypeError("new companion must be instance of Companion class")
        self.companions.append(new_companion) # add new companion to catalog