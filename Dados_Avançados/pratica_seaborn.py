import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

dados = pd.read_csv(url)

sns.scatterplot(data=dados,x="total_bill",y="tip")

plt.show()