

class Player:

  def __init__(self) -> None:
    self.kittens = 8
    self.cats = 0
    self.active_kittens = 0
    self.active_cats = 0


  def upgrade_cats(self):
    self.kittens -= 3
    self.cats += 3
    self.active_kittens -= 3

  def check_all_kittens(self):
    if self.active_kittens == 8:
      self.active_kittens -= 1
      self.cats += 1
      self.kittnes -= 1

  def check_all_cats_win(self):
    return self.active_cats == 8
  
  def remove_active_kitten(self):
    self.active_kittens -= 1

  def remove_active_cat(self):
    self.active_cats -= 1