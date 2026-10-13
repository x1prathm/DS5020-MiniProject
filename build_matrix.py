import json
import os
from pathlib import Path

os.environ["MPLBACKEND"] = "Agg"

from IPython.display import display

project = Path(__file__).resolve().parent
os.chdir(project)

with open(project / "analysis.ipynb", encoding="utf-8") as file:
    notebook = json.load(file)

scope = {"__name__": "__main__", "display": display}

for number, cell in enumerate(notebook["cells"], start=1):
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])

        if source.strip():
            print(f"Running notebook cell {number}...")
            exec(compile(source, f"notebook_cell_{number}", "exec"), scope)

print("MATRIX REBUILT SUCCESSFULLY.")
