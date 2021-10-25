# https://www.learnpython.org/en/Variables_and_Types
# integer
myint = 17
print(myint)

# floating_point
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)

# simple operations with numbers
one = 1
two = 2
three = one + two
print(three)

# simple oeprations with strings
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# multiple assignment
a, b = 3, 4
print(a,b)

# Mixing operators between strings and numbers won't work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

# Exercise

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# https://docs.python.org/3/tutorial/introduction.html#numbers

# division always returns a floating point number
print((50 - 5 * 6) / 4)

# floor division discards the fractional part
print(10 // 3)
# the % operator returns the remainder of the division
print(10 % 3)
# floored quotient * divisor + remainder
print(3 * 3 + 1)

# calculating powers
print(3 ** 3)

# assigning values to variables
x = 10
y = 5 + x
print(x * y)

# operators with mixed type operands convert the integer operand to floating point:
print(4 *1.25 + 2)

# in interactive mode, the last printed expression is assigned to the variable _
# 5 / 2
# _ * 2

# https://docs.python.org/3/tutorial/introduction.html#strings

#  \ can be used to escape quotes:
print ('I\'m alive') # or:
print ("I'm alive")

# \n - new line:
print ('line 1 \nline 2')

# raw strings:
print(r'C:\users\notes')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# strings concatenation
print('ma'* 2 + ' and ' + 'papa')

# string literals are automatically concatenated (does not work with variables or expressions):
print ('Svit' 'lana') # but:
f = 'Sveta '
l = 'Rozova'
print (f + l)

# strings can be indexed:
s = 'autumn'
print(s[0]) # first character
print(s[-1]) # last character

# slicing:
print(s[:3])
print(s[1:])
print(s[:2] + s[2:])
print(s[3:30])

# strings are immutable:
s[0] = 'o' # returns error

len(s) # length

