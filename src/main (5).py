from Car import Car
from CarDrive import CarDrive
from Clothing import Clothing
from Food import Food
from Island import Island
from Forest import Forest
from Jungle import Jungle
from storyend import storyend
import time
import os

c1 = Clothing()
f1 = Food()
cr1 = Car()
cd1 = CarDrive()
i1 = Island()
fr1 = Forest()
j1 = Jungle()
e1 = storyend()

print("Hello, Welcome to the solamander affair")
time.sleep(1.5)
print("Your dear friend solomander has gone missing")
time.sleep(1.5)
print("You need to find him...")
time.sleep(1.5)
print("You have recieved a letter, that letter states:")
time.sleep(1.5)
print(" ")
print("'I have taken your dear friend, he is at my island. WAHHAHAHAH'")
time.sleep(2)
StartInput = input("Are you ready to take on the challenge and find him? (Y/N)")
if StartInput == "Y" or "y":
  os.system('clear||cls')
  c1.choices()
  f1.FoodChoice()
  f1.LeaveHouse()
  c1.leaveHouse()
  cr1.GoToCar()
  cd1.Drive()
  i1.Arrive()
  fr1.GoToForest()
  j1.GoToJungle()
  e1.endscreen()
else:
  print("Fine Then, He DIES")
  exit(0)
  


    