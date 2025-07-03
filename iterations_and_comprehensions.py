# we say in looping_constructs.py that for loops can be used on any sequence type - lists, tuples and strings
for x in 'spam': print(x * 2, end= ' ')

print()
# actually the for loop turns out to be even more generic - it works on any *iterable object*

f = open('file_objects_io/file1.txt')
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line)
line = f.readline()
print(len(line), line) # length 0, empty string
line = f.readline()
print(len(line), line) # length 0, empty string

# instead of f.readline() we could use next() as file object is an iterable
f = open('file_objects_io/file1.txt')
while True:
    try:
        print(f.__next__())
    except StopIteration as e:
        print('StopIteration Error at end of file')
        break
print() # blank line for clarity of output

# infact you dont need to code all of this as python's for loop handles this for us and catches the StopIteration
print('Reading a file line by line - ideal way')
for line in open('file_objects_io/file1.txt'):
    print(line.upper())

# iter and next()

