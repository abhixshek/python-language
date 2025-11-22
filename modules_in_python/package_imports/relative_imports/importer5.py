from dir3.dir4.string_transformer import string # picks string module from the std library when there is no string.py
# in the HOME directory of importer5.py
# and when there is a string.py here, it picks the one here, not the string.py which is present in the same directory
# as string_transformer.py, i.e., in dir3/dir4/
# the only way to make it pick that one, is to use relative imports syntax. see importer6.py
print(dir(string))

import sys
print(sys.path)

# from string import my_upper

# print(my_upper('school'))

