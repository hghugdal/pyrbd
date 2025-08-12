"""Simple RBD example."""

from os import path, chdir

from pyrbd import Block, Diagram

chdir(path.dirname(__file__))

pt = Block("Pressure transmitter", "blue!30", parent=None)
logic = Block("Logic incl. IO", "gray", parent=pt)
valve1 = Block(r"Valve\\ CLOSED", "yellow!50", parent=logic, shift=(0, 1))
valve2 = Block(r"Valve\\ CLOSED", "yellow!50", parent=logic, shift=(0, -1))


diag = Diagram("example_RBD", blocks=[pt, logic, valve1, valve2], hazard="Overpressure")
diag.write()
diag.compile()
