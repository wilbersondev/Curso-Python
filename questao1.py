class cliente:
    def __init__(self,nome,cnpj,cidade):
        self.nome = nome
        self.cnpj = cnpj
        self.cidade = cidade

    def apresentar(self):
      print(f"Cliente: {self.nome} | Nome: {self.cnpj} |Cidade: {self.cidade}")  
        
cliente1 = cliente("Lucas","123456789","Piauí")
cliente2 = cliente("João","987654321","São Paulo")
cliente1.apresentar()
cliente2.apresentar()
        
