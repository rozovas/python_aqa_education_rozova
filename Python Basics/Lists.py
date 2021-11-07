# https://www.learnpython.org/en/Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

mylist = [1,2,3]
print(mylist[10])

# exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('hello')
strings.append('world')
second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# https://docs.python.org/3/tutorial/introduction.html#lists

season = ['autumn', 'winter', 'spring', 'summer']

#  lists can be indexed and sliced:

print(season[1])
print(season[-3:])

# concatanation is supported:
print(season + [1, 2, 3, 4])

#  lists are a mutable type:
season[-1] = 'hottest season'
print(season)

# adds new item to the end of the list:
season.append('january')
print(season)

# assignment to slices is possible:
season[-2:] = ['summer', 'june']

len(season)

# clear the list by replacing all the elements with an empty list
season[:] = []

nesting lists:
season = ['autumn', 'winter', 'spring', 'summer']
month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
         'september', 'october', 'november', 'december']
year = [season, month]
print('Jim Carrey was born in ' + year[0][1] + ' on ' + year[1][0] + ' 17.')

# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

even_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
even_list.append(20)
print(even_list)
odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
odd_list.extend(even_list)
print(odd_list)
odd_list.insert(0, 0)
print(odd_list)
odd_list.remove(20)
print(odd_list)
odd_list.pop() # removes and returns last
print(odd_list)
odd_list.pop(-2) # -2 is position of the item in the list
print(odd_list)
print(odd_list.index(11, 0, 10)) # returns index of 11
odd_list.append(11)
print(odd_list.count(11)) # counts how many values equal to 11 in the list
odd_list.reverse()
print(odd_list)
odd_list.sort(reverse=True)
print(odd_list)
shallow_copy = odd_list.copy() # Equivalent to a[:]
print(shallow_copy)
odd_list.clear()
print(odd_list)