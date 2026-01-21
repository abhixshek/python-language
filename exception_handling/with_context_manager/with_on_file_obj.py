f = open('hello.txt', 'w')
f.write('5\n7\n12\n5.67\n89')
f.close()

with open('hello.txt') as myfile:
    for line in myfile:
        print(line, end="")

print('\n\nlets convert each line into integer')
with open('hello.txt') as myfile:
    for line in myfile:
        print(int(line))

