# if / elif / else

if 1: # 1 is a boolean true
    print('running if block')

if 0:
    print('true')
else:
    print('false') # false gets printed because 0 is a boolean false


subject = 'AI' 
if subject == 'ML':
    print('ML is a subset of AI')
elif subject == 'DL':
    print('DL is a subset of ML')
else: # this gets run as all tests failed
    print('AI is the superset covering both ML and DL to perform complex tasks')

# There is no CASE or SWITCH statement in Python. Instead we code multiple if/elif conditions.
# An alternative to that is using dictionaries or lists.
# example
choice = 'ham'
print({'spam': 10,
      'ham': 90,
      'eggs': 50,
      'beacon': 70}.get(choice, 'None from available choices')) # we used .get() method of dictionary to handle the case where the choice is none of the ones we considered

choice = 'frog'
print({'spam': 10,
      'ham': 90,
      'eggs': 50,
      'beacon': 70}.get(choice, 'None from available choices'))

# the same in if/elif would look like:
choice = 'spam'

if choice == 'spam':
    print(10)
elif choice == 'ham':
    print(90)
elif choice == 'eggs':
    print(50)
elif choice == 'beacon':
    print(70)
else:
    print('None from available choices') # this is same as the default value obtained from .get() if none of the cases match

branch = {'spam': 10,
      'ham': 90,
      'eggs': 50,
      'beacon': 70}
print(branch.get(choice, 'None from available choices'))

# using in membership tests
choice = 'milk'
if choice in branch:
    print(branch[choice])
else:
    print('None from available choices') # this gets executed as choice was not in branch dictionary

# string literals are concatenated when placed adjacent
s = 'hello ' 'world'
print(s) # this was same as doing s = 'hello' + 'world'

# doing it on multiple lines, enclose them in parenthesis
s = ('this is '
        'a beautiful '
        'city of India'
    )
print(s)

# combining multiple simple statements in a single line using ;
x = 1; y = 2; print(x + y)

if y: print(y ** 2)

## Truth tests - and , or 
print(2 or 3, 3 or 2) # or returns the first object which is true in in the expression
# prints 2 for the 1st case and 3 for the 2nd case

print([] or 3) # prints 3 as thats the first true value encountered

result = [] or 3
print(type(result)) # its indeed 3 , an integer. not True or False

print([] or {}) # since the 1st operand is False, it goes to the second operand and returns the 2nd operand whether its true or false. therefore it prints {}

# and operator
print(2 and 3, 3 and 2) # stops at the first false value encountered
print([] and 3) # returns []
print([] and {}) # returns []
print(3 and []) # returns []

X = 2
Y = 3
Z = 5
if X:
    A = Y
else:
    A = Z

print(A)
# the short-hand for the above called ternary expression is:
A = Y if X else Z
print(A)

A = 't' if 'spam' else 'f'
print(A)
A = 't' if '' else 'f'
print(A)

# Same can be achieved by a careful combination of `and` and `or` operators because they either return the object on the left side or the object on the right side.
A = ((X and Y) or Z)
# But there is a catch in this. There is an assumption that Y is a Boolean true.
print(A)

# NOTE since the above expression requires a bit more time to understand for a new developer, it is usually preferred it keep things simple and use ternary expression when dealing with
# simple cases or use the full form of if and else.

# another alternative
X = 2
Y = 3
Z = 5
A = [Y, Z][bool(X)]
# since bool converts X into an equivalent of integer 1(True) or 0 (False) it can be used as above to allow for selection just like an if else
print(A) # A takes the value of Z i.e. 5

r = ['f', 't'][bool('')] # r = 'f'
print(r)
r = ['f', 't'][bool('spam')] # r = 't'
print(r)
# However, this isn’t exactly the same, because Python will not short-circuit—it will always run both Z and Y, regardless of the value of X.

# using boolean operators to assign non-empty object
A = X or Y or Z or None # A = X since X is non-empty = 2
print(A)
A = [] or 0 or {} or False or 45 # A = 45
print(A)
