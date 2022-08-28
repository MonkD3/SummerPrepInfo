import os
import pathlib

cwd = os.getcwd()
path = pathlib.Path(cwd)

files = {"philo-concepts.txt", "info-data-structure.txt", "philo-theorie.txt", "info-tuyaux.txt", "info-projet.py"}

for file in files:
    for f in path.glob(f"**/{file}"):
        os.remove(f)