# w refere-se a escrita, se o arquivo não existir ele será criado, caso exista ele será sobrescrito
# with open ("relatorio.txt","w") as arquivo:
#     arquivo.write("Relatorio de Vendas\n")
#     arquivo.write("Total:1500")

#a refere-se a escrita, se o arquivo não existir ele será criado, caso exista ele será sobrescrito
with open ("relatorio.txt","a") as arquivo:
    arquivo.write("\nNovo registro adicionado")
