import Player
# Board representation:

# ......
# ....o.
# x.....
# ......
# .X....
# ....O.

# x is player 1's kittens
# X is player 1's cats
# o is player 2's kittens
# O is player 2's cats

class Board:

  def __init__(self, player1: Player, player2: Player) -> None:
    self.board = [
      ['.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.']
    ]
    self.player1 = player1
    self.player2 = player2

  def make_move(self, player_piece, row, col):
    self.board[row][col] = player_piece
    self.check_boops(row, col)

  def check_boops(self, is_cat, row, col):
    upper_row = row - 1
    lower_row = row + 1
    left_col = col - 1
    right_col = col + 1

    # check all 8 spots where the cats could get booped:
    # upper left:
    if upper_row >= 0 and left_col >= 0:
      top_left_piece = self.board[upper_row][left_col]

      if top_left_piece != '.' and self.check_valid_boop(is_cat, top_left_piece):
          # check if this is a cat on the edge
          if upper_row == 0 or left_col == 0:
            player_to_boop = self.get_player(top_left_piece)
            if self.check_piece_is_kitten(upper_row, left_col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_top_left_piece = self.board[upper_row - 1][left_col - 1]
            if next_top_left_piece == '.':
              # we have a valid boop
              self.board[upper_row - 1][left_col - 1] = top_left_piece
              self.board[upper_row][left_col] = '.'
    
    # upper middle
    if upper_row >= 0:
      top_piece = self.board[upper_row][col]

      if top_piece != '.' and self.check_valid_boop(is_cat, top_piece):
          # check if this is a cat on the edge
          if upper_row == 0:
            player_to_boop = self.get_player(top_piece)
            if self.check_piece_is_kitten(upper_row, col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_top_piece = self.board[upper_row - 1][col]
            if next_top_piece == '.':
              # we have a valid boop
              self.board[upper_row - 1][col] = top_piece
              self.board[upper_row][col] = '.'

    # upper right
    if upper_row >= 0 and right_col < 6:
      top_right_piece = self.board[upper_row][right_col]

      if top_right_piece != '.' and self.check_valid_boop(is_cat, top_right_piece):
          # check if this is a cat on the edge
          if upper_row == 0 or right_col == 5:
            player_to_boop = self.get_player(top_right_piece)
            if self.check_piece_is_kitten(upper_row, right_col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_top_right_piece = self.board[upper_row - 1][right_col + 1]
            if next_top_right_piece == '.':
              # we have a valid boop
              self.board[upper_row - 1][right_col + 1] = top_right_piece
              self.board[upper_row][right_col] = '.'

    # left
    if left_col >= 0:
      left_piece = self.board[row][left_col]

      if left_piece != '.' and self.check_valid_boop(is_cat, left_piece):
          # check if this is a cat on the edge
          if left_col == 0:
            player_to_boop = self.get_player(left_piece)
            if self.check_piece_is_kitten(row, left_col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_left_piece = self.board[row][left_col - 1]
            if next_left_piece == '.':
              # we have a valid boop
              self.board[row][left_col - 1] = left_piece
              self.board[row][left_col] = '.'

    # right
    if right_col < 6:
      right_piece = self.board[row][right_col]

      if right_piece != '.' and self.check_valid_boop(is_cat, right_piece):
          # check if this is a cat on the edge
          if right_col == 5:
            player_to_boop = self.get_player(right_piece)
            if self.check_piece_is_kitten(row, right_col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_right_piece = self.board[row][right_col + 1]
            if next_right_piece == '.':
              # we have a valid boop
              self.board[row][right_col + 1] = right_piece
              self.board[row][right_col] = '.'

    # bottom left:
    if lower_row < 6 and left_col >= 0:
      bottom_left_piece = self.board[lower_row][left_col]

      if bottom_left_piece != '.' and self.check_valid_boop(is_cat, bottom_left_piece):
          # check if this is a cat on the edge
          if lower_row == 5 or left_col == 0:
            player_to_boop = self.get_player(bottom_left_piece)
            if self.check_piece_is_kitten(lower_row, left_col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_bottom_left_piece = self.board[lower_row + 1][left_col - 1]
            if next_bottom_left_piece == '.':
              # we have a valid boop
              self.board[lower_row + 1][left_col - 1] = bottom_left_piece
              self.board[lower_row][left_col] = '.'

    # lower middle
    if lower_row < 6:
      bottom_piece = self.board[lower_row][col]

      if bottom_piece != '.' and self.check_valid_boop(is_cat, bottom_piece):
          # check if this is a cat on the edge
          if lower_row == 5:
            player_to_boop = self.get_player(bottom_piece)
            if self.check_piece_is_kitten(lower_row, col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_bottom_piece = self.board[lower_row + 1][col]
            if next_bottom_piece == '.':
              # we have a valid boop
              self.board[lower_row + 1][col] = bottom_piece
              self.board[lower_row][col] = '.'

    # bottom right
    if lower_row < 6 and right_col < 6:
      bottom_right_piece = self.board[lower_row][right_col]

      if bottom_right_piece != '.' and self.check_valid_boop(is_cat, bottom_right_piece):
          # check if this is a cat on the edge
          if lower_row == 5 or right_col == 5:
            player_to_boop = self.get_player(bottom_right_piece)
            if self.check_piece_is_kitten(lower_row, right_col):
              player_to_boop.remove_active_kitten()
            else:
              player_to_boop.remove_active_cat()
          else: # need to check the next top left to see if it is blocked
            next_bottom_right_piece = self.board[lower_row + 1][right_col + 1]
            if next_bottom_right_piece == '.':
              # we have a valid boop
              self.board[lower_row + 1][right_col + 1] = bottom_right_piece
              self.board[lower_row][right_col] = '.'


    
  def check_piece_is_kitten(self, row, col):
    return self.board[row][col] == 'x' or self.board[row][col] == 'o'
  
  def get_player(self, piece):
    if piece == 'x' or piece == 'X':
      return self.player1
    else:
      return self.player2

  def check_valid_boop(self, is_cat, target_piece):
    if is_cat:
      return True
    elif target_piece == 'x' or target_piece == 'o':
      return True
    else:
      return False

  def check_win_or_upgrade(self):
    # This function will pass though all 6x6 tiles and see if there are any 3 in a row kittens
    # or any 3 in a row cats. Every time we hit a kitten, we call check_upgrade() which will check
    # the right, bottom_right, and bottom to see if there are 3 kittens in a row. 
    # Every time we hit a cat, we will call check_win() which will check the right, bottom_right
    # and bottom to see if there are 3 cats in a row
    pass

  def check_upgrade(self):
    # Check the right, bottom_right, and bottom to see if there are 3 kittens in a row. If so, take those kittens out
    # and give the player 3 cats.
    pass

  def check_win(self):
    # Check the right, bottom_right, and bottom to see if there are 3 cats in a row. If so this player wins the game!
    pass