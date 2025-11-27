"""
mydir.py: a module that lists the namespaces of other modules
"""

seplen = 60
sepchr = '-'

def my_listing(module, verbose=True):
    attributes = {}
    if not verbose:
        for key in module.__dict__:
            if key.startswith('_'):
                continue
            attributes[key] = module.__dict__[key]


    print(sepchr * 60)
    print('name: %s    file: %s' %(module.__name__, module.__file__))
    print(sepchr * 60)

    size_of_count = len(str(len(attributes)))

    for idx, key in enumerate(attributes):
        print('%0*d) %s %s' %(size_of_count, idx, key, attributes[key]))



import moda
import sys
my_listing(moda, verbose=False)

