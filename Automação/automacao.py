import csv

from pathlib import Path as PATH

ROOT_PATH = PATH(__file__).parent

total = 0

with open(ROOT_PATH / "data.txt", "w") as file:
    file.write("100\n200\n150\n300")

with open(ROOT_PATH / "data.txt", "r") as file:
    for line in file:
        valor = int(line.strip())
        total += valor

print(f"Total de vendas: {total}")

