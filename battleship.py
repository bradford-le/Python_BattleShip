# Here is a python script for playing 1 player BattleShip

from random import randint

board = []
for i in range(5):
  board.append(['O'] * 5)
  
def print_board(board_in):
  for row in board_in:
    print " ".join(row)
    
def random_row(board_in):
  return randint(0,len(board_in)-1)

def random_col(board_in):
  return randint(0,len(board_in)-1)

ship_row = random_row(board)
ship_col = random_col(board)

print_board(board)

print "Ship Row: " + str(ship_row)
print "Ship Column: " + str(ship_col)

# Add your code below!
guess_row = int(raw_input("Guess Row: "))

guess_col = int(raw_input("Guess Col: "))