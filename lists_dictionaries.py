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

a = [5,7,3,87,1,8,5]
print(a)
# iteration
for i in a:
    print(i, end=" ")

print()
print(3 in a) # membership

r = [i * 2 for i in a] # list comprehension
print(r)

a = list(range(-4, 4))
print(a)
r = list(map(abs, a)) # map generator function applies the specified function to each item in the iterable
print(r)

print(a[0]) # indexing
print(a[-2])
print(a[2:4]) # slicing, includes index 2 and 3, not 4

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ] # nested list, acts like a 2D array
print(matrix)
print(matrix[1])
print(matrix[1][1])

