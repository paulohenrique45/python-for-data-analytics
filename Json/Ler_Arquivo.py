#Lendo Json

import json

with open('usuario.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)