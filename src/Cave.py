##Grayson Carter
import time
from BossFight import BossFight
from FinalArea import FinalArea
import os

bf1 = BossFight()
fa = FinalArea()

class Cave:

  def __init__(self):
    self.sword = False
    self.magic = False

  def Cave(self):
    print("You stumble upon a cave in the middle of the jungle")
    time.sleep(2)
    print("1. Enter the cave, 2. Ignore the cave")
    time.sleep(2)
    caveChoice = input("What do you do?")
    if caveChoice == "1":
      self.EnterCave()
    elif caveChoice == "2":
      self.NoCave()

  def EnterCave(self):
    os.system('clear||cls')
    print("You enter the cave")
    time.sleep(2)
    print("there is a sword resting on the side of the cave")
    time.sleep(2)
    print("1. Pick up the sword, 2. Ignore the sword")
    time.sleep(2)
    swordchoice = input("do you want to pick up the sword?")
    time.sleep(2)
    if(swordchoice == "1"):
      os.system('clear||cls')
      print('the entrance to the cave collapsed as soon as you picked up the sword')
      time.sleep(2)
      print("Now you have a pretty cool sword though")
      time.sleep(2)
      self.sword = True
      bf1.playerdamage = 30
      time.sleep(4)
      os.system('clear||cls')
      time.sleep(2)
      print("now you do a little bit more damage to bosses")
      time.sleep(2)
      print("you continue on your journey through the cave")
      time.sleep(2)
      print("you feel a slight breeze")
      time.sleep(2)
      print("that might mean that there is another exit")
      time.sleep(2)
      print("With no other chocie, you decide to continue moving through the cave.")
      time.sleep(4)
      os.system('clear||cls')
      print("You eventually see a little bit of light coming from somewhere deeper in the cave")
      time.sleep(2)
      print("You move cautiously towards the light")
      time.sleep(2)
      print("You find the source of the light")
      time.sleep(2)
      print("Although it isn't the exit of the cave, you did manage to find a campfire")
      time.sleep(2)
      print("i wonder how it got lit")
      time.sleep(2)
      print("you decide to rest for a while")
      time.sleep(5)
      os.system('clear||cls')
      print("You decide to be productive with your time")
      time.sleep(2)
      print("You stand up to finally leave the cave, but realize that there is a strange man on the other side of the campfire")
      time.sleep(2)
      print("you don't know what to do about this")
      time.sleep(2)
      print("you can either 1. Be scared, 2. be friendly, or 3. be a coward")
      time.sleep(2)
      oldman = input("what do you do?")
      if oldman == "1":
        os.system('clear||cls')
        print("you decide to be scared")
        time.sleep(2)
        print("the old man realized you are scared")
        time.sleep(2)
        print("he runs away out of fear of whatever you are afraid of")
        time.sleep(2)
        print("i don't think you can get out without his help")
        time.sleep(2)
        print("the roof of the cave collapses on you")
        time.sleep(2)
        exit(0)
      elif oldman == "2":
        os.system('clear||cls')
        time.sleep(2)
        print("you decide to be friendly")
        time.sleep(2)
        print("you introduce yourself to the old man")
        time.sleep(2)
        print("he introduces himself")
        time.sleep(2)
        print("he says his name is Slick Willie")
        time.sleep(2)
        print("he says he is a wizard")
        time.sleep(2)
        print("you tell him about your current situation")
        time.sleep(2)
        print("he offers to help you find solomander")
        time.sleep(2)
        print("you can either accept his help right now, or have him train you to learn magic")
        time.sleep(2)
        print("1. Accept his help, 2. Have him train you")
        time.sleep(2)
        oldhelpchoice = input("what do you do?")
        if oldhelpchoice == "1":
          os.system('clear||cls')
          print("The old man says he will help you find solomander")
          time.sleep(2)
          print("The old man gives you a map of the island")
          print("You know exactly where to go to get to the capital now")
          fa.Beginning()
        if(oldhelpchoice =="2"):
          os.system('clear||cls')
          print("The old man trains you in his ways")
          print("After 2 weeks of rigourus training, you have finally mastered magic")
          bf1.magicuser = True
          bf1.mana = 100
          print('The old man has decided that you need to beat him in order to leave.')
          bf1.OldMan()
          bf1.BossFight()
          os.system('clear||cls')
          print("congratulations, you have proven yourself a worthy magic user")
          print("You are now ready to face the evil wizard and save solomander")
          fa.Beginning()
      elif oldman == "3":
        os.system('clear||cls')
        print("you decide to be a coward")
        print("You turn tail and run away")
        print("you hear the old man shout something")
        print("you explode")
        print("the old man was a wizard and doesn't like cowards")
        exit(0)
      
    elif(swordchoice == "2"):
      os.system('clear||cls')
      print("you ignore the sword")
      print("you continue walking through the cave")
      print("You get lost")
      print("uh oh")
      print("you suddenly become deathly afraid of the dark")
      print("you died of fear")
      exit(0)
  
  def NoCave(self):
    os.system('clear||cls')
    print("You ignore the cave")
    print("You continue walking through the jungle")
    print("after a few more minutes of walking you get lost")
    print("uh oh")
    print("you hear monkey noises coming from the trees")
    choice = input("do you: 1. investigate or 2. don't")
    if choice == 1:
      os.system('clear||cls')
      print("you decide to check out the monkey noises")
      print("the monkeys are pretty cool")
      print("you decide to hang out with the monkeys")
      print("after a while you decide to join the monkeys tribe")
      print("oo oo aa aa")
      exit(0)
    else:
      os.system('clear||cls')
      print("you decide to walk in the other direction")
      print("as you get farther and farther away from the monkeys, their monkeying gets louder")
      print("the monkeys eventually catch up to you")
      BossFight.Monkeys()
      bf1.BossFight()
      print("you beat the monkeys")
      print("the cave seems like a pretty good idea right now")
      self.EnterCave()
      
  