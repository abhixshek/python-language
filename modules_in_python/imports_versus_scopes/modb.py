X = 11 # global to this file only

import moda # gain access to names in moda

moda.f() # sets moda.X, not this file's X
print(X, moda.X) # 11, 99

