a = [] # empty list
print(type(a))

a = [53, 23, 7, 21]
print(a)
print(len(a)) # 4
r = a + [1, 4, 5] # concatenation. returns a new list
print(r)
print(len(r))
print(a) # notice a was not changed.

t = a * 3 # repetition
print(t)
print(len(t))
print(a) # a was not changed

# r = [1, 2, 3] + "45" # gives TypeError. you cant concatenate a list object and a str object


