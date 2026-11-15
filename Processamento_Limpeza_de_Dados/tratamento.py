# Importa a biblioteca pandas para trabalhar com dados tabulares
import pandas as pd

# URL do dataset Titanic disponível em um repositório público no GitHub
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Lê o arquivo CSV diretamente da URL e armazena os dados em um DataFrame
# DataFrame é a estrutura principal da biblioteca pandas para manipulação de dados
dados = pd.read_csv(url)

# Exibe as primeiras 10 linhas do DataFrame para inspecionar os dados
print(dados.head(10))

# Mostra informações gerais sobre o DataFrame, como:
# - quantidade de linhas e colunas
# - nomes das colunas
# - tipos de dados de cada coluna
# - presença de valores nulos
print(dados.info())

# Exibe estatísticas descritivas das colunas numéricas, como:
# média, desvio padrão, mínimo, quartis e máximo
print(dados.describe())
