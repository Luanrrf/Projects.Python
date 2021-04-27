a = int(input('Quantas vezes você gostaria que o loop se repetisse?'))
soma = 0

for n in range(1, a+1):
    num = int(input(f"Informe o {n}/{a} valor: "))
    soma = soma + num

print(f'A soma é {soma}')
