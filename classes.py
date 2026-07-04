class cliente:
    def __init__(self,nome,cnpj,cidade):
        self.nome = nome
        self.cnpj = cnpj
        self.cidade = cidade

cliente1 = cliente("Lucas","123456789","Piauí")
print(cliente1.nome)
print(cliente1.cnpj)
print(cliente1.cidade)
cliente2 = cliente("João","987654321","São Paulo")
print(cliente2.nome)            
print(cliente2.cnpj)    
print(cliente2.cidade)
