X = 88 # global to this file only

def f():
    global X # change this file's X
    X = 99  # cannot see names in other modules

