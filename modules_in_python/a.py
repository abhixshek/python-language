# a top-level file. imports tools defined in other modules and uses them to perform tasks.

import b # gives this file a.py access to everything defined by top-level code in the file b.py
# it roughly means, "load the file b.py(unless it's already loaded) and give me
# access to all its attributes through the name `b`"

b.spam('Executing from a.py') # "fetch the value of the name `spam` that lives within the object b"
# object.attribute notation is used to access function objects(callable) as well as data values that define an object's properties like person's age.

import os
print(os.getcwd()) # cwd is the directory from where you launch/run this python file a.py
# it maybe the directory where a.py resides or it may be some other directory as well.
# i.e. your cwd can be anything on the system and you can launch this program from there.
# os.getcwd() will give the directory path from where you launched this file.

import sys
print() # blank line
print(sys.path) # list of search paths configured for this program run. this is really the list that python searches
# from left to right when importing a module file


