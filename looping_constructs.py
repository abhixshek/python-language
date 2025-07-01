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
        print(x, end=" ") # prints 8 6 4 2 0

print()

# break - terminate the enclosing loop
x = 9
while x > 0:
    x -= 1
    if x % 3 == 0: break
    print(x, end=" ") # prints 8 7

print()

# loop else. the else clause of loops is executed when no break statement is encountered. Also when the while loop never starts because the condition never evaluated to True to begin with, even then
# else clause is run.

def is_prime(x):
    if x == 1:
        print('1 is neither prime or a composite number.')
        return None # need to do this because otherwise the else clause of the while loop will run for x=1 even though the while loop test condition was never true, the else part runs because break statement
    # was not encountered.

    y = x // 2 # floor division by 2
    while y > 1:
        if x % y == 0:
            print('%i is not a prime number.' %x)
            break
        y -= 1
    else:
        print('%i is a prime number.' %x)

is_prime(1)
is_prime(2)
is_prime(3)
is_prime(10)
is_prime(19)


# for loops




