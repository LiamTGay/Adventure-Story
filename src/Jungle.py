from Food import Food
import time
import random

f1 = Food()

class Jungle:

  def __init__(self):
    self.JungleFood = ""

  def GoToJungle(self):
    print("You choose to go through the jungle")
    #time.sleep(2)
    print("You have been walking for a while now")
    #time.sleep(2)
    print("you begin to feel a little bit hungry")
    #time.sleep(2)
    if(f1.foodChoice == "3"):
      print("maybe eating protein powder for breakfast wasn't the best idea")
      #time.sleep(2)
      print("you have died of starvation")
      exit(0)
    else:
      print("You decide to look for food with whatever energy you have left")
      #time.sleep(2)
      print("There is a hamburger in the middle of the path, a banana tree to your right, and a berry bush to your left")
      self.JungleFood = input("What would you like to eat? 1. Hamburger, 2. Banana, 3. Berry")
      if self.JungleFood == "1":
        print("you REALLY wanted that hamburger, didn't you?")
        #time.sleep(3)
        print("nonetheless, it was tasty, and nothing bad happened.")
      elif self.JungleFood == "2":
        print("you went right to the banana tree")
        #time.sleep(2)
        print("you climbed up the tree and picked a banana")
        monkeyKidnap = random.randint(1,3)
        if monkeyKidnap == 1:
          print("a band of rougue chimpanzees kidnapped you")
          print("you were brainwashed and became a chimpanzee")
          exit(0)
        else:
          print("you ate the banana")
          #time.sleep(2)
          print("that banana was really good, its good you didn't get kidnapped by a band of rogue chimpanzees or something like that")
      elif self.JungleFood == "3":
        print("You went left to the berry bush")
        instantPoison = random.randint(1,5)
        if instantPoison == 1:
          print("You ate a poisoned berry")
          print("you died")
          exit(0)
        else:
          print("you ate the berries")
          #time.sleep(2)
          print("you feel a little bit better now")
          #time.sleep(2)
          print("you continue walking through the jungle")
          #time.sleep(2)
          print("you see a strangle handle sticking out of a bush")
          print("1. grab the handle or 2. don't")
          wheelChoice = input("Do you want to go grab the handle?")
          if(wheelChoice == "1"):
            print("you decided to grab it?")
            #time.sleep(2)
            print("you pull on the handle")
            #time.sleep(2)
            print("you pull a wheelchair out of the bush")
            #time.sleep(2)
            print("you see a person in the wheelchair")
            #time.sleep(2)
            print("you feel unfathomable fear")
            #time.sleep(2)
            print("you can do one of four things")
            #time.sleep(2)
            print("1. shoot a flare into the sky and hope for help, 2. shoot the flare at the person in the wheelchair, 3. push the person out of their wheelchair and steal it, or 4. walk away")
            action = input("What do you do?")
            if action == "1":
              print("you shoot a flare into the sky")
              print("a helicopter sees the flare and comes to your rescue")
              print("you are saved")
              print("")
          
        