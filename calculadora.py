def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

perg = str(input("Informe o sinal do que você deseja fazer com os números sendo: \n+ para soma \n- para subtração \n* para multiplicação \n/ para divisão: \n"))

if perg == '+':
    print(soma(num1, num2))

if perg == '-':
    print(subtracao(num1, num2))

if perg == '*':
    print(multiplicacao(num1, num2))

if perg == '/':
    print(divisao(num1, num2))