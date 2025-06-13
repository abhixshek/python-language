# basic mathematical operators
a = 5
b = 2
print(a + b, a - b, a * b, a / b)
print(a % b) # module operator gives the remainder of the division
print(a ** b) # exponentiation. 5 to the power of 2 = 25

print(3.0 ** b) # mixed types are converted up. therefore the result is 9.0


# some different forms of floating point numbers(floats)
a = 1.2
b = 0.5
c = .45
d = -.32
e = 2.
print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))
e = 2e3
f = 3.0E2
g = 2.45e-4
h = 4.
i = 4E120
j = 4.0e+210
print(e, f, g, h, i, j)
print(type(e), type(f), type(g), type(h), type(i), type(j))

#NOTE that after e or E in the exponent form, you can only have an integer. giving a float there will result in a Syntax error. ex: 2E2.5 will give error.


# mixed types are converted up
a = 5
b = 12.0
c = a + b
print(c, type(c))

b = 4j
c = a + b
print(c, type(c))

b = 2 + 3.5j
c = a + b
print(c, type(c))

#evaluations of some mixed expressions
a = 2 ** 3 ** 2 # computes 3 ** 2 first, i.e. = 9 and then 2 ** 9 = 512
b = 2 ** 3 + 1 ** 2 # since exponentiation has higher precedence than +, it evaluates 1**2=1 and 2**3=8
# and then adds the results 8+1 = 9
print(a, b)

a = 4 * 5 / 2 #since * and / are in the same row, they have same precedence and the operations are grouped from left to right
# therefore 4*5= 20 happens first, then 20 /2 = 10 final result.
print(a)
a = 4 / 5 * 2 # 4 / 5 = 0.8 then 0.8*2 = 1.6
print(a)


