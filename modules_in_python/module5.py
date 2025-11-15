import module1

print(module1.r) # spam
module1.r = 100
print(module1.r) # 100

import module1 # does not reload/rerun the module1 but instead fetches from a table of already loaded modules
print(module1.r) # prints 100. had it been reloaded, it would have printed spam again.

from module1 import r
print(r) # 100. meaning the above from statement did not reload module1


