try:
    a = 100
    print(a) # if the above line is commented out, this line will throw a NameError as a is not defined in that case.
except NameError:
    print('name was not defined')

print('completed')

