class Clothing:

  def __init__(self):
    self.clothing = ""
    
  def choices(self):
      print(" what would you like to wear today? ")
      print("1. T-shirt and Shorts")
      print("2. Sweater and Jeans")
      print("3. Heavy winter coat and winter pants")

      clothing = input("Enter the number of your choice: ")
      if clothing == "1":
        clothingType = "T-shirt and shorts"
        self.clothing == "1"
      elif clothing == "2":
        clothingType = "Sweater and Jeans"
        self.clothing == "2"
      elif clothing == "3":
        clothingType = "Heavy winter coat and winter pants"
        self.clothing == "3"
      else:
          print("You froze because you were to special to   pick something from your wardrobe")
          exit(0)
  
      print("You chose " , clothingType)


  def leaveHouse(self):
    if self.clothing == "1":
        print("it begins raining heavily outside and you freeze because you wore too few layers")
        exit(0)
    elif self.clothing == "2":
        print("you go to your car")
    elif self.clothing == "3":
        print("You wore too many layers and were turned into a fine paste")
        exit(0)