# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_dgarg1")

from pycounts_dgarg1.gg import count_words