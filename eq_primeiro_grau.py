print('Primeiramente arrume sua equação colocando as incógnitas nas suas retas e os números inteiros após a igualdade')

a = int(input('Informe o valor da primeira incógnita da primeira equação:'))
b = int(input('Informe o valor da segunda incógnita da primeira equação:'))
c = int(input('Informe o valor fixo que vem após a igualdade na primeira equação:'))
d = int(input('Informe o valor da primeira incógnita da segunda equação:'))
e = int(input('Informe o valor da segunda incógnita da segunda equação:'))
f = int(input('Informe o valor fixo que vem após a igualdade na primeira equação:'))

y = ((a * f) - (d * c)) / ((-d * b) + (a * e))
x = ((c - (b * y)) / a)
print(f'O valor de x = {int(x)} \ne o valor de y = {int(y)}')
