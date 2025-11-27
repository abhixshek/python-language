import moda


print(moda.name) # kelly, this is called qualifying an object
print(moda.__dict__) # every attribute of moda exists as a string name in the keys of this dictionary.
print()
print(moda.__dict__['name']) # kelly, this is indexing namespace dictionary manually

import sys
print(sys.modules['moda'].name) # kelly, index loaded-modules table manually

print(getattr(moda, 'name')) # kelly, call built-in fetch function

a = 45
b = 'spam'

# you can even access the current(this) module through sys.modules and change variables here indirectly
print(sys.modules[__name__].a)
sys.modules[__name__].b = 89
print(a, b) # 45, 89

