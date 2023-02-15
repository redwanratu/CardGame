from abstract import Suffle
import random

class RegularSuffle(Suffle):
    def __init__(self, deck=None):
        super().__init__(deck)
        self.deal_deck=[]
        
    
    def suffle(self):
        self.deck=random.sample(self.deck,len(self.deck))
        return self
        

    def show(self):
        i=1
        for player_deck in self.deal_deck:
            print(f"******  Player {i}   ********")
            for card in player_deck:
                card.show()
            i+=1
        return self
            
    def deal(self,no_of_player=4,card_per_deal=1):
        if len(self.deck) % no_of_player != 0:
            raise ValueError(" Can,t equally distributed")
        
        player_deck=[]
        for player in range(no_of_player):
            for i in range(player,len(self.deck),no_of_player):
                player_deck.append(self.deck[i])
            self.deal_deck.append(player_deck)
            player_deck=[]
        return self
    
    def get_player_cards(self):
        return self.deal_deck

        
