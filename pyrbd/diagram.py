"""Module containing Diagram class definition."""

from subprocess import check_call

from .block import Block


class Diagram:
    """Reliability block diagram class definition.

    Parameters
    ----------
    name : str
        name of diagram
    blocks : list
        (nested) list of `Block` instances
    hazard : str, optional
        string defining the `hazard` block text

    Attributes
    ----------
    name : str
        diagram name
    blocks : list
        (nested) list of `Block` instances entering the block diagram
    head : Block
        first block in diagram
    preamble : str
        diagram Tex file preamble
    end : str
        diagram Tex file end
    """

    preamble = "\n".join(
        [
            r"\documentclass{standalone}",
            r"\usepackage{tikz}",
            r"\usetikzlibrary{shapes,arrows,positioning,calc}",
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

    end = "\n".join(
        [
            r"\end{tikzpicture}",
            r"\end{document}",
        ]
    )

    def __init__(self, name: str, blocks: list, hazard: str = "") -> None:
        self.name = f"{name}.tex"
        self.head = Block(hazard, "red!60")
        self.head.id = "0"
        self.blocks = blocks

        self.blocks[0].parent = self.head

    def write(self) -> None:
        """Write diagram to .tex file."""

        with open(self.name, mode="w", encoding="utf-8") as file:
            file.write(self.preamble)
            file.write(self.head.get_node())
            for block in self.blocks:
                file.write(block.get_node())
            file.write(self.end)

    def compile(self) -> None:
        """Compile diagram .tex file."""

        check_call(["latexmk", self.name])
        check_call(["latexmk", "-c", self.name])
        check_call(["rm", self.name])
