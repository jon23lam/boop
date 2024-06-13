# This file is the game file which will run each iteration of the game
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from backend.models.Board import Board
from backend.models.Player import Player



def game():
  player1 = Player(1)
  player2 = Player(2)
  board = Board(player1, player2)
  current_player = player1
  winner = None

  while winner is None:
    board.print()

    if current_player == player1:
      print("Player 1's turn:")
    else:
      print("Player 2's turn")
    
    # Assuming move is done in format: "2 3 x" where the first number is the row and the second is the col
    # and the last one is x/o for kitten or X/O for cat
    move = input()
    row = int(move[0])
    col = int(move[2])
    player_piece = move[4]

    board.make_move(player_piece, row, col)

    if player_piece == 'x' or player_piece == 'o':
      current_player.active_kittens += 1
    else:
      current_player.active_cats += 1

    winner = board.check_win_or_upgrade()

    if current_player == player1:
      current_player = player2
    else:
      current_player = player1
    
  print(f"The winner is: {winner}")









if __name__ == "__main__":
  game()