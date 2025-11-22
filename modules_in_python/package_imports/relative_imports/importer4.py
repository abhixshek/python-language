import string # picks string module in the same directory as this module(this module's HOME directory always comes first in sys.path)

print(dir(string))

import sys
print(sys.path)

from string import my_upper

print(my_upper('school'))

