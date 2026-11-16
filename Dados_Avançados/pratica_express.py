import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

dados = pd.read_csv(url)

fig = px.scatter(
    dados,
    x="total_bill",
    y="tip",
    color = "day",
    title="Relação entre conta e gorjeta"
)
fig.show()

