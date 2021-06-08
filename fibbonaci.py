anterior = 0
atual = 1
lista = [anterior,atual]
cont = 2

max = int(input("Informe quantos números da sequência Fibbonacci você deseja: "))

while (cont < max):

    proximo = anterior + atual
    anterior = atual # Tanto essa linha quanto a de baixo só foram necessárias para a próxima leitura da variável proximo
    atual = proximo

    lista.append(proximo)
    print(lista)
    
    cont += 1
    
# Caso queira algum número específico da lista
elemento = int(input("Qual elemento da lista você quer ver? ")) - 1
print (lista[elemento])