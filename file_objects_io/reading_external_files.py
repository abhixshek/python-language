f = open('file1.txt', 'r') # 'r' is read mode and is the default in fact.
lines = f.readlines()
print(lines)
# ['This is a txt file.\n',
# 'It contains special characters like !)$^#&!${}:"\'>?<\\\n', '5 / 4\n',
# 'Notice it even contains a backslash that is escaped (using double backslash) when read in python as a string\n',
# 'I am keeping one blank line at the end of the file\n']

# NOTICE that every line read contains a \n ending
# NOTE that the last blank line in the original txt file did not come as an item in the above list.
# in fact, even the vi editor does not show that blank line.
# backslash in the original text is escaped using double backslash and is 1 byte, recall from strings chapter
# every escape sequence is 1 byte and each character is also 1 byte.

f = open('file2.txt') # file2.txt is nearly same as file1.txt except that it ends with 2 blank lines in the original file
lines = f.readlines()
print(lines)
# ['This is a txt file.\n',
# 'It contains special characters like !)$^#&!${}:"\'>?<\\\n', '5 / 4\n',
# 'Notice it even contains a backslash that is escaped (using double backslash) when read in python as a string\n',
# 'I am keeping one blank line at the end of the file\n',
# '\n']

# NOTICE that file2.txt contained 2 blank lines at the end in the original text file and this time we have got the
# 2nd last line as a '\n' element in the above list
