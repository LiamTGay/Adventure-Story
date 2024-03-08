import tkinter as tk


class Buttons:

  def __init__(self):
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0
    self.text = ""
    self.onepress = False
    self.twopress = False
    self.threepress = False
    self.fourpress = False

  def ButtonOneClick(self):
    self.onepress = True
    print("Button One Clicked")
    self.onepress = False

  def ButtonTwoClick(self):
    self.twopress = True
    print("Button Two Clicked")
    self.twopress = False

  def ButtonThreeClick(self):
    self.threepress = True
    print("Button Three Clicked")
    self.twopress = False

  def ButtonFourClick(self):
    self.fourpress = True
    print("Buttton Four Clicked")
    self.fourpress = False

  def TwoButton(self):
    self.width = 10
    self.height = 5
    self.text = "Buttons"
    window = tk.Tk()
    window.geometry("300x300")

    label = tk.Label(window, text = 'text Goes here')
    label.pack()

    button = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonOneClick)

    buttonTwo = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonTwoClick)

    button.place(anchor='center',x=self.x + (300/4), y=self.y + (300 / 2))
    buttonTwo.place(anchor='center', x=self.x + ((300/4) * 3), y=self.y + (300 / 2))

    tk.mainloop()

  def ThreeButton(self):
    self.width = 5
    self.height = 5
    self.text = "Buttons"
    window = tk.Tk()
    window.geometry("300x300")

    label = tk.Label(window, text = 'text Goes here')
    label.pack()

    button = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonOneClick)

    buttonTwo = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonTwoClick)

    buttonThree = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonThreeClick)

    button.place(anchor='center', x=self.x + (300/4), y=self.y + (300 / 2))
    buttonTwo.place(anchor='center', x=self.x + ((300/4) * 2), y=self.y + (300 / 2))
    buttonThree.place(anchor='center', x=self.x + ((300/4) * 3), y=self.y + (300 / 2))

    tk.mainloop()

  def FourButton(self):
    self.width = 5
    self.height = 5
    self.text = "Buttons"
    window = tk.Tk()
    window.geometry("300x300")

    label = tk.Label(window, text = 'text Goes here')
    label.pack()

    button = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonOneClick)

    buttonTwo = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonTwoClick)

    buttonThree = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonThreeClick)

    buttonFour = tk.Button(text=self.text, height=self.height, width=self.width, command = self.ButtonFourClick)

    button.place(anchor='center', x=self.x + (300/8), y=self.y + (300 / 2))
    buttonTwo.place(anchor='center', x=self.x + ((300/8) * 3), y=self.y + (300 / 2))
    buttonThree.place(anchor='center', x=self.x + ((300/8) * 5), y=self.y + (300 / 2))
    buttonFour.place(anchor='center', x=self.x + ((300/8) * 7), y=self.y + (300 / 2))

    tk.mainloop()
