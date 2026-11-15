import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"


dados = pd.read_csv(url)

#valores ausentes nas colunas
# print(dados.isnull().sum())

# dados_limpos = dados.dropna() #remove linhas com valores nulos

# print(dados_limpos.isnull().sum()) #verifica se ainda existem valores nulos

# print(dados_limpos.head())


# Preenche os valores ausentes da coluna "Age" com a média das idades.
# Assim, registros com idade faltante continuam no conjunto de dados,
# mas recebem um valor estimado que mantém a consistência da análise.
dados["Age"] = dados["Age"].fillna(dados["Age"].mean())

# Verifica quantos valores nulos restaram na coluna "Age".
# Se o resultado for 0, significa que todos os dados faltantes foram preenchidos.
print(dados["Age"].isnull().sum())