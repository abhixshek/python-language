import tkinter as tk


def on_click():
    print("Button was clicked.")
    lbl.config(text="Button clicked. Message on the window")

root = tk.Tk() # creates the window

root.title("Simple App")

lbl = tk.Label(root, text="Label 1")
lbl.grid(row=0, column=0)

btn = tk.Button(root, text="Button 1", command=on_click) # adds a button to our window "root"
btn.grid(row=0, column=1) # shows it on the window

root.mainloop() # keeps the window open and listens for events

