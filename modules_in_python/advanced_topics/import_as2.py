import mod as m


print(m)

import sys
print(sys.modules.keys()) # in the modules system table, it is having key still as mod, not m
print('mod' in sys.modules.keys()) # True

m.func()

# del sys.modules['mod'] # not deleting the module this time. let us if running import again loads the module again or not.
m.func()

print(sys.modules.keys())
print(m)

m.func = 'spam'
print(m.func)

# let us see if now after deleting the module from sys.modules table, does import lead to importing of the module again without requiring reload function or its still loaded.

import mod # it did not import the module again
print(sys.modules.keys()) # we can see mod again in the keys
print(m.func) # spam
print(mod.func) # spam, confirms that mod was not freshly imported again


from formats import money
print(money(-34.784, 10))
commas = 45
print(money(43632, 7)) # note how the function works despite you initializing a name commas in this module
# this is because it does not cause any conflict with the commas function in formats module. that module cannot see what you have defined here.
# and you dont need to import commas function here even though money() uses commas() inside it.

