"""Simple RBD example."""

from os import path, chdir

from pyrbd import Block, Group, Series, Diagram

chdir(path.dirname(__file__))

pt = Block("Pressure transmitter", "blue!30", parent=None)
logic = Block("Logic incl. IO", "gray", parent=pt)
valve1 = Block(r"Valve 1\\ CLOSED", "yellow!50")
valve2 = Block(r"Valve 2\\ CLOSED", "yellow!50")
valve3 = Block(r"Valve 3\\ CLOSED", "yellow!50")
valve4 = Block(r"Valve 4\\ CLOSED", "yellow!50")
valves = Group([valve1, valve2, valve3, valve4], parent=logic)
valve5 = Block(r"Valve 5\\ CLOSED", "yellow!50")
valve6 = Block(r"Valve 6\\ CLOSED", "yellow!50")
series = Series([valve5, valve6], "Valve block", "yellow", parent=valves)
psd = Block("Valves shut OFF", "green!50", parent=series)


diag = Diagram(
    "example_RBD", blocks=[pt, logic, valves, series, psd], hazard="Overpressure"
)
diag.write()
diag.compile()
