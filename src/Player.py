from BossFight import BossFight
from Cave import Cave
c1 = Cave()
bf1 = BossFight()
class Player:

  def __init__(self):
    self.magic = False
    if c1.magic == True :
      self.magic = True