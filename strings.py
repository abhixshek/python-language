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

