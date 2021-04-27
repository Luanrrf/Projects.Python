vetor = []
numero = range(int(input('Quantos algorismos quer que seu vetor tenha? ')))
vetor2 = []
vetorc = []

for a in numero:
    b = int(input(f'Informe o valor do {a + 1}º algarismo: '))
    vetor.append(b)
print(vetor)

for c in numero:
    d = int(input(f'Informe o valor do {c + 1}º algarismo do segundo vetor: '))
    vetor2.append(d)
print(vetor2)

for e in numero:
    f = vetor[e] - vetor2[e]
    vetorc.append(f)

print(vetorc)
