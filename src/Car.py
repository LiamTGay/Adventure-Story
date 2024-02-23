class Car:

  def GoToCar(self):
    print("You begin walking to your car")
    print("You currently own a 2001 Honda Civic")
    print("You can stay in your crappy car or try your luck to obtain your neighbors super cool car(its a Porche 911)")
    steal = input("1. Stay in your car or 2. Steal the car")
    if steal == "1":
      print("you chose to stay in your car")
    elif steal == "2":
      print("you chose to steal the car")
      print("uh oh, the door is locked")
      print("do you still want the car?")
      sure = input("1. yes or 2. no")
      if sure == "1":
        print("you tried again")
        print("the car alarm started blaring")
        print("your neightbor is currently running outside to see what is happening")
        print("FIGHT OR FLIGHT")
        fight = input("1. fight or 2. flight")
        if fight == "1":
          print("your neighbor is much stronger than you are")
          print("you lost the fight")
          exit(0)
        if fight == "2":
          print("You ran to your car")
          print("you escaped")
      if sure == "2":
        print("you returned to your car")
      