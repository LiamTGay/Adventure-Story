import tkinter as tk

class CarDrive:

  def __init__(self):

    self.Icon = False
    self.Walk = False
    self.Spirit = False

  def Drive(self):
    print("You have hit a 3 way split in the road to go to the island.")
    print("1: Left you go on a all inclusive Icon Of The Seas cruise trip")
    print("2: Right you need to walk and swim")
    print("3: Forward you will take a Spirit Airlines Plane and drive it yourself")
    fork = input("Which way do you want to go?")

    if fork == "1":
      self.Icon = True
      print("You have choosen to take the Icon Of The Seas cruise trip")
    elif fork == "2":
      self.Walk = False
      print("You have choosen to walk and swim")
    elif fork == "3":
      self.Spirit = True
      print("You have choosen  to take the Spirit Airlines Plane")