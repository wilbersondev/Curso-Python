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

def cadastro():
    nome = input("Digite o nome do cliente: ")
    dados = input("Digite o CNPJ do cliente: ")
    print("Cliente cadastrado:", nome)
    cursor.execute(
        "INSERT INTO cliente (nome, cnpj) VALUES (?, ?)",
        (nome, dados)
    )
    conexao.commit()
def listar():
    cursor.execute("SELECT * FROM cliente")
    resultado = cursor.fetchall()
    for cliente in resultado:
        print("ID:", cliente[0])
        print("Nome:", cliente[1])
        print("CNPJ:", cliente[2])


while True:
    print("=== SISTEMA DE CLIENTES ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")    
    print("3 - Sair")

    codigo = input("Digite o código de 1 a 3: ")

    if codigo == "1":
        cadastro()

    if codigo == "2":
        listar()

    if codigo == "3":
        print(" encerrando o programa")
        break
     