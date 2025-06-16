import tkinter as tk


root = tk.Tk() # creates the window

root.title("Simple App")

lbl = tk.Label(root, text="Label 1")
lbl.grid(row=0, column=0)

btn = tk.Button(root, text="Button 1") # adds a button to our window "root"
btn.grid(row=0, column=1) # shows it on the window

root.mainloop() # keeps the window open and listens for events

