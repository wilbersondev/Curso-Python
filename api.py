import requests

Cep = input("Informa o seu Cep: ")
resposta = requests.get(f"https://viacep.com.br/ws/{Cep}/json/")
dados = resposta.json()

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{Cep}/json/")
    dados = resposta.json()

    if "erro" in dados:
        print("Cep não encontrado")
    else:
        print("Rua:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("UF:", dados["uf"])

except KeyError:
    print("Cep invalidor digite um Cep com 8 digitos")