from abc import ABC,abstractmethod

class Deck(ABC):
    """ 
    This is abstract class that builds  a complete deck of cards
    
    Atributes:
    cards (list): List of all cards in the deck

    Methods:
    _create_deck(): This method is abstract and must be implemented in subclass
    show() : This method is abstract and must be implemented in subcleass.
    """
    def __init__(self):
        self.cards=[]
        self._create_deck()
    
    @abstractmethod
    def _create_deck(self):
        """
        Build the list of cards in the deck

        """
        pass
    
    @abstractmethod
    def show(self):
        """
        Show all the cards in the deck
        """
        pass        


class Suffle(ABC):
    """  Abstract Suffle : will be subcllassed later"""
    def __init__(self,deck=None):
        self.deck=deck

    @abstractmethod
    def suffle(self):
        pass
    
    @abstractmethod
    def show(self):
        pass


class Deal(ABC):
    """ Abstract Deal Class """
    def __init__(self,deck=None):
        self.deck=deck
    
    @abstractmethod
    def deal(self):
        pass
