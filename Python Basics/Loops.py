# # https://www.learnpython.org/en/Loops
# # for loop
# # my_list = [2, 3, 5, 7]
# # for i in my_list:
# #     print(i)
#
# # Prints out the numbers 0,1,2,3,4
# for x in range(5):
#     print(x)
#
# # Prints out 3,4,5
# for x in range(3, 6):
#     print(x)
#
# # Prints out 3,5,7
# for x in range(3, 8, 2):
#     print(x)
#
# # while loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1  # = count + 1
#
# # Prints out 0,1,2,3,4
# # break and continue
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
#
# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x)
#
# # else with loops
# # If a break statement is executed inside the for loop then the "else" part is skipped.
# # Note that the "else" part is executed even if there is a continue statement.
# # Prints out 0,1,2,3,4 and then it prints "count value reached 5"
#
# count = 0
# while (count < 5):
#     print(count)
#     count += 1
# else:
#     print("count value reached %d" % (count))
#
# # Prints out 1,2,3,4
# for i in range(1, 10):
#     if (i % 5 == 0):
#         break
#     print(i)
# else:
#     print("this is not printed because for loop is terminated "
#           "because of break but not due to fail in condition")
#
# # exercise:
# # Loop through and print out all even numbers from the numbers list
# # in the same order they are received.
# # Don't print any numbers that come after 237 in the sequence.
# numbers = [
#     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#     743, 527
# ]
#
# # your code goes here
# for number in numbers:
#     if number == 237:
#         break
#     if number % 2 == 0:
#         print(number)
#
# # https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)
# for i, v in enumerate(['one', 'two', 'three']):
#     print(i, v)
#
# # To loop over two or more sequences at the same time,
# # the entries can be paired with the zip() function.
# questions = ['name', 'pet\'s name']
# answers = ['John', 'Jerry']
# for q, a in zip(questions, answers):
#     print('What is your {0}? It is {1}'.format(q, a))
#
# for i in reversed(range(1, 10, 2)):
#     print(i)
#
# things = ['pen', 'copybook', 'phone', 'passport', 'laptop', 'wallet', 'pen']
# for i in sorted(things):
#     print(i)
#
# for i in sorted(set(things)):
#     print(i)
#
# #  it is often simpler and safer to create a new list than change it in a loop:
# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)
#
# # https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
#
# # break
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:  # loop fell through without finding a factor
#         print(n, 'is a prime number')

# continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)