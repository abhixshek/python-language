import configparser


config = configparser.ConfigParser()

config.read(['file1.ini', 'file2.ini']) # the ini files are read in order, with the latter ones overwriting keys from the previous ones when the same key is repeated.

print(config.sections())

print(config['School']['name']) # takes D.A.V as this key got overwritten from file2.ini

print(config['School']['system']) # mac as it got overwritten by file2.ini