a = 3
b = 4
print(b / 2 + 3) # prints 5.0 not 5 even though b and 2 both were integers in the division operation.
# if you want to have int result from division in python 3.0 then you can use // (floor division)
print(b //2 + 3)

a = 2
b = 4.0
print(a + b) # in mixed type expressions, operands are converted up to the most complex type, in this case float. so the result is also float. = 6.0



# format / display floats in the exponent form
a = 3.5673
b = 7823.638211
c = 0.00826499

print('%e' %a)
print('%e' %b)
print('%e' %c)
# all are shown with a float with 1 digit to the left of the decimal and then rest of the number followed by the exponent power (base 10)

# Comparison operators and numbers
print(3 < 5) # True
print(3.0 == 3) # True, 3 on the right is first converted up to 3.0 then compared
print(2.0 <= 2) # True, 2 on the right is first converted up to 2.0 then compared
print(2 >= 2.0) # True, 2 on the left is first converted up to 2.0 then compared
print(3 != 3.0) # False, 3 on the left is first converted up to 3.0 then compared

# chained tests
print(1 < 2 < 3) # same as 1< 2 and 2 < 3, True
print(1 <2.0 < 3) # True, first converts up 1 to float then does the comparison 1.0 < 2.0 and 2.0 < 3.0
print(1 < 2.0 < 3 > 4) # False, same as 1.0< 2.0 and 2.0 < 3.0 and 3 > 4
print(1 < 2 > 1) # True, same as 1 < 2 AND 2 > 1. NOTE that this is not 1<2 implies True > 1 => False. no this is wrong. remember that the comparisons are chained using AND
# when in doubt always think in terms of AND logical operations

## division: true and floor
print(4 / 5 ) # 0.8 as / always returns true division in python 3.0. and the result is always a float regardless of the operands
print(4.0 / 5) # 0.8
print(4 / 2) # returns 2.0
print(4 // 2) # returns 2 (int)
print(4 // 2.0) # first converts up 4 to 4.0 then performs floor division and now since operands are float, floor division is also float = 2.0
print(4 // 5) # returns 0
print(4.0 // 5) # returns 0.0

print(-4 // 5) # because // performs floor division and not truncation, the result is -1, not 0
print(-4 // 5.0) # returns -1.0
print(5 // -2) # returns -3 since 5/2 is 2.5 then 5/2 is -2.5. then since // does floor not truncation, the result is -3 not -2
print(5 // -2.0) # returns -3.0 since 5 is converted up to float and then operation performed. explanation is same as above.

import math
print(math.trunc(2.5))# 2
print(math.floor(2.5))#2
print(math.floor(-2.5))#-3
print(math.trunc(-2.5))#-2
print(math.trunc(0.8))#0
print(math.floor(0.8))#0
print(math.trunc(-0.8))#0
print(math.floor(-0.8))#-1


print(99999999999999999999999999999 + 1) # prints the result. in python2.6 prints the number followed by L to denote its a long int

# complex numbers
a = 2 + -3j # becomes 2 - 3j
print(a)
print(type(a))
print(a.real, a.imag)
print(2 + -3j * 3) # since * has higher precedence over + and - we get 2 + - 9j = (2-9j)
print((2 + -3j) * 3) # gives (6-9j)

print(1j * 1j) # gives (-1+0j) because recall from school in complex numbers j*j=-1

# hexadecimal, octal and binary representations of integers

#NOTE that whether you type literals in octal, hexa decimal or binary or decimal base 10 they are all represent integers at the end of the day.
a = 0b100 # or 0B100 will also work. this is integer 4 in binary 
# note we did not type the literal in single or double quotes. 
print(a) # prints 4
print(type(a)) # prints class int

print(0B10000) # prints integer 16
print(0b11111111) # integer 255

a = 0o7  # 7 in octal 
print(a)
a = 0o07 # again 7 in octal
print(a)

a = 0o10 # 8 in octal. since octal digits are from 0-7 only. to write integer 8 you need to move to the next place like we do in binary 00,01,10,11,etc. and that gives 10 in octal
print(a) # prints 8

print(0O377) # prints integer 255

print(0x01, 0x1, 0x09, 0x0A, 0x0B, 0x0F, 0x10, 0xFF, 0xff, 0Xff) # these are hexadecimal literals. prints 1, 1, 9, 10, 11, 15, 16, 255, 255, 255

print(oct(64), hex(64), bin(64)) # use these functions to convert integer in base 10 to the base you want accordingly. the returned value is a string in that base.

# to go the other way around, use int(string, base) to convert that base value to integer in base 10, i.e. decimal
print(int('64'), int('100', 8), int('0x40', 16), int('0b1000000', 2)) # prints integer 64, all of them return integer 64
print(int(4), int(0b100), int('0b100', 2), int('100', 2)) # all return the integer 4

# recall the eval() treats the input string as code expression
print(eval('4')) # prints 4
print(eval('0b100')) # prints 4
print(eval('0xff')) # prints 255
print(eval('0o17')) # prints 15

# we can also convert base 10 integer into its octal, hex or binary representation using string formatting
a = 12
print('{0:o}, {1:x}, {2:b}'.format(a, a, a))
print('%o, %x, %X' % (255, 255, 255))

######### Bitwise operations
x = 1 # 0001
y = x << 2 # shift x left 2 bits: 0100
print(x, bin(x))
print(y, bin(y))

y = x | 2 # bitwise OR, i.e. 0001 | 0010 . now perform OR operation on each bit you get - 0011 which is 3
print(y, bin(y))

y = x & 1 # bitwise AND, i.e. 00001 & 0001. which gives 0001
print(y, bin(y))

print(bin(x | 0b10))
print(bin(x & 0b1))

x = 0xFF # 255 in hexadecimal
print(bin(x)) # 0b11111111
y = x ^ 0b10101010 # ^ operator is the bitwise XOR
print(y, bin(y))

print(int(bin(y), 2)) # binary string to integer in base 10. prints 85

x = 85
print(x.bit_length()) # 7
print(bin(x)) # 0b1010101, notice the length is 7
# same can be achieved using bin and len functions
print(len(bin(x)) - 2)
print(bin(-85)) # -0b1010101


#### numeric modules and functions
print(pow(2.5, 3.5))
print(pow(2.5, -3.5))
print(pow(-2.5, 3.0))
print(pow(-2.5, 3.5)) # complex number because the base is negative and we have a non-integer or decimal value in the power. essentially taking root of a negative number leads to a complex number.
print(pow(0, 1)) # 0
print(pow(0, 0)) # 1

# pow(0, -5) # is 1/0^5 = 1/0 = not defined and therefore gives ZeroDivisionError

print(-2.5 ** 2) # -6.25
print((-2.5) ** 2) # 6.25. the reason is operator precedence. note that ** has higher precedence therefore in the previous expression python did 2.5 ** 2 and then add the negative sign giving -6.25
print(pow(-2.5, 2)) # 6.25, because pow() is essentially evaluating the expression passed in 1st and 2nd argument first and then taking the power. just like the above (-2.5) ** 2

print(abs(-1.00000001))
print(abs(-0.0000001))
print(abs(0.0)) # 0.0
print(abs(-5)) # 5. so it returns the same object type as the one that you have passed.


### math module
import math

print(math.pi, math.e)

print(math.sin(2 * math.pi / 180)) # should be 0 but because of decimal value of pi we get a value very close to zero but not exactly zero.
# math.cos(), math.tan()
print(math.sqrt(9), math.sqrt(9.5))
# math.sqrt(-5) throws ValueError because it doesn take negative inputs. because neg input will result in a complex number and math module does not deal with complex numbers.

print(sum((1,2,3,4))) # sum() takes an iterable as input
print(sum([1,5,6.5]))
print(min([47,642,8,4]))
print(min(76,4,3,26,4)) # min() and max() also accept individual arguments, not just iterable
print(max((867,3342,7,8,42)))


# we met truncation and flooring before, we can also do rounding
print(round(3.556, 2)) # 3.56
print(round(3.555, 2)) # 3.56
print(round(3.545, 2)) # 3.54, not 3.55
print(round(0.543, 1)) # 0.5
print(round(0.456, 0)) # 0.0
print(round(3.56), round(-3.56)) # round() returns an integer by default unless 2nd argument for how many digits to
# round to is provided
# prints 4, -4
print(round(2.5), round(3.5), round(-3.5)) # prints 2 4 -4

print(math.floor(-3.56)) # -4
print(math.floor(3.56)) # 3

print(math.trunc(-3.56)) # -3
print(math.trunc(3.56)) # 3

print(int(3.56), int(-3.56)) # 3, -3, int() does truncation

print('%.1f' %2.567, '{0:.2f}'.format(2.567))

# square roots
print(math.sqrt(9.5))
print(math.sqrt(9)) # returns 3.0, i.e. math.sqrt() will return float always
print(9 ** 0.5) # 3.0
print(pow(9, 0.5)) # 3.0

# random numbers
import random
print(random.random()) # random number in the interval [0,1)
print(random.randint(10, 25)) # random integer in the interval [a,b] , i.e. including both end points

e = [456,63,2,77,86534,12,87896,32]
print(random.choice(e)) # choose a random item from a non-empty sequence
print(random.choices(e, k=3)) # picks out k times at random from the sequence with replacement with equal probability. there is also weights and cum_weights parameters that we can pass.


### Decimal numeric type
print(0.1 + 0.1 + 0.1 - 0.3) # should print 0.0 but it prints 5.17892342e-17 which is close to zero but not exactly 0.0
# however with decimals the result can be dead-on
from decimal import Decimal

result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')   
print(result) # exactly 0.0
print(type(result))

result = Decimal('0.1') - Decimal('-0.005') # different no. of decimal places involved in the expression, python automatically converts up to the largest no. of decimal digits.
print(result)

import decimal

result = decimal.Decimal('1') / decimal.Decimal('3')
print(result) # prints 0.333333 but should have been limited to 0 decimal places because the operands did not have any. 
# to set the precision explicitly do below:
decimal.getcontext().prec = 4
result = decimal.Decimal('1') / decimal.Decimal('3')
print(result) # prints 0.3333

# this is especially useful for monetary applications
dollars = 1999
adds = 1.33
print(dollars + adds)

# context manager to set Decimal precision temporarily
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00')) # only 2 decimal places this time

print(decimal.Decimal('1.00') / decimal.Decimal('3.00')) # back to many decimal places

### Fraction type
from fractions import Fraction

x = Fraction(1, 3) # 1/3, which is num,den
y = Fraction(4, 6) # 2/3 as 4/6 is reduced by greatest common denominator (gcd) to 2/3
z = Fraction(3, 7)
print(x)
print(y)
print(x * z) # 3/21 = 1/7
print(x + z) # 16/21
print(x - y)

a = Fraction('1.25')
b = Fraction('0.33333')
c = Fraction('-1.5')
print(a)
print(b)
print(c)
print(type(c))
result = Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
print(result) # gives Fraction(0,10) which is accurate as opposed to floating point math which was giving a number close to zero but not exactly zero


# mixed type conversions
a = (2.5).as_integer_ratio()
print(a, type(a)) # tuple

f = 2.5
b = Fraction(*f.as_integer_ratio()) # * expands the tuple into arguments to the function
print(b)
print(type(b))

c = 2
d = 3.5
result = b + c # fraction + int -> fraction
print(result)
print(type(result))
result = b + d # fraction + float -> float
print(result)
print(type(result))

#### set core type



