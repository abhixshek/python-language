print('dummy calculator module')
print('2 + 2 = 4 always')
import args # the question is which module is it importing?
# the fact is when you run this calculator.py module directly it will import args.py from this same directory
# but when you import this module calculator in another module importer1.py which is outside this directory,
# importer1.py's home directory itself finds a args.py module and uses that instead of args.py found in this directory.
# that is, which args gets imported depends on which module imports this calculator.py
# to fix it to always use args.py found in this directory, we use relative imports.
# see calculator2.py
print(args)
print()
print(f'{args.a} + {args.b} =', args.a + args.b)

