"""Simple RBD example."""

from os import path, chdir

from pyrbd import Block, Group, Series, Diagram

chdir(path.dirname(__file__))

pt = Block("Pressure transmitter", "blue!30", parent=None)
logic = 2 * Block("Logic incl. IO", "gray", parent=pt)
actuator1 = Block(r"Actutator 1", "yellow!50")
actuator2 = Block(r"Actutator 2", "yellow!50")
valve1 = Block(r"Valve 1\\ CLOSED", "yellow!50")
valve2 = Block(r"Valve 2\\ CLOSED", "yellow!50")
valves = Group(
    [actuator1 + valve1, actuator2 + valve2],
    parent=logic,
    text="Valve group",
    color="yellow",
)
valve3 = Block(r"Valve\\ CLOSED", "orange!50")
valve4 = Block(r"Valve\\ CLOSED", "orange!50")
series = Series([valve3, valve4], "Valve series", "orange", parent=valves)
psd = Block("Valves shut OFF", "green!50", parent=series)


diag = Diagram(
    "example_RBD", blocks=[pt, logic, valves, series, psd], hazard="Overpressure"
)
diag.write()
diag.compile()
