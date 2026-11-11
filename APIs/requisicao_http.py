import requests

url = "https://api.agify.io?name=ana"

resposta = requests.get(url)

print(resposta.status_code)
print(resposta.text)