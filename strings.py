a = "spam" # using double quotes
print(a)
a = 'spam' # using single quotes. same thing. no difference 
print(a)
a = "city's" # single quote as part of string using double quotes on the outside.
print(a)
a = 'city"s' # duoble quote as part of string using single quotes on the outside.
print(a)
a = '''Hi my name is John.
This is a multiline string.'''
print(a)
a = """
Hi my name is John.
This is a multiline string."""
print(a) # notice in the 2nd case we started with an enter (\n) and therefore in the output you can see a blank line between last print and this print
a = "s\tp\na\0m"
print(a) # escape sequences
a = r'C:\users\native\docs\python' # raw string
print(a) # backslashes are not treated as special characters. and therefore no escape sequences.

a = 'this' 'is'           'good'
print(a) # string literals adjacent to each other are concatenated as if a + sign was there.
a = 'this' + 'is' + 'good'
print(a) # same as above
a = ('Meaning'
        ' of'
        ' life'
        )
print(a) # spanned across multiple lines by enclosing in parenthesis. # prints 'Meaning of life'
# notice no \n are inserted even though it might appear like that. this is simple concatenation alllowed to be written on multiple lines due to using parenthesis.

a = 'first', 'last'
print(a) # a is a tuple. ('first', 'last')
# recall you dont need to give parenthesis for tuples necessarily.

a = 'city\'s'
print(a) # single quote inside single quotes by escaping quote using backslash
a = "city\"s"
print(a) # similarly for double quotes

# escape sequences
a = 'a\nb\tc'
print(len(a)) # this is a string of 5 bytes. 
# NOTE \n is a single character. it is represented by a single byte in memory.

b = '\a' # Bell
print(b) # gives a bell sound when you run this statement. and prints a blank line

c = 'this is a door\bR' # \b repesents backspace
print(c) # prints this is a dooR

d = 'C:\py\code' # if python does not recognize a valid escape sequence after \, it keeps the backslash literally
print(d) # prints 'C:\py\code'
print(len(d)) # 10


# raw strings - turns off escape sequences
file_path = r'C:\new\text.dat' # this will not lead to interpreting \n as newline and \t as tab in this string. 
# without the r outside the above string, the file_path would never be found in system because it would search for C:(newline)ew(tab)ext.dat
print(len(file_path)) # 15

# NOTE even raw strings CANNOT end with a backslash.

mantra = """Always look
 to the bright
side of life."""  # this is nothing but 'Always look \n to the bright\nside of life.'
print(mantra)

a = 'abc'
print(len(a)) # 3 as its a sequence with 3 elements/objects

s = 'abc' + 'def' # string concatenation
print(s)

print(a * 4)  # string repetition

s = 'hacker'
print('k' in s) # True
print('z' in s) # False

d = 'He is\n good'
print('is' in d) #true
print('n' in d) # false, note that there is \n and not n. \n is a single character
print('\n' in d) # true

for char in s:
    print(char, end=" ")
print()

# string indexing
s = 'computer'
print(s[:]) # 0 to len(s) ,therefore the whole string. note that in the above string 'computer', len(s) - 1 is the last index, i.e. 8-1=7
# s[:] essentially makes a top level copy of the object.
print(s[1:3]) # upper bound is not included
print(s[1:])
print(s[-1]) # same as s[len(s) - 1]
print(s[:-1]) # all but the last element
print(s[-4:]) # 'uter'
print(s[-4:-1]) # 'ute'

# each slice is really a new object
print(s[::2]) # step size of 2. default is 1
print(s[:6:2]) # prints 'cmu'

print(s[::-1]) # reverse the string
print(s[4:6:-1]) # not logical, and therefore returns empty string ''
print(s[5:1:-1]) # 'tupm'. note that upper bound in this case index 1 is not included

print(s[slice(5, 1, -1)]) # same as above just using the slice object
print(s[slice(None, None)]) # same as s[:]


print(int('42'), str(42))
print(repr(42)) # as-code representation
print(repr('spam')) # prints 'spam' not just spam, i.e. it prints single quotes as well. 
print(float('56.78'))
print(float('1.23e4'))

print(ord('A'))
print(ord('a'))
# print(ord('az')) # error. because ord() takes in a single character only. 
print(ord('\n')) # 10
print(chr(65)) # inverse of ord(). returns the corresponding character of the integer ASCII value
print(chr(98))

print(ord('5'))

######
# Convert a string of binary values into integer
B = '1101'
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I) # 13

######

s = 'spam'
print(s)
s = s.replace('pa', 'HAM')
print(s) # notice we replaced 2 character substring 'pa' with 3 character string 'HAM'. this is possible because python is using concatenationg and slicing to achieve this result. 
# had it been doing it in-place it would lead to an error, as you cant replace 2 elements by 3 elements in a sequence. 
# strings are immutable and there are no changes in-place. string methods and operations always result in a new object which you can assign to the same variable if you want. 

s = 'thisisthebigthesis'
print(s)
s = s.replace('is', 'ABC')
print(s)

