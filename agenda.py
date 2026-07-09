import sqlite3
import tkinter as tk

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("""
               
     CREATE TABLE IF NOT EXISTS contatos(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Telefone TEXT NOT NULL,
        Email TEXT NOT NULL
    )
""") 
conexao.commit()

janelas = tk.Tk()
janelas.title("Agenda de Contatos: ")
janelas.geometry("600x800")
label = tk.Label(janelas, text="Nome:")
label.pack()
entry = tk.Entry(janelas)
entry.pack()
label2 = tk.Label(janelas, text="Telefone:")
label2.pack()   
entry2 = tk.Entry(janelas)
entry2.pack()   
label3 = tk.Label(janelas, text="Email:")
label3.pack()   
entry3 = tk.Entry(janelas)
entry3.pack()
label4 = tk.Label(janelas, text="buscar:")
label4.pack()
entry_buscar = tk.Entry(janelas)
entry_buscar.pack()   

from tkinter import ttk, messagebox
tabela = ttk.Treeview(janelas, columns=("Id", "Nome","Telefone", "Email"), show="headings")
tabela.heading("Id", text="ID")
tabela.heading("Nome", text="Nome") 
tabela.heading("Telefone", text="Telefone")
tabela.heading("Email", text="Email")
tabela.pack()

def Adicionar_contato():
    try:
        nome = entry.get()
        telefone = entry2.get()
        email = entry3.get()
        if not nome or not telefone or not email:
            raise ValueError("Por favor, preencha todos os campos.")
        cursor.execute(
            "INSERT INTO contatos (Nome, Telefone, Email) VALUES (?, ?, ?)",
            (nome, telefone, email))
        conexao.commit()
        print("Contato adicionado:", nome)
        listar_contato()
        entry.delete(0, "end")
        entry2.delete(0, "end")
        entry3.delete(0, "end")
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
    except ValueError:
        messagebox.showinfo("Error","Contato Invalido")

Adiconar_btn = tk.Button(janelas, text="Salvar Contato", command = Adicionar_contato )
Adiconar_btn.pack()

def listar_contato ():
    for row in tabela.get_children():
        tabela.delete(row)
    cursor.execute("SELECT * FROM contatos  ")
    for agenda in cursor.fetchall():
         tabela.insert("", tk.END, values = agenda )

listar_btn = tk.Button(janelas, text = "Listar Contatos", command = listar_contato)
listar_btn.pack()

def buscar_contato():
    nome = entry_buscar.get()
    cursor.execute("SELECT * FROM contatos WHERE Nome LIKE ?", (f"%{nome}%",))

    resultado = cursor.fetchall()

    for row in tabela.get_children():
        tabela.delete(row)
    for agenda in resultado:
        tabela.insert("", tk.END, values = agenda)
    
buscar_btn = tk.Button(janelas, text = "Buscar Contato", command = buscar_contato)
buscar_btn.pack()

def excluir_contato():
    item_selecionado = tabela.selection()
    item = tabela.item(item_selecionado)
    valores = item["values"]
    id_contato = valores[0]
    cursor.execute("DELETE FROM contatos WHERE Id = ?", (id_contato,))
    conexao.commit()
    listar_contato()
    messagebox.showinfo("Sucesso", "Contato Excluido")
excluir_btn = tk.Button(janelas, text = "Excluir Contato", command = excluir_contato )
excluir_btn.pack()

janelas.mainloop()

