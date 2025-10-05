import nbformat
from pathlib import Path

path = Path(r"c:\Users\MadScie254\Documents\GitHub\Stats_CAT_2.1\MSTA_6102_CAT_Stats.ipynb")
nb = nbformat.read(path, as_version=4)
for cell in nb.cells:
    print(repr(cell.get('id')), cell.cell_type, len(cell.source))
