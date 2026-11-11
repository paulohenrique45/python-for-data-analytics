#lendo um CSV

from pathlib import Path

ROOT_PATH = Path(__file__).parent

import csv

with open(ROOT_PATH / "cadastros.csv", "r") as arquivo:
    leitor_csv = csv.reader(arquivo)
    
    for linha in leitor_csv:
        print(linha)