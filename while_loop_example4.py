# handling ValueError when its not a digit
print('Type STOP to stop')
while True:
    reply = input('Enter number here: ')
    if reply == 'STOP': break
    try:
        num = int(reply)
    except:
        print('Bad!'* 8)
    else:
        print(num ** 2)
print('bye')

# This try statement is composed of the word try,
# followed by the main block of code (the action we are trying to run), followed by an
# except part that gives the exception handler code and an else part to be run if no
# exception is raised in the try part. Python first runs the try part, then runs either the
# except part (if an exception occurs) or the else part (if no exception occurs).
