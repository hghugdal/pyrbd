"""Package for creating simple reliability block diagrams using LaTeX TikZ."""

from importlib.metadata import version

from .block import Block, Series, Group
from .diagram import Diagram

__version__ = version("pyrbd")

__all__ = [
    "Block",
    "Series",
    "Group",
    "Diagram",
]
