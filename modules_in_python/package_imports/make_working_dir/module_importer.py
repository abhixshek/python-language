import sys
import os

print(sys.path)

import dir1.dir2.mod

print("__name__ attribute of module mod.py when imported here -->", dir1.dir2.mod.__name__)

print("my current working directory from where I ran this program:", os.getcwd())

print('program completed')

