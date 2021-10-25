# # importing modules
# import math
# print(math.pi)
#
# # math namespace
# print(dir(math))
# # global namespace
# print(dir())
#
# from math import pi
# print(pi)
# print(dir())
#
# # alias
# import math as m
# print(m.pi)
# print(dir())
#
# # The module namespace is implemented as a Python dictionary
# # and is available at the .__dict__ attribute:
#
# print(math.__dict__["pi"])
# print(globals())
#
#
# # The PEP 8 style guide recommends using absolute imports in general.
# # However, relative imports are an alternative for organizing package hierarchies.
# # relative import
# # from . import smth  # . - from current directory
#
# # absolute import
# # from smth import smth
#
# import sys
# for i in sys.path:
#     print(i)
#
# # Imports Style Guide
# '''
#     Keep imports at the top of the file.
#     Write imports on separate lines.
#     Organize imports into groups: first standard library imports, then third-party imports, and finally local application or library imports.
#     Order imports alphabetically within each group.
#     Prefer absolute imports over relative imports.
#     Avoid wildcard imports like from module import *.
# '''
#
# # Standard library imports
# import sys
# from typing import Dict, List
#
# # Third party imports
# import feedparser
# import html2text
#
# # Reader imports
# from reader import URL


# modules cache
from math import pi
print(pi)

# reloading a module to clear cache
# import importlib
# importlib.reload(module_name)

# built-in modules aren’t shadowed by local modules
# because the built-in finder is called before the import path finder,
# which finds local modules.
import sys
print(sys.meta_path)

import sys
print(sys.modules["math"].cos(pi))

# s long as the different versions of the package are compatible,
# you can handle this by renaming the package with as:
# try:
#     from importlib import resources
# except ImportError:
#     import importlib_resources as resources






