##Grayson Carter
import tkinter as tk
from Food import Food
import time
from BossFight import BossFight
import random
from Cave import Cave
import os

b1 = BossFight()
f1 = Food()
c1 = Cave()

class Jungle:

  def __init__(self):
    self.JungleFood = ""
    self.OwnWheelChair = False

  def GoToJungle(self):
    os.system('clear||cls')
    print("You choose to go through the jungle")
    time.sleep(2)
    print("You have been walking for a while now")
    time.sleep(2)
    print("you begin to feel a little bit hungry")
    time.sleep(2)
    if(f1.foodChoice == "3"):
      print("maybe eating protein powder for breakfast wasn't the best idea")
      time.sleep(2)
      print("you have died of starvation")
      exit(0)
    else:
      print("You decide to look for food with whatever energy you have left")
      time.sleep(4)
      os.system('clear||cls')
      print("There is a hamburger in the middle of the path, a banana tree to your right, and a berry bush to your left")
      self.JungleFood = input("What would you like to eat? 1. Hamburger, 2. Banana, 3. Berry")
      if self.JungleFood == "1":
        os.system('clear||cls')
        print("you REALLY wanted that hamburger, didn't you?")
        time.sleep(3)
        print("nonetheless, it was tasty, and nothing bad happened.")
        print("you continue walking through the jungle")
        time.sleep(3)
        os.system('clear||cls')
        print("you see a strange handle sticking out of a bush")
        print("1. grab the handle or 2. don't")
        wheelChoice = input("Do you want to go grab the handle?")
        if(wheelChoice == "1"):
          os.system('clear||cls')
          print("you decided to grab it?")
          time.sleep(2)
          print("you pull on the handle")
          time.sleep(2)
          print("you pull a wheelchair out of the bush")
          time.sleep(2)
          print("you see a person in the wheelchair")
          time.sleep(2)
          print("you feel unfathomable fear")
          time.sleep(3)
          os.system('clear||cls')
          print("you can do one of four things")
          time.sleep(2)
          print("1. shoot a flare into the sky and hope for help,\n 2. shoot the flare at the person in the wheelchair,\n 3. push the person out of their wheelchair and steal it,\n 4. walk away")
          action = input("What do you do?")
          if action == "1":
            os.system('clear||cls')
            print("you shoot a flare into the sky")
            print("a helicopter sees the flare and comes to your rescue")
            print("you are saved")
            print("The helicopter takes you back home, and all hopes of you saving solomander are lost.")
            exit(0)
          elif action == "2":
            os.system('clear||cls')
            print("you shoot the flare at the person in the wheelchair")
            time.sleep(3)
            print("you watch in pure horror as the wheelchair slowly transforms into what can only be described as an off brand optimus prime")
            time.sleep(3)
            print("bad idea")
            b1.WheelChair()
            b1.BossFight()
            print("congratulations, you managed to defeat the boss")
            c1.Cave()
          elif action == "3":
            os.system('clear||cls')
            print("you meanie")
            print("you pushed the person out of their wheelchair")
            print("you stole the wheelchair")
            print("While walking, you see a cave")
            print("You enter the cave")
            c1.Cave()
            self.OwnWheelChair = True
          elif action == "4":
            os.system('clear||cls')
            print("You leave the person alone")
            time.sleep(2)
            print("you continue walking through the jungle")
            print("After a few more minutes of walking, you stumble upon a cave.")
            c1.Cave()
      elif self.JungleFood == "2":
        os.system('clear||cls')
        print("you went right to the banana tree")
        time.sleep(2)
        print("you climbed up the tree and picked a banana")
        monkeyKidnap = random.randint(1,3)
        if monkeyKidnap == 1:
          print("a band of rougue chimpanzees kidnapped you")
          print("you were brainwashed and became a chimpanzee")
          exit(0)
        else:
          os.system('clear||cls')
          print("you ate the banana")
          time.sleep(2)
          print("that banana was really good, its good you didn't get kidnapped by a band of rogue chimpanzees or something like that")
      elif self.JungleFood == "3":
        os.system('clear||cls')
        print("You went left to the berry bush")
        instantPoison = random.randint(1,5)
        if instantPoison == 1:
          os.system('clear||cls')
          print("You ate a poisoned berry")
          print("you died")
          exit(0)
        else:
          os.system('clear||cls')
          print("you ate the berries")
          time.sleep(2)
          print("you feel a little bit better now")
          time.sleep(2)
          
        