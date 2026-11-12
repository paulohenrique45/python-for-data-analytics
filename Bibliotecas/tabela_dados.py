import pandas as pd

from pathlib import Path

ROOT_PATH = Path(__file__).parent

dados ={
    "produto": ['Arroz', 'Feijão', 'Macarrão', 'Açúcar'],
    "preco": [5.50, 7.20, 4.30, 3.80],
    "quantidade": [10, 15, 20, 25]
}

df = pd.DataFrame(dados)

df.to_csv(ROOT_PATH / 'tabela_produtos.csv', index=False)

visualizar = pd.read_csv(ROOT_PATH / 'tabela_produtos.csv')
print(visualizar)


