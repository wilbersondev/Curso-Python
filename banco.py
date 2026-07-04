import sqlite3
conexao = sqlite3.connect("cliente.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id   INTEGER PRIMARY KEY,
        nome TEXT,
        cnpj TEXT
    )
""")
conexao.commit()
cursor.execute(
    "INSERT INTO cliente (nome, cnpj) VALUES (?, ?)",
    ("Lucas", "12345678901234")
)
conexao.commit()
cursor.execute("SELECT * FROM cliente")
resultado = cursor.fetchall()
print(resultado)
conexao.close() 