file = open('xyz123.txt', 'w')
try:
    l = [5, 6, 7]
    file.write(l)
    print('Wrote data to file') # this does not get printed because the above line raises TypeError as you can only write str to file objects in normal write mode.
finally:
    file.close()
    print('file closed') # this is printed despite the exception raised because finally is executed regardless of whether or not exception is raised.

print('not reached') # this is not printed because execution never reaches here. After executing finally block, program terminates with TypeError exception

