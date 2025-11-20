import sys
import os

print(sys.path)

import dir1.dir2.mod

print("__name__ attribute of module mod.py when imported here -->", dir1.dir2.mod.__name__)

print("my current working directory from where I ran this program:", os.getcwd())

import dir1.dir2.mod # does not re-import because its already imported

# Once imported, the path in your import statement becomes a nested object path in your script.
print(dir1) # this is a module object, pointing to __init__.py file of dir1
print(dir1.dir2) # similarly, this points to __init__.py file of dir2
print(dir1.dir2.mod)

from imp import reload

reload(dir1)
reload(dir1.dir2)

print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)

# import statements can be somewhat inconvenient to use with packages, because you may have to retype the paths frequently in your program.
# for example, to access mod object you have to always type dir1.dir2.mod. Typing dir2.mod or just mod will throw a NameError
# in such cases therefore, using `from` is preferable to `import`

print("using from statement for package imports")
from dir1.dir2 import mod
print(mod.z)

# another shorter way if you are using import is to use alias
print("using import as (alias)")
import dir1.dir2.mod as m
print(m.z)

print('program completed')

