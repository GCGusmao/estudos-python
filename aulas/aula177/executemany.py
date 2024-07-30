import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Create table

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

# Register values in table
# CUIDADO: sql injection

# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (id, name, weight) '
#     'VALUES '
#     '(NULL, "Gustavo Gusmão", 9.9), (NULL, "Eduardo", 10)'
# )

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)
# cursor.executemany(
#     sql,
#     (
#         ('Joana', 4), ('Luiz', 5), ('Mateus', 10)
#     )
# )

cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
cursor.executemany(sql, (
    {'nome': 'João', 'peso': 3},
    {'nome': 'Maria', 'peso': 9},
    {'nome': 'Antonio', 'peso': 7},
    {'nome': 'Rita', 'peso': 4},
))
connection.commit()

cursor.close()
connection.close()
if __name__ == '__main__':
    print(sql)
