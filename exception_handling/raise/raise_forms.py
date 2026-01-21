print('hello world')
# raise # if you uncomment this line, this script fails because raise keyword alone reraises the previous raised error, but here there is none
# and this causes RuntimeError

# raise IndexError # creates an instance and then raises exception
# raise IndexError() # uses the instance and raises exception. Both of these raise statememt forms create an instance of the class then raise the Exception

exc = IndexError() # you can create an instance before the raise statement
# raise exc # raises IndexError just like those above
try:
    print('running try')
    raise IndexError
except IndexError as x:
    print(type(x)) # here x is an instance of the class IndexError
    # the `as x` part in the except clause is optional. If it is not there then the instance is simply not assigned to any name you can reference.
    # but if you are interested in using the instance's attributes or methods after this exception is raised, you can use this as x syntax.



