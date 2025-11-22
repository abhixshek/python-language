import dir3.dir4.calculator2


print(dir3.dir4.calculator2) # its picking the calculator module in the sub-directory of relative_imports, i.e. from this module's directory inside.
# there is a similar module path from package_imports/ directory which has been added to PYTHONPATH env variable.
# this shows that home directory of this module is coming first in the sys.path module search path. 
import sys
print(sys.path)

print('program complete')
