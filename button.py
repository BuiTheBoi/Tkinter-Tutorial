from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick)
myButton.pack()
myButton.grid()


root.mainloop()