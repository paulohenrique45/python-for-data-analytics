import sqlite3

from pathlib import Path as PATH

ROOT_PATH = PATH(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "dados.db")

cursor = conn.cursor()

cursor.execute(
    "insert into usuarios values(?, ?)",
    ("Henrique", 33)
)
cursor.execute(
    "insert into usuarios values(?, ?)",
    ("Maria", 28)
)

conn.commit()

print("Usuário inserido com sucesso.")