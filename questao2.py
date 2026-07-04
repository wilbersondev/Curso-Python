class produto :
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self,percentual):
       desconto = self.preco * percentual / 100
       return self.preco - desconto
        
produto1 = produto("notebook", 3000)
print(produto1.aplicar_desconto(10))
       