from importlib.metadata import version, PackageNotFoundError
from wannacri.wannacri import main

try:
    __version__ = version("wannacri")
except PackageNotFoundError:
    # Not installed
    __version__ = "not installed"
