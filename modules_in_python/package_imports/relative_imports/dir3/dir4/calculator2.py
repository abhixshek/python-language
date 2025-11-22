print('dummy calculator module')
print('2 + 2 = 4 always')
from . import args # this tells python to use args module in the directory where this module calculator2.py sits.
print()
print(args)
print()
print(f'{args.a} + {args.b} =', args.a + args.b)
# you can also get a and b using:
from .args import a, b
print(a, b)
