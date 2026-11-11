# Importa a biblioteca sqlite3 para trabalhar com bancos de dados SQLite.
import sqlite3

# Importa a classe Path para manipular caminhos de arquivos e pastas.
from pathlib import Path

# Define a pasta raiz do arquivo atual como referência para os arquivos do projeto.
ROOT_PATH = Path(__file__).parent

# Cria uma conexão com o banco de dados SQLite localizado na pasta raiz.
conexao = sqlite3.connect(ROOT_PATH / 'dados.db')

# Cria um cursor para executar comandos SQL no banco de dados.
cursor = conexao.cursor()

# Executa um comando SQL para criar a tabela 'usuarios' com os campos 'nome' e 'idade'.
cursor.execute("""
CREATE TABLE usuarios (
    nome TEXT,
    idade INTEGER
)
""")

# Salva as alterações realizadas no banco de dados.
conexao.commit()