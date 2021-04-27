n = int(input('Informe um valor\n'))
cont = 0
e = 0
a = 0

while a < n:
    for cont in range(0, n):
        a = a + 1
        e = e + 1 / a

e = e + 1
print(e)
