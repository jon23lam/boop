from .Player import Player

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
    if player_piece == 'X' or player_piece == 'O':
      is_cat = True
    else:
      is_cat = False

    self.check_boops(is_cat, row, col)

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
            self.board[upper_row][left_col] = '.'
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
            self.board[upper_row][col] = '.'
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
            self.board[upper_row][right_col] = '.'
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
            self.board[row][left_col] = '.'
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
            self.board[row][right_col] = '.'
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
            self.board[lower_row][left_col] = '.'
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
            self.board[lower_row][col] = '.'
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
            self.board[lower_row][right_col] = '.'
          else: # need to check the next top left to see if it is blocked
            next_bottom_right_piece = self.board[lower_row + 1][right_col + 1]
            if next_bottom_right_piece == '.':
              # we have a valid boop
              self.board[lower_row + 1][right_col + 1] = bottom_right_piece
              self.board[lower_row][right_col] = '.'


    
  def check_piece_is_kitten(self, row, col) -> bool:
    return self.board[row][col] == 'x' or self.board[row][col] == 'o'
  
  def check_piece_is_cat(self, row, col) -> bool:
    return self.board[row][col] == 'X' or self.board[row][col] == 'O'
  
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
    # This function will pass though all tiles and see if there are any 3 in a row kittens
    # or any 3 in a row cats. Every time we hit a kitten, we call check_upgrade() which will check
    # the right, bottom_right, and bottom to see if there are 3 kittens in a row. 
    # Every time we hit a cat, we will call check_win() which will check the right, bottom_right
    # and bottom to see if there are 3 cats in a row.
    # Note: Do not need to check row and diagonal on last 2 columns
    # Do not need to check column and diagonal on last 2 rows
    
    # Frist check and see if any player has all 8 cats on the board:
    if self.player1.check_all_cats_win():
      return self.player1
    elif self.player2.check_all_cats_win():
      return self.player2
    
    for row in range(6):
      for col in range(6):
        if self.check_piece_is_kitten(row, col):
          self.check_upgrade(row, col)

        if self.check_piece_is_cat(row, col):
          winning_player = self.check_win(row, col)
          if winning_player:
            return winning_player


  def check_upgrade(self, row, col):
    # Check the right, bottom_right, and bottom to see if there are 3 kittens in a row. If so, take those kittens out
    # and give the player 3 cats.
    player = self.get_player(self.board[row][col])
    piece_to_check = player.kitten_piece

    if col < 4:
      # Check next 3 to see if they are the same piece
      if self.board[row ][col + 1] == piece_to_check and self.board[row][col + 2] == piece_to_check:
        player.upgrade_cats()
        self.board[row][col] = '.'
        self.board[row][col + 1] = '.'
        self.board[row][col + 2] = '.'

    if row < 4:
      # Check next 3 to see if they are the same piece
      if self.board[row + 1][col] == piece_to_check and self.board[row + 2][col] == piece_to_check:
        player.upgrade_cats()
        self.board[row][col] = '.'
        self.board[row + 1][col] = '.'
        self.board[row + 2][col] = '.'
    
    if col < 4 and row < 4:
      # Check next 3 to see if they are the same piece
      if self.board[row + 1][col + 1] == piece_to_check and self.board[row + 2][col + 2] == piece_to_check:
        player.upgrade_cats()
        self.board[row][col] = '.'
        self.board[row + 1][col + 1] = '.'
        self.board[row + 2][col + 2] = '.'



  def check_win(self, row, col):
    # Check the right, bottom_right, and bottom to see if there are 3 cats in a row. If so this player wins the game!
    player = self.get_player(self.board[row][col])
    piece_to_check = player.cat_piece

    if col < 4:
      # Check next 3 to see if they are the same piece
      if self.board[row ][col + 1] == piece_to_check and self.board[row][col + 2] == piece_to_check:
        return player

    if row < 4:
      # Check next 3 to see if they are the same piece
      if self.board[row + 1][col] == piece_to_check and self.board[row + 2][col] == piece_to_check:
        return player
    
    if col < 4 and row < 4:
      # Check next 3 to see if they are the same piece
      if self.board[row + 1][col + 1] == piece_to_check and self.board[row + 2][col + 2] == piece_to_check:
        return player

    # If no player has won yet, return None
    return None
  
  def print(self):
    print(f"    0    1    2    3    4    5")
    print(f"0 {self.board[0]}")
    print(f"1 {self.board[1]}")
    print(f"2 {self.board[2]}")
    print(f"3 {self.board[3]}")
    print(f"4 {self.board[4]}")
    print(f"5 {self.board[5]}")