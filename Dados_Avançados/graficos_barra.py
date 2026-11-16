import pandas as pd
import matplotlib.pyplot as plt

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

dados = pd.read_csv(url)

plt.figure(figsize=(8,5))

plt.bar(dados["day"],dados["tip"], color="green")

plt.title("Gorjetas do dia")
plt.xlabel("Dia")
plt.ylabel("Gorjeta")

plt.show()