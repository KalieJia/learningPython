board = {
  "1": " ", "2": " ", "3": " ",
  "4": " ", "5": " ", "6": " ",
  "7": " ", "8": " ", "9": " "}
blankBoard = {
  "1": " ", "2": " ", "3": " ",
  "4": " ", "5": " ", "6": " ",
  "7": " ", "8": " ", "9": " "}

def ticTacToe():
  print("We all want to play tic tac toe!")
  player1 = input("Player 1, what is your name? Enter it here: ")
  player2 = input("Player 2, what is your name? Enter it here: ")
  print(player1 + " will be x and " + player2 + " will be o.")
  print("You guys will take turns choosing a square and filling it in with your symbol. The winner is whoever gets three in a row first, whether it be in a diagonal, horizontal, or vertical line.")
  
  checkStart = input("Ready to start? Type 'got it!' ")
  
  turn = player1
  piece = "x"
  count = 0
  
  while True:
    printBoard(board)
    move = input(turn + ", whhich square would you like to place your piece? Enter a number from 1 to 9: ")
    if move in board:
      if board[move] == " ":
          board[move] = piece
          count += 1
      else:
          print("That spot is already filled. Try again.")
          continue
    else:
      print("Invalid input. Enter an integer from 1 to 9.")
      continue

    if count >= 5:
      if board["7"] == board["8"] == board["9"] != " ": #across the top
        declare_winner(turn, piece)
        break
      elif board["4"] == board["5"] == board["6"] != " ":  #across the middle
        declare_winner(turn, piece)
        break
      elif board["1"] == board["2"] == board["3"] != " ":  #across the bottom
        declare_winner(turn, piece)
        break
      elif board["1"] == board["4"] == board["7"] != " ":  #down the left
        declare_winner(turn, piece)
        break
      elif board["2"] == board["5"] == board["8"] != " ":  #down the middle
        declare_winner(turn, piece)
        break
      elif board["3"] == board["6"] == board["9"] != " ":  #down the right
        declare_winner(turn, piece)
        break
      elif board["7"] == board["5"] == board["3"] != " ":  #diagonal
        declare_winner(turn, piece)
        break
      elif board["1"] == board["5"] == board["9"] != " ":  #diagonal
        declare_winner(turn, piece)
        break
    if count == 9:
        print("It's a tie!")
        printBoard(board)
        break
    if piece =="x":
        piece = "o"
        turn = player2
    else:
      piece = "x"
      turn = player1

def printBoard(board):
  print(board["1"] + " | " + board["2"] + " | " + board["3"])
  print("--+---+--")
  print(board["4"] + " | " + board["5"] + " | " + board["6"])
  print("--+---+--")
  print(board["7"] + " | " + board["8"] + " | " + board["9"])

def declare_winner(turn, piece):
  printBoard(board)
  print("Game Over")

  if piece == "x":
      print(turn + " won!")
  else:
      print(turn + " won!")

#Call the entire function and play the game!
ticTacToe()

restart = input("Would you like to play again? Type 'yes' or 'no': ")
if restart == "yes":
  board = blankBoard
  ticTacToe()
else:
  print("Thanks for playing!")