
escritorio="COMPLETA"
estado="Piauí"
clientes=[
    {"nome":"IMLV","CNPJ":"11050291000191","Cidade":"Teresina"},
    {"nome":"MOVILOC","CNPJ":"11050292000192","Cidade":"Valença"},
    {"nome":"SENAI","CNPJ":"11050293000193","Cidade":"Picos"}
 ]
print("Escritório:", escritorio)
print("Estado:", estado)       
def listar_clientes():
    for cliente in clientes:
        print("Nome:", cliente["nome"])
        print("CNPJ:", cliente["CNPJ"])
        print("Cidade:", cliente["Cidade"]) 
listar_clientes()
def mostrar_cliente(c):
           print("Nome:", c["nome"])
           print("CNPJ:", c["CNPJ"])
           print("Cidade:", c["Cidade"])    
mostrar_cliente(clientes[1])
def validar_cnpj(cnpj):
    if len(cnpj) == 14 :
        print("CNPJ válido")
    else:
        print("CNPJ inválido")  
validar_cnpj("12345678985236")