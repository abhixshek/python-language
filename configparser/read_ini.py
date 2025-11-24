import configparser


config = configparser.ConfigParser()

print(config.sections()) # empty list

config.read('file1.ini')

print(config.sections()) # ['school.student']
# there is no DEFAULT in this list


print('abc' in config.sections()) # False
print('school.student' in config.sections()) # True, this is a simple membership test of an item in a list

default_dict = config.defaults()
print(default_dict)

print(config['school.student']) # section object. does not show dictionary and its values directly. it needs to be prompted with a key

print(config['school.student']['age'])
print(config['school.student']['user'])

age = config['school.student']['age']
print(age, type(age)) # 22, str. 
# NOTE, all values read from ini files are read as string. You need to convert them into data types you want
age = int(age)
print(age, type(age))

print()
for key in config['school.student']:
    print(key)

# NOTE, that although we iterated over school.student section, we also got keys from the default section. i.e., default section is included in all section' keys
# NOTE, all keys are in lowercase once read into the parser
# NOTE, the section names maintain their case even after loading into the parser

print()
for key in config['School']:
    print(key)

print()
print("Name of the school is:", config.get('School', 'name'))

