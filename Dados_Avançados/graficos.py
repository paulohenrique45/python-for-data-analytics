import pandas as pd
import matplotlib.pyplot as plt

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

dados = pd.read_csv(url)

plt.scatter(dados["total_bill"],dados["tip"])

plt.xlabel("Conta total")
plt.ylabel("Valor da gorjeta")
plt.title("Gráfico conta x gorjeta")

plt.show()



