import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

dados = pd.read_csv(url)

def limpar_dados(dados):
    dados["Age"].fillna(dados["Age"].mean(), inplace=True)

    dados["Fare_nomalized"] = (
        dados["Fare"] - dados["Fare"].min()
        ) / (dados["Fare"].max() - dados["Fare"].min())
    
    return dados

dados_limpos = limpar_dados(dados)
print(dados_limpos.head())