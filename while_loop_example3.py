# handling ValueError when its not a digit
print('Type STOP to stop')
while True:
    reply = input('Enter number here: ')
    if reply == 'STOP':
        break
    if not reply.isdigit():
        print('Bad!'* 8)
    else:
        print(int(reply) ** 2)
print('bye')

# The if, elif, and else parts in the preceding example are associated as part of the same
# statement because they all line up vertically (i.e., share the same level of indentation).
# The if statement spans from the word if to the start of the print statement on the last
# line of the script. In turn, the entire if block is part of the while loop because all of it
# is indented under the loop’s header line.
