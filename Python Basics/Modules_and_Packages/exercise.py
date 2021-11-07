import re

# find_functions = []
# s = dir(re)
# for f in range(len(s)):
#     if 'find' in s[i]:
#         find_functions.append(s[i])
#
# print(sorted(find_functions))

find_functions = []
for f in dir(re):
    if 'find' in f:
        find_functions.append(f)

print(sorted(find_functions))
