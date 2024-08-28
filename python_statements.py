a = 5 # assignment statement
a, b = 5, 'rt'
print(a) # function calls are also statements
print(b)

a , *b = 5, 12, 'rt', (4,5) # notice * mark
print(a)
print(b)
print(type(b)) # list

# if/elif/else , for/while are also statements.

# multiple statements in a single line using ;
a = 5; b = 10; c = a + b; print(c)

# single statement across multiple lines possible when using [], {}, ()
a = [111,
         222,
    333]
# there is no indentation requirement in the above as you can see.
A, B, C = 1, 5, 10

if (A == 1 and
    B == 5 and
    C == 10):
    print(A+B+C)

# dated technique of \ also works, but is not recommended today
D = A + B + \
    C
print(D)

# the nested statements of a compound statement can be written on a single line
if A == 1: print('single line if')

if A == 1: print(A)
else: print('single line if else')

