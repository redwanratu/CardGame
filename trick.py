from card import Card
from utils import gap
class Trick:
    """ Trick Class :  Create a Trick object """
    
    rank_serial=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suit_serial=["Spade","Diamond","Club","Heart"]

    
    def __init__(self):
        self.cards=[]
        self.players=[]
        self.winner = None

    def play(self, card: Card,player):
        """ Allow Player to Play a Card """
        if len(self.cards) <= 4:

            self.cards.append(card)
            self.players.append(player)
            print(f"!!!! Played !!!! \t {card} ")
            
        else:
            print(f"Trick Finished")

    
    def get_winner(self):
        rank_serial=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        suit_serial=["Spade","Diamond","Club","Heart"]
        if len(self.cards) == 4:
            
            # TODO Code for find winner 
            # ? use hash to store data card instance
            top_card_serial_index=0
            trick_top_card= None
            
            # if i in range(len(self.cards))
            for card in self.cards:
               # check top cards with respect ot value_serial

                if  rank_serial.index(card._value) >top_card_serial_index:
                    top_card_serial_index=rank_serial.index(card._value)
                    
                    trick_top_index=self.cards.index(card)
                
            self.winner=self.players[trick_top_index]

            return self.cards[trick_top_index] , self.players[trick_top_index]  #, self.cards.index(trick_top_card)


    def display_winner(self):
        """ Display the Current Trick Winner """
        winner_card,winner_player=self.get_winner()
        print(f"Trick Winner  : Player {winner_player+1} --> {winner_card}")
        
    
    def display_trick_state(self):
        print("Cards On The Table")
        for card in self.cards:
            card.show()
        gap(2)
        
    def get_winner_player(self):
        return self.winner