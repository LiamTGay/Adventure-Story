##Grayson Carter
import time
from BossFight import BossFight

bf1 = BossFight()

class Cave:

  def __init__(self):
    self.sword = False
    self.magic = False

  def Cave(self):
    print("You stumble upon a cave in the middle of the jungle")
    print("1. Enter the cave, 2. Ignore the cave")
    caveChoice = input("What do you do?")
    if caveChoice == "1":
      self.EnterCave()
    elif caveChoice == "2":
      self.NoCave()

  def EnterCave(self):
    print("You enter the cave")
    print("there is a sword resting on the side of the cave")
    print("1. Pick up the sword, 2. Ignore the sword")
    swordchoice = input("do you want to pick up the sword?")
    if(swordchoice == "1"):
      print('the entrance to the cave collapsed as soon as you picked up the sword')
      print("Now you have a pretty cool sword though")
      self.sword = True
      bf1.playerdamage = 30
      print("now you do a little bit more damage to bosses")
      print("you continue on your journey through the cave")
      print("you feel a slight breeze")
      print("that might mean that there is another exit")
      print("With no other chocie, you decide to continue moving through the cave.")
      print("You eventually see a little bit of light coming from somewhere deeper in the cave")
      print("You move cautiously towards the light")
      print("You find the source of the light")
      time.sleep(2)
      print("Although it isn't the exit of the cave, you did manage to find a campfire")
      print("i wonder how it got lit")
      print("you decide to rest for a while")
      time.sleep(5)
      print("You decide to be productive with your time")
      print("You stand up to finally leave the cave, but realize that there is a strange man on the other side of the campfire")
      print("you don't know what to do about this")
      print("you can either 1. Be scared, 2. be friendly, or 3. be a coward")
      oldman = input("what do you do?")
      if oldman == "1":
        print("you decide to be scared")
        print("the old man realized you are scared")
        print("he runs away out of fear of whatever you are afraid of")
        print("i don't think you can get out without his help")
        print("the roof of the cave collapses on you")
        exit(0)
      elif oldman == "2":
        print("you decide to be friendly")
        print("you introduce yourself to the old man")
        print("he introduces himself")
        print("he says his name is Slick Willie")
        print("he says he is a wizard")
        print("you tell him about your current situation")
        print("he offers to help you find solomander")
        print("you can either accept his help right now, or have him train you to learn magic")
        print("1. Accept his help, 2. Have him train you")
        helpchoice = input("what do you do?")
        if(helpchoice =="1"):
          print("The old man trains you in his ways")
          print("After 2 weeks of rigourus training, you have finally mastered magic")
          self.magic = True
          print('The old man has decided that you need to beat him in order to leave.')
          bf1.OldMan()
        
      elif oldman == "3":
        print("you decide to be a coward")
        print("You turn tail and run away")
        print("you hear the old man shout something")
        print("you explode")
        print("the old man was a wizard and doesn't like cowards")
        exit(0)
      
    elif(swordchoice == "2"):
      print("you ignore the sword")
      print("you continue walking through the cave")
      print("You get lost")
      print("uh oh")
      print("you suddenly become deathly afraid of the dark")
      print("you died of fear")
      exit(0)
  
  def NoCave(self):
    print("You ignore the cave")
    print("You continue walking through the jungle")
    print("after a few more minutes of walking you get lost")
    print("uh oh")
    print("you hear monkey noises coming from the trees")
    choice = input("do you: 1. investigate or 2. don't")
    if choice == 1:
      print("you decide to check out the monkey noises")
      print("the monkeys are pretty cool")
      print("you decide to hang out with the monkeys")
      print("after a while you decide to join the monkeys tribe")
      print("oo oo aa aa")
      exit(0)
    else:
      print("you decide to walk in the other direction")
      print("as you get farther and farther away from the monkeys, their monkeying gets louder")
      print("the monkeys eventually catch up to you")
      BossFight.Monkeys()
      bf1.BossFight()
      print("you beat the monkeys")
      print("the cave seems like a pretty good idea right now")
      self.EnterCave()
      
  