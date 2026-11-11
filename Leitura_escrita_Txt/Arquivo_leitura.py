from pathlib import Path

ROOT_PATH = Path(__file__).parent

#Leitura de arquivos
#read lê todo o conteúdo do arquivo
with open (ROOT_PATH / "dados.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# quando uso o for ele processa o arquivo linha por linha, e não lê todo o conteúdo de uma vez
with open (ROOT_PATH / "dados.txt","r") as arquivo:
    for linha in arquivo:
# strip() remove os espaços em branco do início e do fim da linha
        print(linha.strip())


