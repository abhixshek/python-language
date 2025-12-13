from data_module import age

print(age) # 
age = 100

print(age) # 100
from data_module import age
print(age) # even though the above import statement does not reload the module because its already loaded, however it still performs the name copying operation.
# in this case, by assigning the object pointed to by age in data_module to the age in this module
# printed 44


