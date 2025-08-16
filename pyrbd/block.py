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
    parent : Optional[Block]
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
    id : str
        block identifier string
    shift : tuple[float, float]
        additional position shift relative to `parent` `Block` instance
    position : str
        string defining the block position
    tikz_options : str
        TikZ node formatting options


    Examples
    --------
    >>> block_1 = Block("Start", "green")
    >>> block_1.id
    '1'
    >>> block_2 = Block("End", "red", parent=block_1)
    >>> block_2.id
    '2'
    """

    tikz_options: str = ", ".join(
        [
            "anchor=west",
            "align=center",
            "fill={fill_color}",
            "draw=black",
            "minimum height=1cm",
            "rounded corners=0.3mm",
            "inner sep=4pt",
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
        self.id: str = str(int(self.parent.id) + 1) if self.parent is not None else "1"

    @property
    def position(self) -> str:
        """Block position."""

        if self.parent is None:
            return ""

        return f"[right={0.5 + self.shift[0]}cm of {self.parent.id}, yshift={self.shift[1]}cm]"

    def arrow(self, connector_position: float) -> str:
        """Get TikZ arrow string."""

        if self.parent is None:
            return ""

        return " ".join(
            [
                f"\\draw[thick, rectangle connector={connector_position}cm]",
                f"({self.parent.id}.east) to ({self.id}.west);\n",
            ]
        )

    def get_node(self, connector_position: float = 0.25) -> str:
        """Get TikZ node string."""

        node = " ".join(
            [
                f"\\node[{self.tikz_options.format(fill_color=self.color)}]",
                f"({self.id})",
                self.position,
                f"{{{self.text}}};\n",
                self.arrow(connector_position),
            ]
        )
        return node
