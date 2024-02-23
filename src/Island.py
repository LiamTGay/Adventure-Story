from Jungle import Jungle
from Forest import Forest

j1 = Jungle()
f1 = Forest()

class Island:

  def Arrive(self):
    print("You have arrived at the island.")
    print("On your right is a forest, and on your left is a jungle.")
    print("Type 1 for forest, and 2 for jungle.")
    direction = input("Which way do you want to go? ")

    if direction == "1":
      f1.GoToForest()
    elif direction == "2":
      j1.GoToJungle()