import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

dados = pd.read_csv(url)

def validar_dataset(dados):

    print("Linhas: ",dados.shape[0])
    print("Colunas: ",dados.shape[1])
    print("\nValores ausentes:")
    print(dados.isnull().sum())

resultados = validar_dataset(dados)
print(resultados)