import os
from colorama import init, Fore, Style
import time
import random

init() # init colorama


win = False
lose = False


list_of_coor = []
txt = ""
Empty = "—"
PLAYER = "O"
AI = "X"


who_won = ""


def print_board(board):
  os.system('clear') # deleting everything
  print(Fore.YELLOW + '-' * 61)
  coordinate_why = 14
  
  for row in board:
    print(Fore.LIGHTCYAN_EX + "| " + ' | '.join(row) + " | " + str(coordinate_why))
    print(Fore.YELLOW + '-' * 61)
    coordinate_why -= 1
  print(Style.RESET_ALL + "  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14")

def is_game_over(board):
  global who_won
  
  #row -------
  for row in board: # --------
    player_in_row = 0
    ai_in_row = 0
    for move in row: #-
      
      if move == PLAYER:
          player_in_row += 1
          ai_in_row = 0
      elif move == AI:
          ai_in_row += 1
          player_in_row = 0


      if player_in_row >= 5:
        who_won = "PLAYER"
        return True
      elif ai_in_row >= 5:
        who_won = "AI"
        return True

  #columm |
  #       |
  for col in range(len(board[0])):
    for row in range(len(board) - 4):
      columm = [board[row + i][col] for i in range(5)]
      if columm == [PLAYER] * 5:
        who_won = "PLAYER"
        return True
      elif columm == [AI] * 5:
        who_won = "AI"
        return True

  # Diagonal
  for row in range(len(board) - 4):
    for col in range(len(board[0]) - 4):
        diagonal1 = [board[row + i][col + i] for i in range(5)]
        diagonal2 = [board[row + i][col + 4 - i] for i in range(5)]
        if diagonal1 == [PLAYER] * 5 or diagonal2 == [PLAYER] * 5:
            who_won = "PLAYER"
            return True
        elif diagonal1 == [AI] * 5 or diagonal2 == [AI] * 5:
            who_won = "AI"
            return True

  # tie
  if all(cell != Empty for row in board for cell in row):
      return True
      who_won = "No one"
  
  return False
  
def ai_turn(board):
    # Load recommendations from the file
    recommendations = load_recommendations()

    # Check if there are any recommendations available
    if recommendations:
        row, col = recommendations.pop(0)  # Get the first recommendation
        board[row][col] = AI

        # Save the remaining recommendations back to the file
        save_recommendations(recommendations)


def load_recommendations():
    recommendations = []
    with open("recommendations.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            row, col = line.strip().split(",")
            recommendations.append((int(row), int(col)))
    return recommendations


def save_recommendations(recommendations):
    with open("recommendations.txt", "w") as file:
        for recommendation in recommendations:
            row, col = recommendation
            file.write(f"{row},{col}\n")



def play_game():
  board = [[Empty] * 15 for _ in range(1, 16)]
  current_player = PLAYER

  while not is_game_over(board):
    if current_player == PLAYER:
      print_board(board)
      col = int(input("Enter the columm (x axis): "))
      row_ask = int(input("Enter the row (y axis): "))
      row = 14 - row_ask
      
      if board[row][col] == Empty:
        board[row][col] = PLAYER
        current_player = AI
      else:
        print("Invalid move. Try again.")
        time.sleep(1)
  
    else:
      print("Ai's turn")
      ai_turn(board)
      current_player = PLAYER
  print_board(board)

  if is_game_over(board):
    print(f"\n{who_won} won!")


play_game()