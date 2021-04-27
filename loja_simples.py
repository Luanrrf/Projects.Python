produto = ''
carrinho = []  # lembrar que carrinho é uma lista

while produto != 'sair':
    produto = input("O que deseja comprar? Caso não queira nada escreva 'sair'\n")
    if produto != 'sair':
        carrinho.append(produto)

print('Seguem os itens do seu carrinho:')
for produto in carrinho:
    print(produto)
