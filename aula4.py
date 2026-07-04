cliente=input("Digita o nome do cliente: ")
print("Olá",cliente)
cnpj=input("DIGITE O CNPJ DO CLIENTE: ")
print("CNPJ do cliente:", cnpj) 
if len(cnpj) == 14 :
        print("CNPJ válido")
        print("Bem vindo:", cliente)
        arquivo = open("cliente.txt", "a")
        arquivo.write("Cliente: " + cliente + " - CNPJ: " + cnpj + "\n")
        arquivo.close()
else:
        print("CNPJ inválido")  

