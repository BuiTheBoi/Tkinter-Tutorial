from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)    # Textbox for user input
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    # When you click the button on the GUI, this program updates the string 'Hello' followed by the user input
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello) 
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()


root.mainloop()