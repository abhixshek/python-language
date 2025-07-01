# while loop is the most general looping construct
x= 'spam'
while x: # this same as the more verbose expression while x!= ''
    print(x, end=' ')
    x = x[1:]

print()
a, b = 0, 10
while a < b: # one way to code counter loops, we will see how to do this using for loops soon
    print(a, end=' ') # prints a from 0 upto, but not including b
    a += 1

print()
# NOTE that python does not have a 'do while' loop

# pass keyword
a = 5
while a > 0:
    pass  # do nothing.
    a -= 1

a = 5
while a > 0:
    ... # alternative to pass keyword. this is called ellipses
    a -= 1

def func1(): ... # can occur on the same line as header too.
print(func1()) # None as by default functions return None

X = ...
print(X) # Ellipses
print(type(X)) # <class ellipses>

# continue - skips to the top of the loop
x = 10
while x > 0:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=" ") # prints 8 6 4 2 0

print()
# continue should be used rarely as it reduces readability and maintainability
# alternatively we can achieve the above using if tests alone
x = 10
while x > 0:
    x = x - 1
    if x % 2 == 0:
        print(x, end=" ")

print()

# break - terminate the enclosing loop


