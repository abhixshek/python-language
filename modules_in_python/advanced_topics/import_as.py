import mod as m


print(m)

import sys
print(sys.modules.keys()) # in the modules system table, it is having key still as mod, not m
print('mod' in sys.modules.keys()) # True

m.func()

del sys.modules['mod']
m.func()

print(sys.modules.keys())
print(m)

m.func = 'spam'
print(m.func)

# let us see if now after deleting the module from sys.modules table, does import lead to importing of the module again without requiring reload function or its still loaded.

import mod # it imported the module again
print(sys.modules.keys()) # we can see mod again in the keys
print(m.func) # spam. which means that the new import has not been made in-place. its a new module imported all together because we had deleted it from the sys.modules table
print(mod.func) # func function
mod.func()


