"""Module containing global configuration options.

Attributes
----------
ARROW_STYLE : str
    definition of TikZ arrow style. Any style defined in the TikZ `arrows`
    library is valid, e.g. `'->'` and `'-latex'`. The default `''` gives a line without
    arrow head.
SERIF_FONT : bool
    `False` to use sans-serif font (default), `True` to use serif fonts
OUTPUT_DIR : str | Path
    output directory of generated diagrams (default=`""`)
SOURCE_DIR : str | Path
    output directory for LaTeX source and compile files (default=`"rbd_source"`)
"""

from pathlib import Path

ARROW_STYLE: str = ""

SERIF_FONT: bool = False

OUTPUT_DIR: str | Path = ""

SOURCE_DIR: str | Path = "rbd_source"
