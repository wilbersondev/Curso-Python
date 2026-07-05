import sqlite3
import tkinter as tk
from tkinter import messagebox


conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
         ID INTEGER PRIMARY KEY,
         Descricao TEXT,
         Status TEXT DEFAULT 'pendente' 
    )
""")
conexao.commit()

janelas = tk.Tk()
janelas.title("Sistema De Tarefas")
janelas.geometry("500x500")
label = tk.Label(janelas, text="Descricao: ")
label.pack()
entry = tk.Entry(janelas)
entry.pack()
label2 = tk.Label(janelas, text="Status: ")
label2.pack()                       
entry2 = tk.Entry(janelas)
entry2.pack()

from tkinter import ttk
tabela = ttk.Treeview(janelas, columns=("ID", "Descricao", "Status"), show="headings")
tabela.heading("ID", text="ID")
tabela.heading("Descricao", text="Descricao")
tabela.heading("Status", text="Status")
tabela.pack()

def Adicionar_tarefa():
        Descricao = entry.get()
        Status = entry2.get()
        cursor.execute("INSERT INTO tarefas (Descricao, Status) VALUES (?, ?)", (Descricao, Status))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")

botao =  tk.Button(janelas, text="Adicionar Tarefa", command=Adicionar_tarefa)
botao.pack()

def listar_tarefas():
    for row in tabela.get_children():
        tabela.delete(row)
    cursor.execute("SELECT * FROM tarefas")
    for tarefa in cursor.fetchall():
        tabela.insert("", tk.END, values=tarefa)

listar = tk.Button(janelas, text="Listar tarefas", command=listar_tarefas)
listar.pack()

def concluir_tarefa():
    selected_item = tabela.selection()
    if selected_item:
        tarefa_id = tabela.item(selected_item)["values"][0]
        cursor.execute("UPDATE tarefas SET Status = 'concluida' WHERE ID = ?", (tarefa_id,))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Tarefa concluída com sucesso!")
        listar_tarefas()
    else:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")

concluir = tk.Button(janelas, text="Concluir Tarefa", command=concluir_tarefa)
concluir.pack()

def excluir_tarefa():
    selected_item = tabela.selection()
    if not selected_item:
        return
    tarefa_id = tabela.item(selected_item)["values"][0]
    cursor.execute("DELETE FROM tarefas WHERE ID = ?", (tarefa_id,))
    conexao.commit()
    listar_tarefas()  
    messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")
excluir = tk.Button(janelas, text="Excluir Tarefa", command=excluir_tarefa)
excluir.pack()

janelas.mainloop()