class animal():
     def __init__(self,nome):
        self.nome = nome 

     def faze_som(self):
        return "Som Generico"

class Cachorro(animal): # herda da Class Animal
      def faze_som(self):
        return"au au!"

class gato(animal):
     def faze_som(self):
        return"miau!"
        
animal_desconhecido = animal("generico")
dog =Cachorro("paek")
cat = gato("filó")

print("O animal faz:", animal_desconhecido.faze_som())
print("O Cachorro faz:", dog.faze_som())
print("O gato:", cat.faze_som())
