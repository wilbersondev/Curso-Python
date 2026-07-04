class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo 

    def depositar(self,valor):
        self.saldo = self.saldo + valor
        print("Saldo:", self.saldo)
    
    def sacar(self,valor):
        if valor > self.saldo:
            print("saldo insuficiente!")
        else:
            self.saldo = self.saldo - valor
            print("Saldo:", self.saldo )
    
conta = ContaBancaria("lucas", 1000)
conta.depositar(500)
conta.sacar(1500)
conta.sacar(2000)

        