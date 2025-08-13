"""Definition of Group class for vertically stacking grouped `Block` instances."""

from typing import Optional

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

    def __init__(
        self, blocks: list["Block"], parent: Optional["Block | Group"] = None
    ) -> None:
        Block.__init__(self, "", "", parent)

        self.blocks = blocks
        for i, (block, shift) in enumerate(zip(self.blocks, self.shifts)):
            block.shift = (0.5, shift)
            block.parent = parent
            block.id = f"{self.id}-{i}"

    @property
    def shifts(self) -> list[float]:
        """List of vertical position shifts for each `Block` instance in group."""

        n_blocks = len(self.blocks)

        return list(
            self.shift_scale
            * linspace(-n_blocks / 2, n_blocks / 2, n_blocks, dtype="float")
        )

    @property
    def arrows(self) -> str:
        """Get TikZ arrow string."""

        return "\n".join(
            [
                " ".join(
                    [
                        "\\draw[thick, rectangle line]",
                        f"({block.id}.east) to ({self.id});\n",
                    ]
                )
                for block in self.blocks
            ]
        )

    def get_node(self, connector_position: float = 0.5) -> str:
        """Get TikZ node string."""

        block_nodes = "\n".join(
            block.get_node(connector_position) for block in self.blocks
        )
        group_node = " ".join(
            [
                f"\\coordinate ({self.id}) at",
                f"($({self.blocks[0].id}.east)!0.5!({self.blocks[-1].id}.east) + (0.5cm, 0)$);",
                "\n",
            ]
        )
        return block_nodes + group_node + self.arrows
