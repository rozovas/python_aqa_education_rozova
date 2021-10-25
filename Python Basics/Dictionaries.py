# https://www.learnpython.org/en/Dictionaries

phonebook = {}
phonebook['John'] = 938477566
phonebook['Jack'] = 938377264
phonebook['Jill'] = 947662781
print(phonebook)

# or:

phonebook = {
    'John' : 938477566,
    'Jack' : 938377264,
    'Jill' : 947662781
}
print(phonebook)

# iterating over dictionaries
for k, v in phonebook.items():
    print('%s\'s phone number is %d' % (k, v))

# removing a value
del phonebook['Jill']
print(phonebook)

# phonebook.pop() works similarly
# phonebook.pop('Jack')

# exercise

phonebook2 = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
# your code goes here
phonebook2['Jake'] = 938273443
phonebook2.pop('Jill')

# testing code
if "Jake" in phonebook2:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook2:
    print("Jill is not listed in the phonebook.")

# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

tel = {'mum' : 11111111, 'dad' : 22222222, 'brother' : 555555555}
tel['sister'] = 33333333
print(tel)
del tel['dad']
print(tel)
print(list(tel))
print(sorted(tel))
print('mum' in tel)
print('dad' not in tel)

# dict constructor:

a = dict([('mum', 11111111), ('dad', 22222222), ('sister', 4444444444)])
print(a)

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
dictionary = {x: x**2 for x in (2, 4, 6)}
print(dictionary)
dictionary2 = dict(sape=4139, guido=4127, jack=4098)
print(dictionary2)
