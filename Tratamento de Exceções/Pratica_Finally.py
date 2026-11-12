try:
    numero =int("A")
    print(numero)
except ValueError:
    print("Ocorreu um erro de conversão")
finally:
    print("Execução Finalizada")
    