from IPython.display import clear_output
from random import *
import os
def display_board(board):
    clear_output()
    os.system('cls')
    print(f"7 | 8 | 9")
    print(f"---------")
    print(f"4 | 5 | 6")
    print(f"---------")
    print(f"1 | 2 | 3")
    print("\n*********\n")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print(f"---------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"---------")
    print(f"{board[1]} | {board[2]} | {board[3]}")

def player_input():
    symbol = ''
    while not (symbol == 'x' or symbol == 'o'):
        symbol = input("Choose the symbol for the Player1: x or o\n")
    global player1
    global player2
    player1 = symbol
    if player1 == 'x':
        player2 = 'o'
    elif player1 == 'o':
        player2 = 'x'
    print("The symbol of Player2 is {0}\n**********************************\n".format(player2))

def place_marker(board, marker, position):
    print(f"here{type(position)}")
    if 1<=position and position<=9:
        board[position]=marker
    else:
    	print("Wrong number!!!!")

def win_check(board, mark):
    if mark == board[1] and mark == board[2] and mark == board[3]:
        return True
    elif mark == board[4] and mark == board[5] and mark == board[6]:
        return True
    elif mark == board[7] and mark == board[8] and mark == board[9]:
        return True
    elif mark == board[7] and mark == board[4] and mark == board[1]:
        return True
    elif mark == board[8] and mark == board[5] and mark == board[2]:
        return True
    elif mark == board[9] and mark == board[6] and mark == board[3]:
        return True
    elif mark == board[1] and mark == board[5] and mark == board[9]:
        return True
    elif mark == board[7] and mark == board[5] and mark == board[3]:
        return True
    else:
        return False

def choose_first():
    chs = randint(1,2)
    if chs == 1:
        return 'p1'
    else:
        return 'p2'

def full_board_check(board):
    for item in board:
        if item == '':
            return False
        else:
            return True

def player_choice(board):
    poscho = int(input("Enter the position to place your marker\n"))
    #while 1>poscho or poscho>9:
     #   poscho = int(input("Enter the position to place your marker\n"))
    while not(space_check(actual,poscho)):
    	poscho = int(input("Enter a different position\n"))
    return poscho


def space_check(board, position):
    if board[position] == '':
        return True
    else:
        return False

def deadlock():
	if turncount == 9:
		print("DEADLOCK!!!")
		global game
		game="off"

def replay():
    recho = input("Do you wan to continue playing\n Choose yes or no\n")
    if recho == 'yes':
    	return True
    else:
        return False

def reset():
	global actual 
	actual = ['o','','','','','','','','','']

os.system('cls')
print('Welcome to Tic Tac Toe!\n**********************************\nTHE NUMBER POSITIONS ARE AS FOLLOWS\n')
print(f"7 | 8 | 9")
print(f"---------")
print(f"4 | 5 | 6")
print(f"---------")
print(f"1 | 2 | 3")
turncount=0
player_input()
actual = ['o','','','','','','','','','']
first = choose_first()
if first == 'p1':
    print("Player 1 has the first move\n**********************************\n")
else:
    print("Player2 has the first move\n**********************************\n")
game = 'on'
turn = first
while game == 'on':
    if turn == 'p1':
        print("Player1 Turn:\n**********************************\n")
        pos = player_choice(actual)
        place_marker(actual,player1,pos)
        display_board(actual)
        turncount+=1
        turn = 'p2'
    else:
        print("Player2 Turn:\n**********************************\n")
        pos = player_choice(actual)
        place_marker(actual,player2,pos)
        display_board(actual)
        turncount+=1
        turn = 'p1'
    
    if win_check(actual,'x'):
            print("Player1 Won!!")
            if not(replay()):
                    game = 'off'
            else:
            	reset()
    elif win_check(actual,'o'):
            print("Player2 Won!!")
            if not(replay()):
                    game = 'off'
            else:
            	reset()
    if game=='on':
    	deadlock()

