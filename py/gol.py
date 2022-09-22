#Game of Life
#Christopher De Silva
#CSCI 77800 Fall 2022
#collaborators: https://www.geeksforgeeks.org/conways-game-life-python-implementation/

#The Rules of Life:
#Survivals:
# A living cell with 2 or 3 living neighbours will survive for the next generation.
#Deaths:
#Each cell with >3 neighbours will die from overpopulation.
#Every cell with <2 neighbours will die from isolation.
#Births:
#Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.

import random #needed to randomly generate live cells

def gol():
#create a board 10 x 10 (not animated), called 5 times
  rows = 10
  cols = 10
  board = set_alive_cells(rows, cols) #create board using rows and cols. 
 
  for i in range(0, 6): #calls function 5 times 
    print("Generation %s:" % i)
    print_board(board)
    print()
    board = generate_next_board(board)

def set_alive_cells(rows, cols):
 #This function randomly sets the alive function based on rows and cols specified.  
  board = []
  for row in range(0, rows): 
    board.append([])
    for col in range(0, cols):
      if 0.5 > random.random():
        board[row].append("X")
      else:
        board[row].append("-")
  return board

#used to print the board
def print_board(board):
 
  for row in board:
    line = ""
    for col in row:
      line += col + " "
    print(line)

#creates the next board to using info from the previous generation 
def generate_next_board(board):
  new_board = []
  for row in range(0, len(board)):
    new_board.append([])
    for col in range(0, len(board[row])):
      new_board[row].append(get_next_gen_cell(board, row, col))
  return new_board

# This sets cell to either dead or alive based on neightbors. 
def get_next_gen_cell(board, r, c):
  nextGenCell = '-'
  neighbours = count_neighbours(board, r, c)
  if board[r][c] == 'X':
    if neighbours < 2 or neighbours > 3:
      nextGenCell = '-' 
    else:
      nextGenCell = 'X' 
  elif neighbours == 3:
    nextGenCell = 'X'
  return nextGenCell

#Checks to the amount of living neighbors to keep alive cells.
def count_neighbours(board, r, c):
  living_neighbors = 0
  for i in range(r-1, r+2): 
    if i >= 0 and i < len(board): 
      for j in range(c-1, c+2): 
        if j >= 0 and j < len(board[r]):
          if i==r and j==c:
            continue
          elif board[i][j] == 'X':
            living_neighbors += 1
  return living_neighbors
  
# Starts Game of life  
gol()