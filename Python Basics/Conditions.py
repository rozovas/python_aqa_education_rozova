# https://www.learnpython.org/en/Conditions
x = 5
print(x == 5)  # True
print(x == 3)  # False
print(x < 10)  # True

age = 10
name = 'George'
if age == 10 and name == 'George':
    print('George is a 10-year old boy')
if name == 'George' or name == 'John' or name == 'Ringo' or name == 'Paul':
    print('You\'re one of the Beatles guys')

# in operator
if name in ['George', 'John', 'Ringo', 'Paul']:
    print('You\'re one of the Beatles guys')

# code blocks, indentation
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# another example
if x == 5:
    print('x equals 5')
else:
    print('x does not equal 5')

# the "is" operator does not match the values of the variables,
# but the instances themselves:
x = [2, 4, 6]
y = [2, 4, 6]
print(x == y)
print(x is y)

# not operator
print(not True)
print((not False) == (True))

# exercise
# change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1,2]

if number > 15:
    print("1")
if first_array:
    print("2")
if len(second_array) == 2:
    print("3")
if len(first_array) + len(second_array) == 5:
    print("4")
if first_array and first_array[0] == 1:
    print("5")
if not second_number:
    print("6")

