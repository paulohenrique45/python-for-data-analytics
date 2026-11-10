#lendo um CSV

import csv

with open('cadastros.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    
    for linha in leitor_csv:
        print(linha)