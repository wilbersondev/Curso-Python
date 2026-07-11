import sqlite3 
import tkinter as tk 

conexao = sqlite3.connect("mercadoria.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome text,
        Quantidade INTEGER,
        Preço real
    )
""")
conexao.commit()

janelas = tk.Tk()
janelas.title("Sistema de Estoque ")
janelas.geometry("600x800")
label = tk.Label(janelas, text="Nome")
label.pack()
entry = tk.Entry(janelas)
entry.pack()
label2 = tk.Label(janelas, text="Quantidade")
label2.pack()
entry2 = tk.Entry(janelas)
entry2.pack()
label3 = tk.Label(janelas, text="Preço")
label3.pack()
entry3 = tk.Entry(janelas)
entry3.pack()
label_qtn = tk.Label(janelas, text ="Entrada de estoque")
label_qtn.pack()
entry_qtn = tk.Entry(janelas)
entry_qtn.pack()
label_saida = tk.Label(janelas, text="Qtd Saída:")
label_saida.pack()
entry_saida = tk.Entry(janelas)
entry_saida.pack()

from tkinter import ttk, messagebox
tabela = ttk.Treeview(janelas, columns = ("Id","Nome","Quantidade","Preço"), show="headings")
tabela.heading ("Id", text = "Id")
tabela.heading ("Nome", text = "Nome")
tabela.heading ("Quantidade", text = "Quantidade")
tabela.heading ("Preço", text = "Preço")
tabela.pack()

def cadastra_produto():
    try:
        Nome = entry.get()
        Quantidade = entry2.get()
        Preço = float (entry3.get())
        if not Nome  or not Quantidade or not Preço :
            raise ValueError ("Preencher todos os campos!")
        cursor.execute(
            "INSERT INTO estoque(Nome, Quantidade, Preço) VALUES (?, ?, ?)", (Nome, Quantidade, Preço))
        conexao.commit()
        print("Produto Cadastrado", Nome)
        Listar_Produtos()
        entry.delete(0, "end")
        entry2.delete(0, "end")
        entry3.delete(0, "end")
        messagebox.showinfo("Sucesso", "Produtos Cadastrados")

    except ValueError: 
        messagebox.showinfo("Erro", "Cadastre um Produto")
Cadastra_btn = tk.Button(janelas, text="Cadastrado", command  = cadastra_produto)
Cadastra_btn.pack()

def Listar_Produtos():
    for row in tabela.get_children():
        tabela.delete(row)
    cursor.execute("SELECT * FROM estoque") # buscar todos os produtos 
    for  row  in cursor.fetchall(): # para cada produto encontrado 
        tabela.insert("", tk.END, values = row) # insere o produtoi na tabela 
        # O row é cada linha que veio do banco - um produto por vez 
    
Listar_btn = tk.Button(janelas, text = "Produtos Listados", command = Listar_Produtos)
Listar_btn.pack()

def Entrada_de_Estoque():
    selected_item = tabela.selection()
    if selected_item:
        estoque_id = tabela.item(selected_item)["values"][0]
        Quantidade = int(entry_qtn.get())
        cursor.execute(" UPDATE estoque SET quantidade = quantidade + ? WHERE id = ?", 
                      (Quantidade, estoque_id))
        conexao.commit()
        messagebox.showinfo("Susseco", "Produtos Adicionados")
        Listar_Produtos()
        entry.delete(0, "end")
        entry2.delete(0, "end")
        entry3.delete(0, "end")
        entry_qtn.delete(0, "end")
        entry_saida.delete(0, "end")
    else:
        messagebox.showinfo("Erro","Produto não foi Adicionado")
Entrada_btn = tk.Button(janelas, text = "Entrada de Estoque", command=Entrada_de_Estoque)
Entrada_btn.pack()

def Saida_de_Estoque():
    selected_item = tabela.selection() 
    estoque_id = tabela.item(selected_item)["values"][0]
    Quantidade_atual = tabela.item(selected_item)["values"][2]
    Quantidade = int(entry_saida.get())
    if Quantidade > Quantidade_atual:
        messagebox.showwarning("Erro", "Produtos  Insuficiente")
        return

    else :
        cursor.execute(
        "UPDATE estoque SET quantidade = quantidade - ? WHERE id = ?",
        (Quantidade, estoque_id)
        )
        conexao.commit()
        Listar_Produtos()
        messagebox.showwarning("Sucesso", "Saida de Produtos")
        entry.delete(0, "end")
        entry2.delete(0, "end")
        entry3.delete(0, "end")
        entry_qtn.delete(0, "end")
        entry_saida.delete(0, "end")
Saida_btn = tk.Button(janelas, text = "Saida de Estoque", command = Saida_de_Estoque)
Saida_btn.pack()

def selecionar():
    # pega o item selecionar 
    # colocar os dados nos campos entry e entry2
    selected_item = tabela.selection()
    if not selected_item: # para a função se nada estiver selecionado.
        return
    item = tabela.item(selected_item)
    valores = item["values"]    
    entry.delete(0,"end")   
    entry.insert(0, valores[1]) #coloca o nome no entry
    entry2.delete(0,"end")
    entry2.insert(0, valores[2]) #coloca o quantidade no entry2

tabela.bind("<<TreeviewSelect>>", lambda e: selecionar())


janelas.mainloop()
