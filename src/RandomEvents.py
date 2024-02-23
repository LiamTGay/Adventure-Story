import random

class RandomEvents:
  def __init__(self):
    self.randomEvent = ""

  def lightning(self):
    if random.randint(1,15300) == 1:
      print("you have been struck by lightning and burnt to a crisp")
      exit(0)
            
  def CarCrash(self):
    if random.randint(1,366) == 1:
      print("You have been hit by a car and died")