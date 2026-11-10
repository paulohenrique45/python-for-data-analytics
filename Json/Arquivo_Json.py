import json


dados = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "Sao Paulo"
}


with open('usuario.json', 'w') as arquivo:
    json.dump(dados, arquivo)