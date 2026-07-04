while True :

    print("=== SISTEMA DE CLIENTES ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")    
    print("3 - Sair")

    codigo = input("Digite o código de 1 a 3: ")

    if codigo == "1":
     cadastro = input("Digite o nome do cliente: ")
     dados = input("Digite CPF do cliente: ")
     print("Cliente cadastrado:", cadastro)
     arquivo = open("cadastro.txt", "a")
     arquivo.write("cadastro: " + cadastro + " - dados: " + dados + "\n")
     arquivo.close()
    if codigo == "2":
     arquivo = open("cadastro.txt", "r")
     conteudo = arquivo.read()
     arquivo.close()
     print(conteudo)
    if codigo == "3":
     print(" encerrando o programa")
     break
