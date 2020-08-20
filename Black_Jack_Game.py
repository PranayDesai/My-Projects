import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit
    
    def __str__(self):
        return self.rank+' of '+self.suit
    

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp =''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value=values[card.rank]+self.value
        
        if card.rank == 'Ace':
            self.aces = 1 + self.aces  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total= self.total + self.bet
        print(self.total)
    
    def lose_bet(self):
        self.total=self.total - self.bet
        print(self.total)


def take_bet(chips):
    while True:  
        try:
            chips.bet=int(input('Place Your bet!!\n'))
        except:
            print("you can't place this bet\n")
        else:
            if chips.bet > chips.total:
                print("sorry your bet can't exceed\n ",chips.total)
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while playing:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'\n")
        
        if x[0].lower()=='h':
            hit(deck,hand)
        
        elif x[0].lower()=='s':
            print("Player stands , Dealer is playing....\n")
            playing = False
        
        else:
            print("Sorry, Please try again.\n")
            continue
            
        break    



def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)   


def player_busts(player,dealer,chips):
    print('Player busts !!\n')
    chips.lose_bet()
    print("\nPlayer's winnings stand at",chips.total)


def player_wins(player,dealer,chips):
    print("Player wins !!\n")
    chips.win_bet()
    print("\nPlayer's winnings stand at",chips.total)


def dealer_busts(player,dealer,chips):
    print("Dealer busts !!\n")
    chips.win_bet()
    print("\nPlayer's winnings stand at",chips.total)
 
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins !!\n")
    chips.lose_bet()
    print("\nPlayer's winnings stand at",chips.total)

    
def push():
    print("Dealer and Player tie! It's a push.\n")




while True:
    print("_____BLACK JACK_____\n")
    print("Welcome to the table !!\n")
    print("Get as close to 21 as you can without going over!\n")
    print("Dealer hits until she reaches 17.\n")
    print(" Aces count as 1 or 11.\n")
    
    deck=Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips=Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
      
        
    
    while playing: 
        
        hit_or_stand(deck,player_hand)
        
        show_some(player_hand,dealer_hand)   
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break 
           
    if player_hand.value <= 21:
        
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)    

            
            show_all(player_hand,dealer_hand)

            
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)


    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break       

