# https://www.learnpython.org/en/Sets

print(set('my name is Eric and Eric is my name'.split()))

# intersection

a = set(['Jake', 'Jill', 'Julie'])
print(a)
b = set(['John', 'Jill', 'Jake'])
print(b)
print('\n')
print(a.intersection(b))
print(b.intersection(a))

# "symmetric_difference" method:
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# "difference" method:
print(a.difference(b))  # Julie is present in a, but missing in b
print(b.difference(a))  # John

# "union" method:
print(a.union(b))

# exercise
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
a1 = set(a)
b1 = set(b)
print(a1.difference(b1))

# https://docs.python.org/3/tutorial/datastructures.html#sets
# set operations

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(a | b)
print(a & b)  # in both a and b
print(a ^ b)  # in a or b but not both

# list comprehension
squares = [x**2 for x in range(10)]

print(squares)

# set comprehensioons are supported:
a = {x for x in 'baracadabra' if x not in 'abc'}
print(a)
