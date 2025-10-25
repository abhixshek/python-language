import module1


module1.printer('john')

import dir1.simple_file # this does not work when simple_file.txt is the only file in dir1
# only when there exists a file like simple_file.py, this statement is working.
# NOTE that you can have both simple_file.txt and simple_file.py in that directory and python will automatically pick the
# .py file and there wont be any conflict.
# in other words, .txt file extension is not considered for imports in any case
# in addition to .py or .pyc files, only c or c++ extension files are supported

print(dir1.simple_file.a)



