# opening a file
f = open('coming_home_lyrics.txt', 'r')
# r = read, w = write, + = read+write, t = text mode, a = appending, b = binary

# reading a file
print(f.read())  # read the whole file
print(f.read(1))  # 1 - number of symbols top read

# reading line by line
for  line in f:
    print(line)

f.close()

# writing into the file
l = [str(i)+str(i-1) for i in range(20)]
f = open('list.txt', 'w')
for i in l:
    f.write(i + '\n')
f.close()


f = open('list.txt', 'r')
for line in f:
    print(line)
f.close()

# https://realpython.com/read-write-files-python/#reading-and-writing-opened-files
# reading
with open('coming_home_lyrics.txt', 'r') as reader:
    print(reader.readline(10))
    print(reader.readline(10))
    print(reader.readline(10))


f = open('coming_home_lyrics.txt')
print(f.readlines())
f.close()
f = open('coming_home_lyrics.txt')
a = list(f)
print(a)
f.close()

with open('coming_home_lyrics.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line, end = '')
        line = reader.readline()

with open('coming_home_lyrics.txt', 'r') as reader:
    for l in reader.readlines():
        print(l, end = '')

# writing
with open('coming_home_lyrics.txt', 'r') as reader:
    coming_home_lyrics = reader.readlines()

with(open('coming_home_lyrics.txt', 'w')) as writer:
    # writer.writelines(reversed(coming_home_lyrics))
    for line in reversed(coming_home_lyrics):
        writer.write(line)



# reading a file as bytes object
with open('GetImage1.png', 'rb') as byte_reader:
    print(byte_reader.read(1))  # A “magic” number to indicate that this is the start of a PNG
    print(byte_reader.read(3))  # PNG in ASCII
    print(byte_reader.read(2))  # A DOS style line ending \r\n
    print(byte_reader.read(1))  # A DOS style EOF character
    print(byte_reader.read(1))  # A Unix style line ending \n
    print(byte_reader.read())
