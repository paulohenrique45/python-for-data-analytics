#Lendo Json

from pathlib import Path

ROOT_PATH = Path(__file__).parent

import json

with open(ROOT_PATH / "usuario.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)