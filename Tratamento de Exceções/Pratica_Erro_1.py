#Exemplo de erro
try:
    numero = 10/0
    print(numero)
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")        