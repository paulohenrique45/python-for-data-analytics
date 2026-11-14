import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "produto": ['notebook', 'mouse', 'teclado', 'monitor'],
    "preco": [2500.00, 150.00, 300.00, 800.00],
}

visualizacao = pd.DataFrame(dados)
print(visualizacao.groupby("produto").mean())

plt.bar(visualizacao["produto"], visualizacao["preco"])
plt.xlabel("Produto")
plt.ylabel("Preço")
plt.title("Preço dos Produtos")
plt.show()