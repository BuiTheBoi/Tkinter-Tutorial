from tkinter import *


root = Tk()

# Creating a Label Widget 
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Justin Bui").grid(row=1, column=5)
myLabel3 = Label(root, text="            ").grid(row=1, column=1)


# # Shoving it onto the screen
# myLabel.pack()


root.mainloop()