print('before assert')
assert 5 == 5
print('after assert')

assert 4 < 2, 'no way'
print('completed') # this line is not printed as the above assert fails and execution never reaches this line.

