from pathlib import Path
import os

BASE_DIR = Path(__file__).parent

path_output = BASE_DIR.parent / "project" / "output" / "report.txt"

os.makedirs(path_output.parent, exist_ok=True)

with open(path_output, "a") as report:
    report.write("Report generated successfully\n")