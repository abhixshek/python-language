# some different forms of floating point numbers(floats)
a = 1.2
b = 0.5
c = .45
d = -.32
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
e = 2e3
f = 3.0E2
g = 2.45e-4
h = 4.
i = 4E120
j = 4.0e+210
print(e, f, g, h, i, j)
print(type(e), type(f), type(g), type(h), type(i), type(j))

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


# format / display floats in the exponent form
a = 3.5673
b = 7823.638211
c = 0.00826499

print('%e' %a)
print('%e' %b)
print('%e' %c)
# all are shown with a float with 1 digit to the left of the decimal and then left of the number followed by the exponent power (base 10)

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

## division: true and floor
print(4 / 5 ) # 0.8 as / always returns true division in python 3.0
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

# hexadecimal, octal and binary representations of integers
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

# to go the other way around, use int(string, base) to convert that base value to integer in bae 10, i.e. decimal
print(int('64'), int('100', 8), int('0x40', 16), int('0b1000000', 2)) # prints integer 64, all of them return integer 64

