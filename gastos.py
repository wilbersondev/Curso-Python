import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect("gastos.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos (
        ID INTEGER PRIMARY KEY,
        Descricao  TEXT,
        Valor REAL,
        Categoria TEXT
    )
""")
conexao.commit()

# CRIA JANELA PRINCIPAL
janelas = tk.Tk()
janelas.title("Sistema de Gastos")
janelas.geometry("600x500")
label = tk.Label(janelas, text="Descricao: ")
label.pack()
entry =  tk.Entry(janelas)
entry.pack()
label2 = tk.Label(janelas, text="Valor: ")
label2.pack()
entry2 = tk.Entry(janelas)
entry2.pack()

# A TABELA E CRIADA FORA DA FUNÇÃO
tabela = ttk.Treeview(janelas, columns=("ID", "Descricao", "Valor", "Categoria"), show="headings")
tabela.heading("ID", text="ID")
tabela.heading("Descricao", text="Descricao")
tabela.heading("Valor", text="Valor")   
tabela.heading("Categoria", text="Categoria")
tabela.pack()
categorias = ["Alimentação", "Transporte", "Saúde", "Lazer", "Outros"]
combo = ttk.Combobox(janelas, values=categorias, state="readonly")
combo.pack()

def adicionar_gasto(): # essa função adiciona um gasto na tabela
    try:
        descricao = entry.get()
        valor = float(entry2.get())
        categoria = combo.get()
        if not  descricao or not valor or not categoria: # Verifica se todos os campos estão preenchidos
            raise ValueError("Por favor, preencha todos os campos.")
        cursor.execute("INSERT INTO gastos (Descricao, Valor, Categoria) VALUES (?, ?, ?)", (descricao, valor, categoria))
        conexao.commit()
        print("Salvo no banco:", descricao)
        listar_gastos()
        entry.delete(0, "end")
        entry2.delete(0, "end") 
        messagebox.showinfo("Sucesso", "Gasto cadastrado com sucesso!")
    except ValueError:
         messagebox.showerror("Erro", "Valor inválido!")
botao_gasto= tk.Button(janelas, text="Adicionar Gasto", command=adicionar_gasto)
botao_gasto.pack()

def listar_gastos(): # essa função lista os gastos cadastrados na tabela
    for row in tabela.get_children():
        tabela.delete(row)
    cursor.execute("SELECT * FROM gastos")
    for gasto in  cursor.fetchall():
        tabela.insert("",tk.END, values=gasto)
botao_listar =  tk.Button(janelas, text="Listar Gastos", command=listar_gastos)
botao_listar.pack()

def excluir_gasto(): # essa função exclui o gasto selecionado na tabela
    selected_item = tabela.selection()
    if selected_item:
        gasto_id = tabela.item(selected_item)["values"][0]
        cursor.execute("DELETE FROM gastos WHERE ID = ?", (gasto_id,))
        conexao.commit()
        listar_gastos()
    else:
        messagebox.showwarning("Aviso", "Selecione um gasto para excluir.")
botao_excluir = tk.Button(janelas, text="Excluir Gasto", command=excluir_gasto)
botao_excluir.pack()

def ver_total(): # essa função calcula o total de gastos e exibe em uma mensagem
    cursor.execute("SELECT SUM(Valor) FROM gastos")
    total = cursor.fetchone()[0]
    messagebox.showinfo("Total", f"Total gasto: R$ {total:.2f}")

botao_total = tk.Button(janelas, text="Ver Total", command=ver_total)
botao_total.pack()

janelas.mainloop()

