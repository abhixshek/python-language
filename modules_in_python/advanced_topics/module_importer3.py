from formats import money, commas


print(money(123.4567))
print('%s %s' %(commas(34223), 34223))

# since we wrote docstrings for these functions. we can retrieve them
print(money.__doc__)

help(money)

import formats
help(formats)


