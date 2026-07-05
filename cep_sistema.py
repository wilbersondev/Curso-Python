import tkinter as tk
import sqlite3
import requests

conexao = sqlite3.connect("enderecos.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS enderecos (
        id   INTEGER PRIMARY KEY,
        Cep TEXT,       
        rua TEXT,
        bairro TEXT,
        cidade TEXT,
        uf TEXT
    )
""")
conexao.commit()


janelas = tk.Tk()
janelas.title("Sistema De Enderecos")
janelas.geometry("500x400")
label = tk.Label(janelas, text="Cep: ")
label.pack()
entry = tk.Entry(janelas)
entry.pack()    
label2 = tk.Label(janelas, text="Rua: ")
label2.pack()       
entry2 = tk.Entry(janelas)
entry2.pack()
label3 = tk.Label(janelas, text="Bairro: ")
label3.pack()
entry3 = tk.Entry(janelas)
entry3.pack()   
label4 = tk.Label(janelas, text="Cidade: ")
label4.pack()   
entry4 = tk.Entry(janelas)
entry4.pack()   
label5 = tk.Label(janelas, text="UF: ")
label5.pack()
entry5 = tk.Entry(janelas)
entry5.pack()

def buscar_cep():
    Cep = entry.get()
    resposta = requests.get(f"https://viacep.com.br/ws/{Cep}/json/")
    dados = resposta.json()

    if "erro" in dados:
        print("Cep não encontrado")
    else:
        entry2.delete(0, tk.END)
        entry2.insert(0, dados["logradouro"])
        entry3.delete(0, tk.END)
        entry3.insert(0, dados["bairro"])
        entry4.delete(0, tk.END)
        entry4.insert(0, dados["localidade"])
        entry5.delete(0, tk.END)
        entry5.insert(0, dados["uf"])
botao = tk.Button(janelas, text="buscar_cep", command=buscar_cep)
botao.pack()

def salvar():
    cep = entry.get()
    rua = entry2.get()
    bairro = entry3.get()
    cidade = entry4.get()
    uf = entry5.get()
    cursor.execute(
        "INSERT INTO enderecos ( Cep, Rua, Bairro, Cidade, Uf) VALUES (?,?,?,?,?)",
        (cep, rua, bairro, cidade, uf)
    )
    conexao.commit()
    print("Endereço Salvo !")
botao = tk.Button(janelas, text="salvar", command=salvar)
botao.pack()



janelas.mainloop()