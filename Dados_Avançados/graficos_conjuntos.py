import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

dados = pd.read_csv(url)

fig,ax = plt.subplots(1,2, figsize=(10,4))

sns.histplot(dados["total_bill"],ax=ax[0])
ax[0].set_title("Distribuição da Conta")

sns.boxplot(data=dados, x="day", y="tip", ax=ax[1])
ax[1].set_title("Gorjeta por dia")

plt.show()