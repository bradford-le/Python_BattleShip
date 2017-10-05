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

print_board(board)

print "random row: " + str(random_row(board))
print "random column: " + str(random_col(board))