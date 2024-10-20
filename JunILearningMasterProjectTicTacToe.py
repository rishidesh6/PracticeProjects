import random
import copy

people = ["computer", "user"]
selectedChoice = random.choice(people)
game = [[" "," "," "], [" "," "," "], [" "," "," "]]


def playerChoice(board):
  while(True):
    row = input("Please enter which row you want to play in here: ")
    column = input("Please enter which column you want to play in here: ")
    if int(row) > 2 and int(row) < 0 or int(column) > 2 and int(column) < 0:
      print("Both answers need to be less than or equal to 2! ")
      
    elif board[int(row)][int(column)] != " ":
      print("This spot is already taken, please try again.")
    
    else:
      game[int(row)][int(column)] = "O"
      break

'''def computerChoice(board):
  row = random.randint(0, 2)
  column = random.randint(0, 2)
  
  while board[row][column] != " ":
    row = random.randint(0, 2)
    column = random.randint(0, 2)
  board[row][column] = "X"
  return board'''


def forking(board, player, row, column):
   board2 = copy.deepcopy(board)
   if board2[row][column] == " ":
     board2[row][column] = player
     wins = 0
     for i in range(0, 3):
       for j in range(0, 3):
         if board2[i][j] == " ":
           board2[i][j] = player
           if win(board2, player):
             wins += 1
           board2[i][j] = " "
     if wins >= 2:
       return True
   return False
            
def computerChoice(board):
  for i in range(0, 3):
    for j in range(0, 3):
      if board[i][j] == " ":
        board[i][j] = "X"
        if win(board, "X"):
          return 
        else:
          board[i][j] = " "
          
  for i in range(0, 3):
    for j in range(0, 3):
      if board[i][j] == " ":
        board[i][j] = "O"
        if win(board, "O"):
          board[i][j] = "X"
          return
        else:
          board[i][j] = " "
          
  for i in range(0, 3):
    for j in range(0, 3):
      if forking(game, "O", i, j):
        game[i][j] = "X"
        return
      
  for i in range(0, 3):
    for j in range(0, 3):
      if forking(game, "X", i, j):
        game[i][j] = "X"
        return
  
  
  if board[1][1] == " ":
      board[1][1] = "X"
      return
    
    
  full = 0    
  while (full < 4):
    randomLoc = random.randint(0, 3)
    
    
    if randomLoc == 0:
      if board[0][0] == " ":
        board[0][0] = "X"
        return
      else:
        full += 1
        
    elif randomLoc == 1:
      if board[0][2] == " ":
        board[0][2] = "X"
        return
      else:
        full += 1
      
    elif randomLoc == 2:
      if board[2][0] == " ":
        board[2][0] = "X"
        return
      else:
        full += 1
        
    elif randomLoc == 3:
      if board[2][2] == " ":
        board[2][2] = "X"
        return 
      else:
        full += 1
        
       
  full = 0    
  while (full < 4):
    randomLoc = random.randint(0, 3)
    
    
    if randomLoc == 0:
      if board[0][1] == " ":
        board[0][1] = "X"
        return
      else:
        full += 1
        
    elif randomLoc == 1:
      if board[1][0] == " ":
        board[1][0] = "X"
        return
      else:
        full += 1
      
    elif randomLoc == 2:
      if board[1][2] == " ":
        board[1][2] = "X"
        return
      else:
        full += 1
        
    elif randomLoc == 3:
      if board[2][1] == " ":
        board[2][1] = "X"
        return
      else:
        full += 1  
  return    

def printBoard(game):
  for i in range(0, 3):
    for j in range(0, 3):
      if j <= 1:
        print(" " + game[i][j] + " |", end='')
      else:
        print(" " + game[i][j], end='')
    if i <= 1:
      print("\n---+---+---")
  print("")
      
def win(board, player):
  for i in range(0, 3):
    if board[i][0] == player and board[i][1] == player and board[i][2] == player:
      return True
  for j in range(0, 3):
    if board[0][j] == player and board[1][j] == player and board[2][j] == player:
      return True
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def draw(board):
  for i in range(0, 3):
    for j in range(0, 3):
      if board[i][j] == " ":
        return False
  return True


while(True):
  print("\n")
  printBoard(game)
  
  print("Now Playing: " + selectedChoice)
  if selectedChoice == "user":
    playerChoice(game)
    if win(game, "O"):
      printBoard(game)
      print("Human won!")
      break
    if draw(game):
      printBoard(game)
      print("There's a draw.")
      break
    selectedChoice = "computer"
    
  else:
    computerChoice(game)
    if win(game, "X"):
      printBoard(game)
      print("Computer won!")
      break
    if draw(game):
      printBoard(game)
      print("There's a draw.")
      break
    selectedChoice = "user"
