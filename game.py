from dealer import Dealer
from trick import Trick
import os
from utils import gap

class Game:
    def __init__(self) -> None:
        self.username="User"
        self.dealer=Dealer()
        self.tricks=[]
        self.show_card=False
        self.score=[0 for i in range(4)]



    def start(self):

        """
    Client Interface

    1. Take name of the Player
    2. Show Dealed Card
    3. Play A Card
    4. Display Winner Of the Trick
    5. Play Next Card till last card
    
    """
        os.system('clear')

        """1. Take name of the Player"""
        # should we use a property ?? 

        player=self.get_player_name()
        print(f"Player 1: {player} ")

        """ ## 2. Show Dealed Card  """
        # should we instantiate it here or in another factory ??
        
        
        cards=self.dealer.getCards()
        #self.display_all_players_card(cards)
        
      
        #self.display_cards(cards)

        # print("your cards: ")
        # for card in cards:
        #     card.show()

        
        """ 3. Play Cards  """
        # TODO  will move to server interface for client communicaiton 
        # should we instantiate it here or in another factory ??
        # we can refactor this with new method or transferring to  Trick Class 
        trick_starter=0
        for i in range(13):
            trick=Trick()
            
            
            for player in range(trick_starter, 4+trick_starter):
                player=player%4

                self.scoreboard()
                self.display_all_players_card(cards)

                player_hand_cards=cards[player]
                trick.display_trick_state()
                print(f"Player {player+1} Cards: \n")
                

                self.display_cards(player_hand_cards)
                card_number=int(input("Play a Card:" ))

                trick.play(player_hand_cards[card_number-1],player)
                cards[player].remove(player_hand_cards[card_number-1])
                os.system('clear')

            
            self.scoreboard()
            trick.display_trick_state()
            

            """# !  -------     section     -------

            # !  Player One
        

            trick.display_trick_state()
            self.display_cards(cards)
            card_number=int(input("Play a Card:" ))
            trick.play(cards[card_number-1])
            os.system('clear')
            trick.display_trick_state()

            # !  Player two
            card_number=int(input("Play a Card:" ))
            trick.play(cards[card_number-1])
            trick.display_trick_state()

            # !  Player three
            card_number=int(input("Play a Card:" ))
            trick.play(cards[card_number-1])
            trick.display_trick_state()

            # !  Player four
            card_number=int(input("Play a Card:" ))
            trick.play(cards[card_number-1])
            trick.display_trick_state()

            # !  -------   end    section     -------"""

            

            """4. Display Winner Of the Trick"""
            self.tricks.append(trick)

            
            
            trick.display_winner()
            trick_starter= trick.get_winner_player()
            self.score[trick_starter]+=1
            input("\n\nPress enter to continue...")
            os.system('clear')
        self.scoreboard()
    
    ## 5. Play Next Card till last card
        


    def get_player_name(self):
        self.username=input("Enter your name: ")
        return self.username

    def display_cards(self, cards : list):
        hand= "\t".join(f"{card}" for card in cards)
        serial="\t\t".join(f"{i}" for i in range(1,len(cards)+1))
        print(f"{hand}\n{serial}")

        gap(4)

    def display_all_players_card(self,dealed_cards):
        if self.show_card:
            for i in range(4):
                print(f"\t Player {i+1} \t: \tCards")
                self.display_cards(dealed_cards[i])
                print("\n\n")
       
        
    def scoreboard(self):
        print("SCORECARD: ")
        if self.tricks:
            for trick in self.tricks:
                trick.display_winner()
        gap(1)

        if len(self.tricks)==13:
            self.display_player_stat()
            self.display_game_winner()
    
    def game_winner(self):
        max_win=max(self.score)
        return self.score.index(max_win) +1
    
    def display_game_winner(self):
        print(f"\t\t\tPlayer {self.game_winner()} Won !!!! ")
    
    def display_player_stat(self):
        for i in range(4):
            print(f"Player {i+1} --> {self.score[i]}")

        
        
            
        
        
        
    


    
    

            