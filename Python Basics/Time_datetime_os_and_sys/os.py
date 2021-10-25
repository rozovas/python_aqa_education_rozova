# # os
# import os
# print(os.name)
# print(os.environ)  # dictionary of environmental variables
# print(os.getlogin()) # user name logged in to the terminal
# print(os.getpid()) # id of the current process
# print(os.getppid()) # return the parent’s process id
# # os.uname() #OS info, seem to not work on windows
# # os.access()
# # os.chdir(path) # change directory
# link = 'C:/Users/sv/PycharmProjects/pythonProject/Python Basics'
# link2 = 'C:/Users/sv/PycharmProjects/pythonProject'
# for list in os.listdir(link):
#     print(list)
# os.chdir(link2)
#
# def listdirectories():
#     list2 = link2 = 'C:/Users/sv/PycharmProjects/pythonProject'
#     for list in os.listdir(link2):
#         print(list)
#
# listdirectories()
#
# print(os.supports_bytes_environ)  #True if the native OS type of the environment is bytes (eg. False on Windows).
#
# print(os.getcwd()) # current working directory
# # os.mkdir('C:/Users/sv/PycharmProjects/pythonProject/newdir', mode=0o777, dir_fd=None) # create a directory
# # listdirectories()
# # os.rename('C:/Users/sv/PycharmProjects/pythonProject/newdir', 'C:/Users/sv/PycharmProjects/pythonProject/newdir222')
# # listdirectories()
# # os.rmdir('C:/Users/sv/PycharmProjects/pythonProject/newdir222') # remove empty dir
# # os.removedirs(path) - removes directory then tries to remove parent directories recursively if they are empty
# # listdirectories()
# # os.truncate('C:/Users/sv/PycharmProjects/pythonProject/Time_datetime_os_and_sys/filefortruncate11111.txt', 11) # trancates file to length.
# # listdirectories()

# print(os.urandom(10))
# print(os.times())  # Returns the current global process times
# print(os.urandom(9)) # Return a string of size random bytes suitable for cryptographic use.

# sys
import sys
print(sys.argv)
print(sys.byteorder) # This will have the value 'big' on big-endian (most-significant byte first) platforms,
# and 'little' on little-endian (least-significant byte first) platforms.
print(sys.builtin_module_names) # A tuple of strings containing the names of all modules
# that are compiled into this Python interpreter.
print(sys.dllhandle) # Integer specifying the handle of the Python DLL.
print(sys.exec_prefix )
print(sys.exec_prefix )
# sys.exit() # exit from python. This is implemented by raising the SystemExit exception,
# so cleanup actions specified by finally clauses of try statements are honored,
# and it is possible to intercept the exit attempt at an outer level.
print(sys.float_info)
print(sys.getdefaultencoding()) # returns used encoding
print(sys.getfilesystemencoding()) # returns files encoding
q = 3333
print(sys.getrefcount(q))
w = 3333
print(sys.getrefcount(q))
print(sys.getsizeof(q))
print(sys.getwindowsversion())
print(sys.hash_info)
print(sys.hexversion)
print(sys.implementation)
print(sys.int_info)
print(sys.maxsize) # An integer giving the maximum value a variable of type Py_ssize_t can take.
# It’s usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.

for name in sys.modules:
    print(name)
for name in sys.path:
    print(name)

print(sys.platform)
print(sys.prefix) #A string giving the site-specific directory prefix
# where the platform independent Python files are installed
print(sys.dont_write_bytecode)
print(sys.version)
print(sys.api_version) # C API
print(sys.winver) #python version used to form registry keys on Windows platforms