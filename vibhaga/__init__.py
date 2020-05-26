""" Vibhaga initialization module """
from os import path
from sys import modules

__version__ = "0.2.0"
AUTHOR = "Kerem Koseoglu"
EMAIL = "kerem@keremkoseoglu.com"
DESCRIPTION = "Vibhaga is a dynamic module loader for Python"
PYTHON_VERSION = ">=3.6.5"


def get_root_path() -> str:
    """ Returns the root path of Vibhaga """
    return path.dirname(modules['__main__'].__file__)
