import tkinter as tk


def add_to_list(event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text) # add it to the list
        entry.delete(0, tk.END) # to clear the contents typed by the user in the box


root = tk.Tk() # creates the window
root.title("Simple App")


root.columnconfigure(0, weight=1) # so that our window resizes well
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)


# a frame is a container for our widgets to better organize them.
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5) # frame isnt something visible on the window. its just a container.

frame.columnconfigure(0, weight=1) # we only configure column 0 because our button is in column 1 and we dont want it to be stretched on resizing the window
frame.rowconfigure(1, weight=1)

entry = tk.Entry(frame) # entry is a text input field.
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list) # we bind the return key to this entry field. now everytime return is pressed this actually returns an event object.
# so if our function add_to_list does not take any input arguments, it will raise an error because an event object is being passed to that function.
# this is why we added an event parameter to our function definition with default value of None and now it works. 
# the alternative is to use lambda functions:
# entry.bind("<Return>", lambda event: add_to_list())

btn = tk.Button(frame, text="Add", command=add_to_list)
btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew") # ew stands for east west. 

frame_2 = tk.Frame(root)
frame_2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5) # frame isnt something visible on the window. its just a container.

frame_2.columnconfigure(0, weight=1) # we only configure column 0 because our button is in column 1 and we dont want it to be stretched on resizing the window
frame_2.rowconfigure(1, weight=1)

entry = tk.Entry(frame_2) # entry is a text input field.
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list) # we bind the return key to this entry field. now everytime return is pressed this actually returns an event object.
# so if our function add_to_list does not take any input arguments, it will raise an error because an event object is being passed to that function.
# this is why we added an event parameter to our function definition with default value of None and now it works.
# the alternative is to use lambda functions:
# entry.bind("<Return>", lambda event: add_to_list())

btn = tk.Button(frame_2, text="Add", command=add_to_list)
btn.grid(row=0, column=1)

text_list = tk.Listbox(frame_2)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew") # ew stands for east west.



root.mainloop() # keeps the window open and listens for events

