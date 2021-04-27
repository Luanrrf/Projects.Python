soma = 0
cont = 0
media = 0
for numero in range(21):
    print(numero)
    cont = cont + 1
    soma = soma + numero
    media = soma / cont
print(f'A soma é {soma} e a média é {media}')
