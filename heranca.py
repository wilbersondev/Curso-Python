class animal():
    def __init__(self,nome):
        self.nome = nome 

    def faze_som(self):
        print("Som Generico")

class Cachorro(animal): # herda da Class Animal
    def latir(self):
        print(f"{self.nome}, Diz: Au,Au!")
        
class gato(animal):
    def miar(self):
        print(f"{self.nome}, Diz: MIAU,MIAU")

dog = Cachorro("spaek")
dog.latir("au, au")

cat = gato("filo")
cat.miar("MIAU,MIAU")