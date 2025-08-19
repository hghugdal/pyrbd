"""Definition of Group class for vertically stacking grouped `Block` instances."""

from typing import Optional
from itertools import combinations

from numpy import linspace

from .block import Block


class Group(Block):
    """Group of `Block` instances for vertical stacking.

    Parameters
    ----------
    blocks : list[Block]
        list of `Block` instances
    parent : Block, optional
        parent `Block` instance
    """

    shift_scale = 0.8
    tikz_options: str = ", ".join(
        [
            "anchor=west",
        ]
    )

    def __init__(self, blocks: list["Block"], parent: Optional["Block"] = None) -> None:
        Block.__init__(self, "", "", parent)

        self.blocks = blocks
        for i, (block, shift) in enumerate(zip(self.blocks, self.shifts)):
            block.shift = (0, shift)
            block.parent = self
            block.id = f"{self.id}-{i}"

    @property
    def shifts(self) -> list[float]:
        """List of vertical position shifts for each `Block` instance in group."""

        n_blocks = len(self.blocks)

        return list(
            self.shift_scale
            * linspace(n_blocks / 2, -n_blocks / 2, n_blocks, dtype="float")
        )

    @property
    def position(self) -> str:
        """Group position."""

        if self.parent is None:
            return ""

        return f"[right=0.5cm of {self.parent.id}, xshift=0.0cm]"

    def arrow(self, connector_position: float) -> str:
        """Get TikZ arrow string."""

        if self.parent is None:
            return ""

        return f"\\draw[thick] ({self.parent.id}.east) to ({self.id}.west);\n"

    @property
    def arrows(self) -> str:
        """Get TikZ arrow string."""

        return "\n".join(
            [
                " ".join(
                    [
                        "\\draw[thick, rectangle line]",
                        f"({block1.id}.east) to ({block2.id}.east);\n",
                    ]
                )
                for (block1, block2) in combinations(self.blocks, 2)
            ]
        )

    def get_node(self, connector_position: float = 0.0) -> str:
        """Get TikZ node string."""

        block_nodes = "\n".join(
            block.get_node(connector_position) for block in self.blocks
        )

        group_node = "".join(
            [
                f"\\node[anchor=west, outer sep=0pt, inner sep=0pt, align=center] ({self.id}) ",
                self.position,
                "{\\begin{tikzpicture}\n",
                f"\\coordinate ({self.id}) at (0, 0);\n",
                block_nodes,
                self.arrows,
                "\\end{tikzpicture}};\n\n",
                self.arrow(connector_position),
            ]
        )

        return group_node
