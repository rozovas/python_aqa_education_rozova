# https://www.learnpython.org/en/Basic_String_Operations
string1 = "Hello world!"
print("single quotes are ' '")
print(len(string1))
print(string1.index('o'))
print(string1.count('l'))
print('The ' + string1[6:-1] + ' is awesome!')
print(string1[::2]) # [start:end:step]
print(string1[::-1]) # reversing a string
print(string1.upper())
print(string1.lower())
print(string1.startswith('hello'))
print(string1.startswith('Hello'))
print(string1.endswith('!'))
print(string1.split(' '))

# exercise
s = 'Love is all you need'
# Length should be 20
print('Length of s = %d' % len(s))

# First occurrence of "a" should be at index 8
print('The first occurrence of the letter a = %d' % s.index('a'))

# Number of a's should be 2
print('a occurs %d times' % s.count('a'))

# Slicing the string into bits
print('The first five characters are "%s"' % s[:5])  # Start to 5
print('The next five characters are "%s"' % s[5:10])  # 5 to 10
print('The thirteenth character is "s"' % s[12])  # Just number 12
print('The characters with odd index are "%s"' % s[1::2])  # (0-based indexing)
print('The last five characters are "%s"' % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print('String in uppercase: %s' % s.upper())

# Convert everything to lowercase
print('String in lowercase: %s' % s.lower())

# Check how a string starts
if s.startswith('Love'):
    print('String starts with "Love". Good!')

# Check how a string ends
if s.endswith('ome!'):
    print('String ends with "ome!". Good!')

# Split the string into three separate strings,
# each containing only a word
print('Split the words of the string: %s' % s.split(' '))
