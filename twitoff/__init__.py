"""Twitoff is our python package. 
__init__.py marks twitoff directory as a Python package directory. 
When twitoff package is imorted, __init__.py is implicitly executed, and the objects it defines are bound to names in the package’s namespace. 

__init__.py file is usually empty (a good practice, if the package’s modules and sub-packages do not need to share any code), or can be used to define any variables at the package level.

"""

from .app import create_app
# relative imports: A single dot means that the module or package referenced is in the same directory as the current location. Two dots mean that it is in the parent directory of the current location. Three dots mean that it is in the grandparent directory, and so on.
APP = create_app()