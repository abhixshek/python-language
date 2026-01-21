try:
    print(55)
    raise IndexError
    print(100)
finally:
    print('running termination code\n') # this line is still printed despite the try block failing(raiing an error).
    # The error is caught by the default exception handler and termninates the program, but the important thing is that finally block runs first and only after that the program terminated. 

print('hello') # this line is not run

