"""
# -------------------------------------------------RECEITA--------------------------------------------------------------

receitamaior = 0
receitamenor = 0
receitalista = []
meses = range(12)

for a in meses:
    b = int(input(f'Informe a receita referente ao mês {a+1}: '))
    receitalista.append(b)

receitat1 = receitalista[0] + receitalista[1] + receitalista[2]
receitat2 = receitalista[3] + receitalista[4] + receitalista[5]
receitat3 = receitalista[6] + receitalista[7] + receitalista[8]
receitat4 = receitalista[9] + receitalista[10] + receitalista[11]

receitatlista = (receitat1, receitat2, receitat3, receitat4)
receitatmenor = 0
receitatmaior = 0

print(f'\nA sua maior receita mensal foi de {max(receitalista)} no {receitalista.index(max(receitalista))+1}º mês')
print(f'A sua maior receita trimestral foi de {max(receitatlista)} no '
      f'{receitatlista.index(max(receitatlista))+1}º trimestre')
print(f'\nA sua menor receita mensal foi de {min(receitalista)} no {receitalista.index(min(receitalista))+1}º mês')
print(f'A sua menor receita trimestral foi de {min(receitatlista)} no '
      f'{receitatlista.index(min(receitatlista))+1}º trimestre')

print(f'\nSua receita média trimestral foi de {sum(receitalista)/4}')
print(f'Sua receita média mensal foi de {sum(receitalista)/12}')
"""

# --------------------------------------------------CUSTOS--------------------------------------------------------------

lista_quantidade_produtos = []
lista_rateio = []
quantidade_acumulada = 0
custofixo = int(input('Informe quanto é seu custo fixo mensal:\n'))
custovariavel = int(input('Informe quanto é seu custo variavel mensal:\n'))
print(f'Seu custo total foi de {(custofixo + custovariavel)}\n')
c = input('Seu custo variavel já está rateado? Caso não esteja o critério de produção será a quantidade produzida.\n')

if c == ['sim', 'Sim']:
    c == 'ok'
else:
    tipos_produtos = int(input('Quantos produtos diferentes sua empresa vende?\n'))
    quantidade_acumulada = 0
    for a in range(tipos_produtos):
        q = int(input(f'Informe a quantidade do produto número {a+1}\n'))
        lista_quantidade_produtos = lista_quantidade_produtos + [q]
        quantidade_acumulada = quantidade_acumulada + q

for a in lista_quantidade_produtos:
    b = (a*100)/quantidade_acumulada
    print(f'O produto {lista_quantidade_produtos.index(a)+1} representa {float(round(b,2))}%')
    valor_rateio = float(round((b * (custofixo + custovariavel))/100,2))
    lista_rateio.append(valor_rateio)

for a in range(len(lista_rateio)):
    print(f'O valor de rateio do custo do {a+1}º produto é de R${(lista_rateio[a])}')

"""
# ------------------------------------------------ROI E PAYBACK---------------------------------------------------------

invest = int(input('Quanto ao total você investiu?\n'))
retorno = int(input('Quanto você recebeu de volta até agora?\n'))
time = int(input('Em quantos meses você recebeu esse valor?\n'))

payback = (invest * time) / retorno
print(f'Seu payback será em {payback} meses')
roi2 = 24 / payback
roi5 = 60 / payback

print(f'Seu ROI em 2 anos será de {roi2} \nE em 5 anos o ROI será de {roi5}')

"""