import nbformat

nb = nbformat.read('MSTA6102_CAT_Solutions.ipynb', as_version=4)
code_cells = [cell for cell in nb.cells if cell.get('cell_type') == 'code']

for idx, cell in enumerate(code_cells[:5], start=1):
    print(f"Code cell {idx}:\n{cell['source']}\n{'-'*40}")
