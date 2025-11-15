import module1


print(module1.r) # spam
module1.r = 42 # changes the object module1.r points to. # such cross-file changes are discouraged and bad design choice.
# NOTE that this is different from what we did in module7 where the >>>age[0] = 99 meant that list object itself was changed, not the name.

print(module1.r) # 42

from module1 import r
print(r) # 42

