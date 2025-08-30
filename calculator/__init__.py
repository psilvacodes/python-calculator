"""Top-level package for python-calculator.

Exposes the public arithmetic API and the package version.
"""

from .operations import add, divide, multiply, subtract

__all__ = ["add", "subtract", "multiply", "divide", "sqrt"]
__version__ = "1.1.0"
