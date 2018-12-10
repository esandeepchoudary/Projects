import random

suits = ('♠','♣','♦','♥')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}


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
        
    def draw_card(self):
        card = random.randint(0,len(self.deck))
        card_index = self.deck.index(card)
        self.deck.pop(card_index)
        return card

def print_card(card):
    card_list = card.split()
    symbol = card_list[0]
    value = vlaues[card_list[2]]
    print("------------")
    print(f"|{symbol}{value}         |")
    print("|           |")
    print("|           |")
    print(f"|    {symbol}{value}     |")
    print("|           |")
    print("|           |")
    print(f"|         {symbol}{value}|")
    print("------------")

class Player:

    chip=100
    sum=0
    player_card = []

    def first_adder(self):
        for item in player_card:
            st = item.split()
            sum+=values[st[2]]
    def chips(self):
        print(f"The player has {Player.chip} chips.")
        return
    
    def bet(self):
        self.bet_amount=int(input("Place the bet\n"))
        if self.bet_amount>Player.chip or self.bet_amount<=0:
            bet()
        return
    def hit():
        card = draw_card()
        print_card(card)
    
    def stand():
        global turn
        turn = h
    
    def adder():
        for ele in range(2,len(house_card)):
            st = house_card[ele].split()
            House.sum+=values[st[2]]    
        
    def plr_win(): 
        pass

class House:
    house_card = []
    sum=0

    def first_adder():
        for item in player_card:
            st = item.split()
            House.sum+=values[st[2]]

    def adder():
        for ele in range(2,len(house_card)):
            st = house_card[ele].split()
            House.sum+=values[st[2]]
    def hit():
        pass

    def stand():
        pass


turn = 'p'
game = 'on'
while game=='on':
    print("Game is on!!!!")
    plr = Player()
    plr.chips()
    plr.bet()
    h = House()
    d = Deck()
    d.shuffle()    
    Player.player_card.append(d.draw_card())
    Player.player_card.append(d.draw_card())
    print("Player cards:")
    print_card(player_card[0])
    print_card(player_card[1])
    House.house_card.append(d.draw_card())
    House.house_card.append(d.draw_card())
    print("House cards:")
    print_card(house_card[0])
    p.adder()
    h.adder()
    while turn == p:
        print("\n\nIts the players turn")
        player_choice = int(input("Press 1 for Hit\nPress 2 for Stand"))
        if player_choice == 1:
            p.hit()
        elif player_choice == 2:
            p.stand()
