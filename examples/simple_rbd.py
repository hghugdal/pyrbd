"""Simple RBD example."""

from os import path, chdir

from pyrbd import Block, Group, Diagram

chdir(path.dirname(__file__))

pt = Block("Pressure transmitter", "blue!30", parent=None)
logic = Block("Logic incl. IO", "gray", parent=pt)
valve1 = Block(r"Valve\\ CLOSED", "yellow!50")
valve2 = Block(r"Valve\\ CLOSED", "yellow!50")
valve3 = Block(r"Valve\\ CLOSED", "yellow!50")
valve4 = Block(r"Valve\\ CLOSED", "yellow!50")
valves = Group([valve1, valve2, valve3, valve4], parent=logic)
psd = Block("Valves shut OFF", "green!50", parent=valves)


diag = Diagram("example_RBD", blocks=[pt, logic, valves, psd], hazard="Overpressure")
diag.write()
diag.compile()
