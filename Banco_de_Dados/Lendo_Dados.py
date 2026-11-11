import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'dados.db')

cursor = conexao.cursor()

cursor.execute("select *from usuarios")

dados = cursor.fetchall()

print(dados)