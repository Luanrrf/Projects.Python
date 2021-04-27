repita = 'sim'
soma = 0

while repita == 'sim':
    a = int(input('Informe o primeiro número:'))
    b = int(input('Informe o segundo número:'))
    if a%2 == 0 and b%2 == 0:
        for num in range (a,b+1,2):
            print(num)
            soma = soma + num
    elif a%2 != 0 and b%2 == 0:
        for num in range (a,b+1,2):
            num = num + 1
            print(num)
            soma = soma + num
    elif a%2 == 0 and b%2 != 0:
        for num in range (a,b,2):
            print(num)
            soma = soma + num
    else:
        for num in range (a,b,2):
            num = num + 1
            print(num)
            soma = soma + num

    print(soma)
    repita = input('Quer que repita?')