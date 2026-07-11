import tkinter as tk
import sqlite3
from tkinter import messagebox


# CONEXÃO COM O BANCO DE DADOS
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

# CRIA JANELA PRINCIPAL
janelas = tk.Tk()
janelas.title("Sistema De Clientes")
janelas.geometry("500x400")
label = tk.Label(janelas, text="Nome do Clintes: ")
label.pack()
entry = tk.Entry(janelas)
entry.pack()
label2 = tk.Label(janelas, text="CNPJ do CLientes:")
label2.pack()
entry2 = tk.Entry(janelas)
entry2.pack()
# A TABELA E CRIADA FORA DA FUNÇÃO
from tkinter import ttk
tabela = ttk.Treeview(janelas, columns=("id", "nome", "cnpj"), show="headings")
tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("cnpj", text="CNPJ")
tabela.pack()

def cadastrar():
    #PEGAR OS DADOS DOS CAMPOS DE ENTRADA
    try:
        nome = entry.get()
        cnpj = entry2.get()
        if not nome or not cnpj:
            raise ValueError("Por favor, preencha todos os campos.")
        cursor.execute(
            "INSERT INTO cliente (nome,cnpj) VALUES (?, ?)", # INSERIR DADOS DE ENTRADA NA TABELA
            (nome, cnpj)
        )
        conexao.commit()
        print("Salvo no banco:", nome)
        listar()
        # LIMPAR OS CAMPOS DE ENTRADA
        entry.delete(0,"end")
        entry2.delete(0,"end")
        #Para mostrar uma mensagem de confirmação na janela
        messagebox.showinfo("Sucesso", "cliente cadastrado com sucesso!")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
botao = tk.Button(janelas, text="cadastrar", command=cadastrar)
botao.pack() 


def listar():
    # LIMPAR A TABELA ANTES DE PREENCHE
    for item in tabela.get_children(): 
        tabela.delete(item)
        #BUSCAR NO BANCO DE DADOSE INSERER  
    cursor.execute("SELECT * FROM cliente")
    resultado = cursor.fetchall()
    for linha in resultado:
       tabela.insert("","end", values=linha) #INSERIR UMA LINHA NA TABELA
# botao de listar
lista = tk.Button(janelas, text="Listar", command=listar)
lista.pack()

def editar():
    #PEGAR O ITEM SELECIONADO NA TABELA
    item_selecionado = tabela.selection()
    item = tabela.item(item_selecionado)
    valores = item["values"]
    id_cliente = valores[0]
    #PEGAR OS NOVOS DADOS DOS CAMPOS DE ENTRADA
    nome = entry.get()
    cnpj = entry2.get()
    #ATUALIZAR O CLIENTE NO BANCO DE DADOS
    cursor.execute(
        "UPDATE cliente SET nome = ?, cnpj = ? WHERE id = ?",
        (nome, cnpj, id_cliente)
    )
    conexao.commit() #salvar as alterações no banco de dados
    listar()
    #Para mostrar uma mensagem de confirmação na janela
    messagebox.showinfo("Sucesso", "Cliente editado com sucesso!")
salvar_btn = tk.Button(janelas, text="Salvar Edição", command=editar)
salvar_btn.pack()

def excluir():
    #PEGAR O ITEM SELECIONADO NA TABELA
    item_selecionado = tabela.selection()
    item = tabela.item(item_selecionado)
    valores = item["values"]
    id_cliente = valores[0]
    #EXCLUIR O CLIENTE DO BANCO DE DADOS
    cursor.execute("DELETE FROM cliente WHERE id = ?", (id_cliente))
    conexao.commit() #salvar as alterações no banco de dados
    listar()
    #Para mostrar uma mensagem de confirmação na janela
    messagebox.showinfo("Sucesso", "Cliente excluido com sucesso!")
#botao de excluir
excluir_btn = tk.Button(janelas, text="Excluir", command=excluir)
excluir_btn.pack()

def selecionar():
    # pega o item selecionar 
    # colocar os dados nos campos entry e entry2
    item_selecionar = tabela.selection()
    if not item_selecionar: # para a função se nada estiver selecionado.
        return
    item = tabela.item(item_selecionar)
    valores = item["values"]    
    entry.delete(0,"end")   
    entry.insert(0, valores[1]) #coloca o nome no entry
    entry2.delete(0,"end")
    entry2.insert(0, valores[2]) #coloca o cnpj no entry2
tabela.bind("<<TreeviewSelect>>", lambda e: selecionar())

janelas.mainloop()
