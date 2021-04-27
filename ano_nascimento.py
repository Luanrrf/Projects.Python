nome = input('Qual seu nome?\n')
print(f'Bem vindo {nome}')
idade = input('Quantos anos você tem?\n')
aniversario = int(input('Você já fez aniversário esse ano? Digite 1 para sim e 0 para não\n'))
ano = input ('Em que ano estamos?\n')
if aniversario==1:
    print(f'Olá {nome}, sei que você nasceu em {int(ano)-int(idade)}')

elif aniversario ==0:
    print(f'Olá {nome}, sei que você nasceu em {int(ano) - 1 - int(idade)}')