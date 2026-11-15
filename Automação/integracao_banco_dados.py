import sqlite3

from pathlib import Path as PATH

ROOT_PATH = PATH(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "dados.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
nome TEXT,
idade INTEGER
)
''')

conn.commit()

print("Tabela 'usuarios' criada com sucesso.")