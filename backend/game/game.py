# This file is the game file which will run each iteration of the game
import sys
import os

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
      current_player_turn = "Player 1's turn: "
    else:
      current_player_turn = "Player 2's turn: "
    
    print(f"Available kittens: {current_player.kittens - current_player.active_kittens}")
    print(f"Available cats: {current_player.cats - current_player.active_cats}")
    # Assuming move is done in format: "2 3 x" where the first number is the row and the second is the col
    # and the last one is x/o for kitten or X/O for cat
    move = input(current_player_turn)
    valid_move, validated_move, error_message = check_valid_move(move, current_player)

    while not valid_move:
      move = input(error_message)
      valid_move, validated_move, error_message = check_valid_move(move, current_player)
      
    row = int(validated_move[0])
    col = int(validated_move[2])
    piece = validated_move[4]

    if piece == 'k':
      player_piece = current_player.kitten_piece
      current_player.active_kittens += 1
    else:
      player_piece = current_player.cat_piece
      current_player.active_cats += 1

    board.make_move(player_piece, row, col)

    winner = board.check_win_or_upgrade()

    if current_player == player1:
      current_player = player2
    else:
      current_player = player1
    
  print(f"The winner is: Player {winner.player}")

def check_valid_move(move: str, player: Player):
  valid_move = True
  error_message = None

  if len(move) != 5:
    valid_move = False
    error_message = "That is not a valid move. Please make sure that moves are in the format: 'num num piece' where the first number is the row and the second is the col and the last one is k for kitten or c for cat: "
  else:
    row = int(move[0])
    col = int(move[2])
    player_piece = move[4]

    if (row < 0 or row >= 6) or (col < 0 and col >= 6) or (player_piece != 'k' and player_piece != 'c'):
      valid_move = False
      error_message = "That is not a valid move. Please make sure that moves are in the format: 'num num piece' where the first number is the row and the second is the col and the last one is k for kitten or c for cat: "
    elif player_piece == 'k' and player.active_kittens + 1 > player.kittens:
      valid_move = False
      error_message = "You do not have enough kittens to make that move. Please try again: "
    elif player_piece == 'c' and player.active_cats + 1 > player.cats:
      valid_move = False
      error_message = "You do not have enough cats to make that move. Please try again: "


  return valid_move, move, error_message

if __name__ == "__main__":
  game()