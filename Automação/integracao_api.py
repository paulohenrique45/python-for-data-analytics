import requests


url = "https://api.agify.io?name=Maria"

resposta = requests.get(url)

dados = resposta.json()

print(dados)