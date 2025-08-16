"""Definition of Group class for vertically stacking grouped `Block` instances."""

from typing import Optional

from .block import Block


class Series(Block):
    """Series configuration of `Block` instances for horisontal grouping.

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
            "inner sep=0pt",
        ]
    )

    def __init__(
        self,
        blocks: list["Block"],
        text: str = "",
        color: str = "white",
        parent: Optional["Block"] = None,
    ) -> None:
        Block.__init__(self, text, color, parent)

        self.blocks = blocks
        self.blocks[0].id = f"{self.id}+0"
        for i, (block, new_parent) in enumerate(
            zip(self.blocks[1::], self.blocks[0:-1]), start=1
        ):
            block.parent = new_parent
            block.id = f"{self.id}+{i}"

    def get_node(self, connector_position: float = 0.25) -> str:
        """Get TikZ node string."""

        block_nodes = "\n".join(
            block.get_node(connector_position) for block in self.blocks
        )
        series_node = " ".join(
            [
                f"\\node[{self.tikz_options}]",
                f"({self.id})",
                self.position,
                "{\\begin{tikzpicture}\n",
                block_nodes,
                "\\end{tikzpicture}};\n",
                self.arrow(connector_position),
                r"\begin{pgfonlayer}{background}",
                f"\\coordinate (sw) at ($({self.id}.south west)+(-1mm, -1mm)$);",
                f"\\coordinate (nw) at ($({self.id}.north west)+(-1mm, 1mm)$);",
                f"\\coordinate (ne) at ($({self.id}.north east)+(1mm, 1mm)$);",
                f"\\coordinate (n) at ($({self.id}.north)+(0mm, 1mm)$);",
                f"\\draw[{self.color}, thick] (sw) rectangle (ne);",
                f"\\draw[{self.color}, fill={self.color}!50, thick] (nw)",
                r"rectangle ($(ne)+(0, 0.5cm)$);",
                f"\\node[anchor=south] at (n) {{{self.text}}};",
                r"\end{pgfonlayer}",
            ]
        )
        return series_node
