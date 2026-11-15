import sqlite3

from pathlib import Path as PATH

ROOT_PATH = PATH(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "dados.db")

cursor = conn.cursor()

cursor.execute("select * from usuarios")

dados = cursor.fetchall()

print("Usuários no banco de dados:")

for usuario in dados:
    print(usuario)


conn.close()
print("Conexão com o banco de dados encerrada.")