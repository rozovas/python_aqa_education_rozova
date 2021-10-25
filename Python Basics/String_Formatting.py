# https://www.learnpython.org/en/String_Formatting

n = 'you'
print('Hey, %s!' % n)

# tuple for more than one arguments

m = 'me'
print('Hey, %s and %s!' % (n, m))

x = 2022
print ('%d is coming...' % x)

pie = 0.5
print(f'There is {pie} (half) a pie left')

mylist = [1,2,3]
print('The list contains: %s' % mylist)

# exercise

data = ('John', 'Doe', 53.44)
format_string = 'Hello %s %s. Your current balance is $%.2f.'

print(format_string % data)

# https://realpython.com/python-string-formatting/

# 1 “Old Style” String Formatting (% Operator)
capital = 30567
name = 'Luisa'
print('Hello, %s' % name)

# Here, you can use the %x format specifier
# to convert an int value to a string and to represent it as a hexadecimal number:
print("Capital hash is %x" % capital)
print('Hey, %s, you saved some money: %d' % (name, capital))

print('Hey %(name)s, you saved %(capital)d!' % {"name": name, "capital": capital })

# 2 “New Style” String Formatting (str.format)
print('Hello, {}!'.format(name))
print('Hey {name}, you saved some money: {capital:d}.'.format(name=name, capital=capital))

# 3 String Interpolation / f-Strings (Python 3.6+)
print(f'Hello, {name}!')
# Because you can embed arbitrary Python expressions, you can even do inline arithmetic with it:
a = 7
b = 9
print(f'Seven plus nine is {a + b}.')

# 4 Template Strings (Standard Library)
from string import Template
t = Template('Hey, $name')
print(t.substitute(name=name))
# If your format strings are user-supplied,
# use Template Strings (#4) to avoid security issues.
# Otherwise, use Literal String Interpolation/f-Strings (#3) if you’re on Python 3.6+,
# and “New Style” str.format (#2) if you’re not.
