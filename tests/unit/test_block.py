"""Tests for classes in block.py"""

from copy import deepcopy

from pyrbd import Block, Series, Group


def test_block() -> None:
    """Test `Block` __init__ and properties."""

    block = Block("Block", "blue")
    assert block.id == "1"
    assert block.position == ""
    assert block.arrow(0.5) == ""

    child = Block("Child", "green", shift=(0.5, 2), parent=block)
    assert child.id == "2"
    assert child.position == "[right=1.0cm of 1, yshift=2cm]"
    assert (
        "\\draw[thick, rectangle connector=0.5cm](1.east) to (2.west);"
        in child.arrow(0.5)
    )

    node = child.get_node()
    assert "green" in node
    assert "Child" in node


def test_series() -> None:
    """Test `Series` __init__ and properties."""

    block_1 = Block("Block 1", "blue")
    block_2 = Block("Block 2", "green")
    series = Series([block_1, block_2])

    assert series.id == "1"
    assert series.parent is None

    assert block_1.id == "1+0"
    assert block_2.id == "1+1"
    assert block_1.parent is None
    assert block_2.parent is block_1

    assert series.background == ""
    assert series.label == ""

    series_node = Series([block_1, block_2], "Series label", "gray", parent=series)

    assert series_node.id == "2"
    assert "gray" in series_node.background
    assert "gray" in series_node.label and "Series label" in series_node.label

    for color in ["blue", "green", "gray"]:
        assert color in series_node.get_node()


def test_add() -> None:
    """Tests for __add__ for `Block` class."""

    block = Block("block", "white")

    assert isinstance(series := block + deepcopy(block), Series)
    assert len(series.blocks) == 2


def test_mul() -> None:
    """Tests for __mul__ for `Block` class."""

    block = Block("block", "white")

    assert isinstance(group := 3 * block, Group)
    assert len(group.blocks) == 3

    assert isinstance(group := block * 2, Group)
    assert len(group.blocks) == 2
