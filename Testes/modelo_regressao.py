# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -----------------------------------------------------------------------------
# 1) Carregamento dos dados
# -----------------------------------------------------------------------------
# URL do dataset de imóveis usado para treino do modelo de regressão linear
url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
dados = pd.read_csv(url)

# Exibe as primeiras linhas do DataFrame para inspecionar os dados
print(dados.head())

# -----------------------------------------------------------------------------
# 2) Limpeza e preparação dos dados
# -----------------------------------------------------------------------------
# Remove linhas com valores ausentes para evitar erros no treinamento do modelo
dados = dados.dropna()

# Seleciona as variáveis explicativas (features) e a variável alvo
# A coluna 'median_house_value' será a variável que queremos prever
x = dados.drop("median_house_value", axis=1)
y = dados["median_house_value"]

# Converte variáveis categóricas em colunas binárias (one-hot encoding)
# Isso permite que o modelo scikit-learn trabalhe com dados categóricos
x = pd.get_dummies(x)

# -----------------------------------------------------------------------------
# 3) Divisão dos dados em treino e teste
# -----------------------------------------------------------------------------
# Separa os dados em conjunto de treino e teste
# test_size=0.2 -> 20% dos dados são usados para teste
# random_state=42 -> garante reprodutibilidade
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
)

# -----------------------------------------------------------------------------
# 4) Criação e treinamento do modelo
# -----------------------------------------------------------------------------
# Instancia o modelo de regressão linear
model = LinearRegression()

# Ajusta o modelo aos dados de treinamento
model.fit(x_train, y_train)

# -----------------------------------------------------------------------------
# 5) Previsão e análise dos resíduos
# -----------------------------------------------------------------------------
# Gera previsões para os dados de teste
y_pred = model.predict(x_test)

# Calcula os resíduos = diferença entre valor real e valor previsto
# Se o modelo estiver bom, os resíduos devem estar distribuídos aleatoriamente
residuos = y_test - y_pred

# -----------------------------------------------------------------------------
# 6) Visualização dos resíduos
# -----------------------------------------------------------------------------
# Cria a figura do gráfico
plt.figure(figsize=(6, 5))

# Scatter plot: resíduos em função dos valores previstos
plt.scatter(y_pred, residuos)

# Linha horizontal em zero para facilitar a interpretação
plt.axhline(0, color='red')

# Configuração dos eixos e do título
plt.xlabel("Valores Preditos")
plt.ylabel("Resíduos")
plt.title("Resíduos vs Valores Preditos")

# Exibe o gráfico
plt.show()
