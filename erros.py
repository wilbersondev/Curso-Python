numero = input("Informe um Número ")
try:
    numero = int(numero)
    print(numero * 2)
except ValueError:
    print("Informe apenas numeros! ")
finally:
    print("Fim do programa!")