from module1 import r, age


print(r) # spam
print(age) # [25, 36, 44]. # that is, age is pointing to a mutable object, list.

r = 'hello'
age[0] = 99
print(age)
print(r) # hello

import module1
print(module1.r) # module1.r still points to the same object - spam
print(module1.age) # module1.age points to the same object which age in our current module points to. and therefore its changed


