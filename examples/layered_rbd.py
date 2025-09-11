"""Example with layered Series and Group instances."""

from os import path, chdir
from copy import deepcopy

from pyrbd import Block, Group, Series, Diagram

chdir(path.dirname(__file__))

# Define the blocks comprising the diagram
start_block = Block("Start", "blue!30")
block = Block("Block", "gray")
group_1 = Group(
    [deepcopy(b) + deepcopy(b) for b in 3 * [block]],
    text="Group with Series",
    color="orange",
    parent=start_block,
)
series_1 = Series(
    [deepcopy(block), 2 * deepcopy(block)],
    text="Series with Group",
    color="red",
    parent=group_1,
)
series_2 = Series(
    [2 * deepcopy(block), deepcopy(block), 3 * (deepcopy(block) + deepcopy(block))],
    text="Series with mixed Groups",
    color="RoyalBlue",
    parent=series_1,
)
group_2 = Group(
    [
        deepcopy(block) + deepcopy(block) + deepcopy(block),
        deepcopy(block),
        deepcopy(block) + deepcopy(block) + deepcopy(block) + deepcopy(block),
    ],
    text="Group with mixed Series",
    color="red",
    parent=series_2,
)
end_block = Block("End", "green!50", parent=group_2)

# Define and compile the diagram
diagram = Diagram(
    "layered_RBD",
    blocks=[start_block, group_1, series_1, series_2, group_2, end_block],
)
diagram.write()
diagram.compile(["pdf", "svg"])
