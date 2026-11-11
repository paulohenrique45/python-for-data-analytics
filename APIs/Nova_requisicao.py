import json
import requests

from pathlib import Path

ROOT_PATH = Path(__file__).parent

url = "https://api.agify.io?name=ana"

resposta = requests.get(url)

dados = resposta.json()

with open(ROOT_PATH / "dados_api.json", "w") as arquivo:
    json.dump(dados, arquivo)