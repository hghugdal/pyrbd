# <img alt="pyRBDlogo" src=images/logo.svg width=50 align=top> pyRBD

<img alt="Python" src="https://img.shields.io/badge/Python-3.11, 3.12, 3.13-blue?logo=python&link=None"> <img alt="Tests" src="https://img.shields.io/badge/Tests-Passing-darkgreen?logo=pytest&link=None"> <img alt="Coverage" src="https://img.shields.io/badge/Coverage-100%25-darkgreen?link=None"> <img alt="Pylint" src="https://img.shields.io/badge/Pylint-10%2F10-darkgreen?link=None">

A Python package for creating simple reliability block diagrams (RBDs) using `LaTeX` and [`TikZ`](https://en.wikipedia.org/wiki/PGF/TikZ).

## Dependencies
`pyRBD` requires a working installation of `LaTeX` including [`latexmk`](https://ctan.org/pkg/latexmk/).

## Simple example diagram
The blocks of the RBD are defined using `Block`, `Series` and `Group`, and the diagram itself is handled by the `Diagram` class. A simple example is given by the code
```python
from pyrbd import Block, Diagram

start_block = Block("Start", "blue!30", parent=None)
parallel = 2 * Block("Parallel blocks", "gray", parent=start_block)
end_block = Block("End", "green!50", parent=parallel)

diagram = Diagram(
    "simple_RBD",
    blocks=[start_block, parallel, end_block],
)
diagram.write()
diagram.compile()
```
producing the following diagram

<img src="examples/simple_RBD.png" width=600>
