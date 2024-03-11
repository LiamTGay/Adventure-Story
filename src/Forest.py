import tkinter as tk
import time
from Jungle import Jungle
import os

j1 = Jungle()

class Forest:

  def GoToForest(self):
    os.system('clear||cls')
    print("You chose to walk through the Forest")
    print("Oh no! You have swept up by a pelican!")
    time.sleep(4)
    print("You have blacked out and been taken to their nest")
    time.sleep(5)
    os.system('clear||cls')
    print("Cawcaww! Cawcaww! Cawcaww!")
    translate = input("Type 1 to learn pelicano: ")

    if translate == "1":
      os.system('clear||cls')
      print("Hello there! I am the pelican that took you!")
      print("It has been three months since you were awake")
      print("You now walk and talk like a pelican")
      print("What are you going to do now?")
      print("1: Eat some food")
      print("2: Leave the nest, and learn the ways of humans again")
      nestchoice = input("What do you choose: ")
    else:
      os.system('clear||cls')
      print("Cawcaww! Cawcaww! Cawcaww!")


    if nestchoice == "1":
      os.system('clear||cls')
      print("There is a solomander on the ground")
      print("Do you want to dive down and eat it?")
      eating = input("type 1 to swoop down and eat it, type 2 to leave it alone: ")
      if eating == "1":
        os.system('clear||cls')
        print("You have eaten the solomander")
        print("You have been poisoned and have died")
        exit(0)
      elif eating == "2":
        os.system('clear||cls')
        print("You have starved to death")
        exit(0)
    elif nestchoice == "2":
      os.system('clear||cls')
      print("You have realized your human form again, congrats")
      print("Time to leave this scary forest, and now enter the jungle")
      j1.GoToJungle()
    
      