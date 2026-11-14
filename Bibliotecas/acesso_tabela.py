import pandas as pd

from pathlib import Path

ROOT_PATH = Path(__file__).parent

visualizar = pd.read_csv(ROOT_PATH / 'tabela_produtos.csv')
print(visualizar["produto"])

# Operação estatística

# valor médio dos produtos
print("Valor médio dos produtos:", visualizar["preco"].mean())

#contagem de produtos
print("contagem de produtos:", visualizar["quantidade"].count())

#descrição estatística
print("Descrição estatística:", visualizar.describe())
