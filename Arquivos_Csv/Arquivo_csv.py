# Criando arquivo CSV
# Este script cria um arquivo .csv com uma tabela de dados.
# O módulo csv do Python facilita a escrita de arquivos CSV de forma organizada.

import csv

# Lista de listas contendo os dados que serão gravados no arquivo CSV.
# A primeira linha representa o cabeçalho da tabela:
# Nome, Idade e Cidade.
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Maria", 28, "Belo Horizonte"]
]

# Abre o arquivo "cadastros.csv" em modo de escrita ("w").
# O parâmetro newline="" evita que o Python insira quebras de linha extras
# em sistemas diferentes, como Windows.
with open("cadastros.csv", "w", newline="") as arquivo:
    # Cria um objeto writer do módulo csv para escrever no arquivo.
    # Esse objeto é responsável por formatar os dados em CSV.
    writer = csv.writer(arquivo)

    # Escreve todas as linhas da lista 'dados' no arquivo.
    # A função writerows() recebe uma lista de listas e grava cada lista
    # como uma linha do arquivo CSV.
    writer.writerows(dados)

# Funcionalidades:
# - import csv: importa a biblioteca que permite manipular arquivos CSV.
# - dados: armazena as informações em formato tabular.
# - open(..., "w"): abre o arquivo para escrita.
# - csv.writer(...): cria o escritor CSV.
# - writer.writerows(...): grava todas as linhas de dados no arquivo. 
# O resultado será um arquivo chamado cadastros.csv com o conteúdo:
# Nome,Idade,Cidade
# Ana,25,São Paulo
# Carlos,30,Rio de Janeiro
# Maria,28,Belo Horizonte

