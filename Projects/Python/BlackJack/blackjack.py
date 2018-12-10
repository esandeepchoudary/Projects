import random
import os
import sys
import time

suits = ['♠','♣','♦','♥']
ranks = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}

deck=[]
for suit in suits:
            for rank in ranks:
                deck.append(suit+"-"+rank)

def shuffle():
        random.shuffle(deck)       

def print_card(card):
    card_list = card.split('-')
    symbol = card_list[0]
    if card_list[1] in ['jack','queen','king','ace']:
    	value = card_list[1]
    else:
    	value = values[card_list[1]]
    print("---------------")
    print(f"|{symbol}{value}         |\n\n")
    
    print(f"|    {symbol}{value}     |\n\n")
    
    print(f"|         {symbol}{value}|")
    print("---------------")       

def draw_card():
        ind = random.randint(0,len(deck))
        card=deck[ind]
        deck.pop(ind)
        return card

def plsum():
	playersum=0
	for c in playercards:
		st=c.split('-')
		playersum+=values[st[1]]
	return playersum


def end():
	sys.exit(0)
os.system('cls')
playersum = 0 
housesum = 0
game = 'on'
playercards=[]
housecards=[]
shuffle()
bet=0
chips=100
playercards.append(draw_card())
playercards.append(draw_card())
housecards.append(draw_card())
housecards.append(draw_card())
print("House cards:")
print(f"***Card 1 is enclosed***{housecards[0]}")
time.sleep(1)
print_card(housecards[1])
for c in housecards:
	st=c.split('-')
	housesum+=values[st[1]]
print("Players cards:")
for c in playercards:
	time.sleep(1)	
	print_card(c)

print(f"The sum of ur cards is {plsum()}")
while game == 'on':
	print(f"No of chips available with player is: {chips}")
	while (bet<=0 or bet>100):
		bet=int(input("Enter the bet amount\n"))
	turn = "p"
	while turn == 'p':
		playerchoice=int(input("Enter 1 to hit\nEnter 2 to stand\n"))
		if playerchoice==1:
			time.sleep(1)
			dc = draw_card()
			print_card(dc)
			playercards.append(dc)
			psum=plsum()
			print(f"The sum of ur cards is {psum}")
			if psum>21:
				print("Player lost!!")
				chips-=bet
				print(f"The player chips are {chips}")
				end()
		else:
			turn = 'h'

	while turn=='h':
		print("House turn!!")
		time.sleep(5)
		housechoice=1
		if housesum>17:
			housechoice = random.randint(1,2)
		if housechoice == 1:
			print("House wants to HIT")
			time.sleep(1)
			dc = draw_card()
			print_card(dc)
			housecards.append(dc)
			dc=c.split('-')
			housesum+=values[dc[1]]
			if housesum>21:
				print(f"House sum = {housesum}\nHouse lost!!")
				chips+=(bet*2)
				print(f"The player chips are {chips}")
				end()
		else:
			print("The house wants to stand\n\n")
			print(f"The sum of house cards is {housesum}")
			if housesum<plsum():
				print("House lost!!")
				chips+=(bet*2)
				print(f"The player chips are {chips}")
				end()
			else:
				print("Player lost!!")
				chips-=bet
				print(f"The player chips are {chips}")
				end()