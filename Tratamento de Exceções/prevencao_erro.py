# Solicita ao usuário que digite um número.
numero = input("Digite um número: ")

# Verifica se o valor informado contém apenas dígitos.
if numero.isdigit():
    # Converte o texto para inteiro e exibe o número.
    numero = int(numero)
    print(f"O número digitado é: {numero}")

else:
    # Informa quando o valor digitado não é válido.
    print("Valor inválido.")
