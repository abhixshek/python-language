a = () # empty tuple
print(a)
print(type(a))
print(len(a))

a = (4, ) # 1 item tuple
print(a)
print(len(a))

a = (1, 2)
b = (5, 6)
result = a + b # concatenation
print(result)
print(a)
print(b)

r = a * 4 # repetition
print(r)
print(len(r))

a = (6, 7, 9, 2, 4, 2, 4, 3, 1)
print(a)
print(a[2]) # indexing
print(a[2:5]) # slicing
