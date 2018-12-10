import random

def print_card(card):
    print("------------")
    print(f"|{card}         |")
    print("|           |")
    print("|           |")
    print(f"|    {card}     |")
    print("|           |")
    print("|           |")
    print(f"|         {card}|")
    print("------------")



print("♠♣♦♥")
print_card("6A")


suits = ('♦','♥','♠','♣')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

playing = True

class Card:
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(suit+"-"+rank)

    def __str__(self):
        return f"Cards {self.deck}"

    def shuffle(self):
        random.shuffle(self.deck)
        
    def 

test_deck = Deck()
print(test_deck)