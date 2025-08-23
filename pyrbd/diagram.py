"""Module containing Diagram class definition."""

import subprocess

from .block import Block


class Diagram:
    """Reliability block diagram class definition.

    Parameters
    ----------
    name : str
        name of diagram
    blocks : list[Block]
        (nested) list of `Block` instances
    hazard : str, optional
        string defining the `hazard` block text
    """

    def __init__(self, name: str, blocks: list[Block], hazard: str = "") -> None:
        self.filename = f"{name}.tex"
        if hazard:
            self.head = Block(hazard, "red!60")
        else:
            self.head = blocks.pop(0)

        self.head.id = "0"
        self.blocks = blocks
        self.blocks[0].parent = self.head

    def write(self) -> None:
        """Write diagram to .tex file."""

        with open(self.filename, mode="w", encoding="utf-8") as file:
            file.write(TEX_PREAMBLE)
            for block in [self.head, *self.blocks]:
                file.write(block.get_node())
            file.write(TEX_END)

    def compile(self) -> None:
        """Compile diagram .tex file.

        Raises
        ------
        FileNotFoundError
            If .tex file is not found, e.g. because `Diagram.write()` has not been called
            before `Diagram.compile()`.
        """

        try:
            subprocess.check_call(["latexmk", self.filename])
            subprocess.check_call(["latexmk", "-c", self.filename])
            subprocess.check_call(["rm", self.filename])
        except subprocess.CalledProcessError as err:
            if err.returncode == 11:
                raise FileNotFoundError(
                    (
                        f"File {self.filename} not found. "
                        + "Check if call to Class method write() is missing."
                    )
                ) from err


TEX_PREAMBLE = "\n".join(
    [
        r"\documentclass{standalone}",
        r"\usepackage{tikz}",
        r"\usetikzlibrary{shapes,arrows,positioning,calc}",
        r"\pgfdeclarelayer{background}",
        r"\pgfsetlayers{background, main}",
        r"\tikzset{",
        r"connector/.style={",
        r"-latex,",
        r"font=\scriptsize},",
        r"line/.style={",
        r"font=\scriptsize},",
        r"rectangle connector/.style={",
        r"connector,"
        r"to path={(\tikztostart) -- ++(#1,0pt) \tikztonodes |- (\tikztotarget) },",
        r"pos=0.5},"
        r"rectangle connector/.default=0.5cm,",
        r"rectangle line/.style={",
        r"line,"
        r"to path={(\tikztostart) -- ++(#1,0pt) \tikztonodes |- (\tikztotarget) },",
        r"pos=0.5},"
        r"rectangle line/.default=0.5cm,",
        r"straight connector/.style={",
        r"connector,",
        r"to path=--(\tikztotarget) \tikztonodes}",
        r"}",
        r"\begin{document}",
        r"\begin{tikzpicture}",
        "",
    ]
)

TEX_END = "\n".join(
    [
        r"\end{tikzpicture}",
        r"\end{document}",
    ]
)
