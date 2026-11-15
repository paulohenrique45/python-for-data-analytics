import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

dados = pd.read_csv(url)

dados["Age_log"] = dados["Age"].apply(lambda x:x)

print(dados["Age_log"])

