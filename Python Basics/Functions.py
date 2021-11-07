# https://www.learnpython.org/en/Functions
def kittycat():
    print('Cat! I\'m a kitty cat! \nAnd I meow, meow, meow and I meow, meow, meow\n' * 3)


def sum_function(a, b):
    return a + b


def greeting(name):
    print('Hello, %s!' % name)


kittycat()
print(sum_function(10, 2))
greeting('Sveta')

# exercise
# 1. Add a function named list_benefits() that returns the following list of strings:
# "More organized code", "More readable code", "Easier code reuse",
# "Allowing programmers to share and connect code together"
# 2. Add a function named build_sentence(info) which receives a single argument
# containing a string and returns a sentence starting with the given string
# and ending with the string " is a benefit of functions!"
# Run and see all the functions work together!


# Modify this function to return a list of strings as defined above
def list_benefits():
    return [ 'More organized code',
             'More readable code',
             'Easier code reuse',
             'Allowing programmers to share and connect code together']

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + ' is a benefit of functions.'

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

# https://www.learnpython.org/en/Multiple_Function_Arguments

# declaring functions which receive a variable number of arguments:
def function1(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))


function1(1, 2, 3, 4, 5, 6)

#kwargs
def function2(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first


result = function2(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

# exercise
# edit the functions prototype and implementation
def foo(a, b, c, *options):
    return len(options)

def bar(a, b, c, **koptions):
    if koptions.get('magicnumber') == 7:
        return True
    else:
        return False

print(foo(1, 2, 3, 4, 7, 9))

print(bar(1, 2, 3, magicnumber = 7))

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")