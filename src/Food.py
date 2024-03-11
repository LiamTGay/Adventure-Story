import tkinter as tk
import os

class Food:
  
  def __init__(self):
    self.foodChoice = ""
    self.breakWall = False
  def FoodChoice(self):
      print("What would you like to eat today? ")
      print("1. 14 cakes")
      print("2. Large Burger")
      print("3. Protein powder(the gym calls)")
      food = input("Food Choice: ")
      if food == "1":
        foodType = "cakes"
        self.foodChoice = "1"
      elif food == "2":
        foodType = "burger"
        self.foodChoice = "2"
      elif food == "3":
        foodType = "protein"
        self.foodChoice = "3"
      else:
        print("Dont think you can get away without eating! I know your fat!")
        exit(0)
      os.system('clear||cls')
      print("you chose to eat " + foodType)
      print("Its time to leave the house! ")
  
  def LeaveHouse(self):
      if(self.foodChoice == "1"):
        os.system('clear||cls')
        print("you are too fat to fit through the door")
        print("you can either break down the wall or go through the window")
        choice1 = input("1. break down the wall or 2. go through the window")
        if choice1 == "1":
          os.system('clear||cls')
          print("You break down the wall")
          self.breakwall = True
        elif choice1 == "2":
          os.system('clear||cls')
          print("Oh my god! You are so fat you can't fit through the window either!")
          print("You have choose to go through the door instead")

      if(self.foodChoice == "2"):
        os.system('clear||cls')
        print("Congrats, you have left the house!")

      if(self.foodChoice == "3"):
        os.system('clear||cls')
        print("Congrats, you have left the house!")
