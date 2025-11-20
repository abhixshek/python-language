import dir3.dir4.calculator
# note that in this case dir3 and dir4 both do not contain any __init__.py file

print(dir3.dir4.calculator)

print(dir3)
print(dir(dir3)) # since there is no __init__.py file that you have placed in this directory. only attribute that dir3 has is dir4, accessed by dir3.dir4
print(dir3.__dict__.keys())
print(dir3.dir4)
print(dir3.dir4.__dict__.keys())

print("using from statement to get calculator module")
from dir3.dir4 import calculator
print(calculator.add(4, 5))

print('Program completed.')
