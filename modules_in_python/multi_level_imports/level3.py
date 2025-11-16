import level2 # runs `import level1` as part of its code

r = 'ai'

print(level2.level1.age)
print(level2.level1.r) # spam
level2.level1.r = 'school'
print(level2.level1.r)

import sys
print('level1' in sys.modules.keys()) # True, meaning level1 already exists in the loaded modules table in this program even though we have not run `import level1` here
# NOTE that while level1 is known to the modules table, the name level1 does not exist in the current module's(this file) scope
# so running print(level1.r) will give NameError

import level1 # does not reload level1
print(level1.r) # school

m = sys.modules['level1']
print(m)
print(type(m))
print(m.r) # school
print(m.age)

# this module, level3 has access to its own global scope, level2's global scope and also level1's global scope(through level2) because level2 imports level1 in its code.

print(r) # ai
print(level2.r) # ml
print(level2.level1.r) # school

# NOTE, the reverse however is not true, i.e., level1 cannot see names in level2 and level2 cannot see names in level3. dont be confused, just look at a module file's code and see the objects involved.

# also note while importing, you can say import level2 then do level2.level1.X to access attributes of level1
# BUT YOU CANNOT do `import level2.level1`. this is a syntax for package(directory) imports.
# import level2.level1 # throws ModuleNotFoundError: No module named 'level2.level1'; 'level2' is not a package