s = 'cool boy is very cool.'
idx = s.find('cool') # returns the index where the substring appears (starts). returns -1 if not found.
print(idx) 
s = s.replace('cool', 'hot', 1) # replace only 1 occurence 
print(s)

s = 'spammy'
L = list(s)
L[3] = 'C'
L[4] = 'C'
print(''.join(L))
w = ['this', 'is', 'good'] # list of strings
t = '-'.join(w)
print(t)

a = 'aaa bbb  ccc' # notice double space before ccc
print(a.split()) # ['aaa', 'bbb', 'ccc'] by default it splits on any whitespace in the string, i.e sep=None and ignores any empty strings
print(a.split(" ")) # split on ' ' (single space) . ['aaa', 'bbb', '', 'ccc']

a = 'aaa bbb    ccc \nddd \teee' 
print(a.split()) # ['aaa', 'bbb', 'ccc', 'ddd', 'eee'] as we said by default is splits on any whitespace and that includes any number of spaces, \n, \t also, 

line = "i'mSPAMaSPAMlumberjack"
print(line)
print(line.split("SPAM"))

s = "   \t The school is closed today\n "
print(s)
print(s.rstrip()) # strip whitespace (\n \t spaces) on the right 
print(s.lstrip()) # strip whitespace on the left
print(s.strip()) # strip whitespace from both sides
print(s.strip().upper())
print(s.isalpha()) # False, should have ONLY alphabets, not even whitespace is acceptable.
s = 'This is a football!'
print(s.isalpha()) # should have all alphabets only. this has ! symbol and therefore False
print('spam'.isalpha()) # True
print('spam2'.isalpha()) # False

print(s.startswith('This')) # True
print(s.startswith('this')) # False, because 'this' is not same as 'This'
print(s.endswith('ball!')) # True
sub = 'ball!'
print(s[-len(sub):] == sub) # alternative way to the above endswith() method

# string formatting
s = '%d times %s is %s'
print(s % (2, 'two', 'four'))
print('%s %s %s' % (23, 56.32, [45,99, 12,77]))
print('going to %s' % 'work')
# %s - strings, %d - integers
print('pie is %d' % 3.14) # prints 'pie is 3' since %d converts to int and int(3.14) is 3

print("integers:...%d...%-6d...%6d...%06d" % (1234, 1234, 1234, 1234)) # normal, 6-character with left justification, 6-character with right justification, 6 character with right justification
# and filled with zeros in places of blank space
print("%3d" %123456) # this is more than 3 characters and so will be printed as it is 123456

num = 4567.3451278
print("%e | %f | %g" % (num, num, num))
print("%E"%num) # same as %e just that exponent sign e is uppercase E

print('%.2f...%3.2f...%8.2f...%-8.2f...' % (num, num, num, num))
print('%08.2f' %num)

print('%.2e...%4.2e...%9.2e...%09.2e...'%(num, num, num, num))


print("%.2f" %56.789) # rounds to 2 decimal places, not truncation.
print("%+.2f"%56.789) # puts + sign at the front
print("%-.2f"%56.789) # does not do anything, because the number is positive. cannot just put minus sign, it would be illogical. so does nothing. 

# dictionary based formatting
print("%(n)s %(t)d %(q).2f" %{"t": 78, "q": 67.289, "n": 'spam'})

reply = """
Greetings...
Hi my name is %(name)s
I am a %(age)d years old student at %(university)s university.
"""
print(reply % {"name": "Bob", "age": 22, "university": "XYZ"})

# such formatting is often used in conjunction with the vars() builtin function which generates a dict of variable, value pairs in the scope it is called in. 
r = 'Bob'
t = 67.22
print(vars())
print()
print("%(r)s %(t)f" % vars())

# string formatting method call
template = "{0} {1} {2}" # by position
print(template.format('spam', 56.789, [6,8,'boy']))
template = '{name}, {age}, {school}' # by keywords
print(template.format(name='Bob', age=23, school='XYZ'))
template = '{name}, {0}, {school}' # both by position and keyword
print(template.format('ham', name='John', school='XYZ')) # positional arguments always come before keyword args

import sys
print('{} and {}'.format('spam', 'ham')) # 'spam and ham'
print('{1} and {0}'.format('spam', 'ham')) # 'ham and spam'
print('My {0} runs {1}'.format('laptop', sys.platform)) # 'My laptop runs win32'
print('My {1[name]} runs {0.platform}'.format(sys, {'name': 'laptop'}))  # 'My laptop runs win32' # note in the left expression there are no quotes around name key
print('My {config[name]} runs {my_sys.platform}'.format(my_sys=sys, config={"name": 'laptop', "age": 24})) # 'My laptop runs win32'

# using list indices
somelist = list('SPAM')
# print('{0} and {1}'.format(somelist)) # ERROR
print('{0} and {1}'.format(somelist[0], somelist[-1]))
print('{0[1]} and {0[0]}'.format(somelist)) # negative index and slices are not allowed, only positive integers
print('{0} and {1}'.format(*somelist))

t = 'boy', 22, [7,45,32.773] # tuple
print('{2} and {1} and {0}'.format(*t))

