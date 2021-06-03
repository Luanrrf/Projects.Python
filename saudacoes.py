nome = ""
lista = [] 
contador = 0
maximo = 0

while True:
    nome = input("\n Qual seu nome? Digite sair para encerrar o programa. \n ")
    if nome in ["sair", "Sair"]: 
        print("\n")
        break
    else:
        lista.append(nome)
        maximo += 1

while contador < maximo:
    print("Bem vindo, Sr(a)",lista[contador],", espero que esteja tendo um excelente dia.")
    contador += 1

print("\n")