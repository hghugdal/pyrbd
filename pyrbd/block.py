"""Module containing Block class definition."""

from typing import Optional


class Block:
    """Block entering a reliability block diagram.

    Parameters
    ----------
    text : str
        block text string
    color : str
        block color
    parent : Block, optional
        parent `Block` instance
    shift : tuple[float, float], optional
        additional position shift `(x, y)` relative to `parent` `Block` instance

    Attributes
    ----------
    text : str
        block text string
    color : str
        block color
    parent : Block | None
        parent `Block` instance or `None`
    shift : tuple[float, float]
        additional position shift relative to `parent` `Block` instance
    position : str
        string defining the block position
    options : str
        TikZ node formatting options

    """

    options: str = ", ".join(
        [
            "anchor=west",
            "align=center",
            "fill={fill_color}",
            "draw=black",
            "minimum height=1cm",
            "rounded corners=1mm",
        ]
    )

    def __init__(
        self,
        text: str,
        color: str,
        parent: Optional["Block"] = None,
        shift: tuple[float, float] = (0.0, 0.0),
    ) -> None:
        self.text = text
        self.color = color
        self.parent = parent
        self.shift = shift
        self.id: int = self.parent.id + 1 if self.parent is not None else 1

    @property
    def position(self) -> str:
        """Block position."""

        if self.parent is None:
            return ""

        return f"[right=of {self.parent.id}, xshift={self.shift[0]}cm, yshift={self.shift[1]}cm]"

    @property
    def arrow(self) -> str:
        """Get TikZ arrow string."""

        if self.parent is None:
            return ""

        return " ".join(
            [
                "\\draw[thick, rectangle connector=0.5cm]",
                f"({self.parent.id}.east) to ({self.id}.west);\n",
            ]
        )

    def get_node(self) -> str:
        """Get TikZ node string."""

        node = " ".join(
            [
                f"\\node[{self.options.format(fill_color=self.color)}]",
                f"({self.id})",
                self.position,
                f"{{{self.text}}};\n",
                self.arrow,
            ]
        )
        return node
