from module1 import r
print(r) # spam

r = 'world'
print(r) # world

import module1
print(module1.r) # spam. BUT, NOTE that the above import did not reload the module1 again. 
# what has happened is, the first from statement at the top, ran the module1 and copied the name r from it into the current module and assigned the same name r.
# so r in this module references the r in the module1. but, r = 'world', reassigns r to point to the object 'world' now.
# but this does not change what r in the module1 points to. it still points to/references the object 'spam'

# in other words, these are the same assignment rules we had studied before.
# in the next file, you will find more details when we deal with mutable objects as well.

