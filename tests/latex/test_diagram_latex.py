"""Tests for `Diagram` class."""

from os import chdir
from pathlib import Path

import pytest

from pyrbd import Block, Diagram, config


@pytest.fixture(name="diagram")
def diagram_fixture(source_dir: str, output_dir: str) -> Diagram:
    """Diagram pytest fixture."""

    config.SOURCE_DIR = source_dir

    block1 = Block("block1", "white")
    block2 = Block("block2", "white")
    block3 = Block("block3", "white")
    return Diagram(
        "test_diagram_compile", [block1, block2, block3], "Overpressure", output_dir=output_dir
    )


def test_diagram_compile(tmp_path: Path, diagram: Diagram) -> None:
    """Test `Diagram` `write` method."""

    temp_dir = tmp_path / "test_diagram_compile"
    temp_dir.mkdir()
    chdir(temp_dir)

    with pytest.raises(FileNotFoundError):
        diagram.compile()

    diagram.write()
    assert ".pdf" in "\n".join(diagram.compile(clear_source=False))
    assert ".svg" in "\n".join(diagram.compile("svg", clear_source=False))
    assert ".png" in "\n".join(diagram.compile("png", clear_source=False))
    assert ".pdf" not in "\n".join(diagram.compile(["svg", "png"], clear_source=False))
    assert ".pdf" in "\n".join(diagram.compile(["pdf", "svg"]))

    diagram.write()
    output_files = diagram.compile(["pdf", "svg", "png"])

    for file in output_files:
        assert Path(file).is_file()
        assert Path(file).exists()
