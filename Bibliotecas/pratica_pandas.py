import pandas as pd

# Dicionário com os dados que serão transformados em um DataFrame
# Cada chave representa uma coluna e cada lista representa os valores dessa coluna
# 
# Exemplo:
# 'Nome' -> ['Alice', 'Bob', 'Charlie', 'David']
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']
}

# Criação do DataFrame a partir do dicionário 'dados'
df = pd.DataFrame(dados)

# Exibe o DataFrame original no console
print("DataFrame original:")
print(df)