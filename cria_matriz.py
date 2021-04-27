linhas = range(int(input('Informe quantas linhas você deseja que sua matriz tenha: ')))
colunas = range(int(input('Informe quantas colunas você deseja que sua matriz tenha: ')))

def lista(a):
    print("alo")

for a in linhas:
    lista(a)
    for b in colunas:
        c = int(input(f'Informe o valor da {a+1}ª linha e da {b+1}ª coluna: '))
        lista(a).append(c)
        b = b + 1
    print(lista(a))
    a = a + 1

