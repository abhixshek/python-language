f1 = open('file1.txt', 'r') # 'r' is read mode and is the default in fact.
lines = f1.readlines()
print(lines)
# ['This is a txt file.\n',
# 'It contains special characters like !)$^#&!${}:"\'>?<\\\n', '5 / 4\n',
# 'Notice it even contains a backslash that is escaped (using double backslash) when read in python as a string\n',
# 'I am keeping one blank line at the end of the file\n']

# NOTICE that every line read contains a \n ending
# NOTE that the last blank line in the original txt file did not come as an item in the above list.
# in fact, even the vi editor does not show that blank line.
# backslash in the original text is escaped using double backslash and is 1 byte, recall from strings chapter
# every escape sequence is 1 byte and each character is also 1 byte.

f2 = open('file2.txt') # file2.txt is nearly same as file1.txt except that it ends with 2 blank lines in the original file
lines = f2.readlines()
print(lines)
# ['This is a txt file.\n',
# 'It contains special characters like !)$^#&!${}:"\'>?<\\\n', '5 / 4\n',
# 'Notice it even contains a backslash that is escaped (using double backslash) when read in python as a string\n',
# 'I am keeping one blank line at the end of the file\n',
# '\n']

# NOTICE that file2.txt contained 2 blank lines at the end in the original text file and this time we have got the
# 2nd last line as a '\n' element in the above list

f3 = open('file3.txt', 'w')
f3.write('Hello, this is a line from a string written in \tpython.\n2 + 2 = 4\n')
# if you store this line in a variable/print it, it will give 65
# 65 is the number of bytes written to the file. if you do len() on the above string that is also 65
f3.write('another line in the file.\n')
f3.write('\n')
f3.close() # flush the output buffers to disk
# until the file is closed, you will not find the file in your directory or its already created you wont find any
# content inside it. So closing the file after writing to it is important.

# reading lines one at a time
print('Reading a file line by line')
f4 = open('file3.txt')
l = f4.readline()
print(l) # recall in print(), end="\n" is the default. therefore there is 1 \n due to the text having it and 2nd
# due to end="\n" parameter of print()
print(len(l))
l = f4.readline()
print(l)
print(len(l))
l = f4.readline()
print(l)
print(len(l))
l = f4.readline()
print(l)
print(len(l)) # 1, because '\n' is of length 1
l = f4.readline()
print(l)
print(len(l)) # 0 because it is an empty string ''
l = f4.readline()
print(l)
print(len(l)) # 0 because it is an empty string ''

# NOTE that empty string is your cue to know that we have reached the end of file because blank lines are not empty
# they contain \n and therefore have length = 1.

# reading line by line is best done through file iterators
print('Reading using file iterator')
for line in open('file3.txt'):
    print(line, end= '')
print('End of iterator')

# Writing python objects (goes as strings) to a text file
X, Y, Z = 99, 56, 25
S = 'Jason\'s flat is in Bengaluru.'
D = {'a': 23, 'b': 44}
L = [77, 34, 67]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

chars = open('datafile.txt', 'r').read()
print(chars)
# all the text was read back as a string too.
# how do we recreate python objects by reading from a file?
F = open('datafile.txt', 'r')
line = F.readline()
line = line.rstrip() # gets rid of the \n at the end of the line. line[:-1] would have also worked but in case where
# the line is not ending with a \n, it would cause you to remove valuable information
print(line)
line = F.readline()
print(line) # this is a line of numbers(int) separated by comma
parts = line.split(',')
numbers = [int(num) for num in parts]
print(numbers) # NOTICE we didnt have to remove the \n for the last number in parts because int() quietly ignores
# whitespace around numbers
print(type(numbers[1])) # int

# finally we need to convert the list and dictionary on the final line
# we can use eval() for this
line = F.readline()
parts = line.split('$') # split(parse) on $
objects = [eval(P) for P in parts]
print(objects)
print(type(objects[0])) # list
print(type(objects[1])) # dict

# storing python objects with pickle
D = {'a': 45, 'b': 33}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)
F.close()

# reading the data back
F = open('datafile.pkl', 'rb')
print(F.read()) # you cannot decode the binary data directly but pickle can
F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E)
print(type(E)) # dict

# file context managers
with open('file3.txt') as text_file:
    print(text_file.readline())
# text_file gets automatically closed outside the content manager
# running print(text_file.readline()) outside the context manager will lead to ValueError as `text_file`
# has already been closed
