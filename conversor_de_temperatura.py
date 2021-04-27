ask = 'sim'
while ask in ['sim', 'Sim']:
    pergunta = input('Informe se a temperatura está em Celsius, Kelvin ou Fahrenheit?\n')
    temperatura = input('Informe por favor a temperatura\n')

    if pergunta in ['celsius', 'Celsius']:
        print(
            f'se sua temperatura em celsius é de {temperatura}ºC, sua temperatura \nem fahrenheit sera '
            f'{(int(temperatura) * 9 / 5) + 32}ºF '
            f'e em kelvin sera {int(temperatura) + 273}ºK')

    elif pergunta in ['Fahrenheit', 'fahrenheit']:
        print(
            f'se sua temperatura em fahrenheit é de {temperatura}ºF, sua temperatura \nem celsius sera '
            f'{(int(temperatura) - 32) / 1.8}ºC '
            f'e em kelvin sera {(int(temperatura) - 32) * 5 / 9 + 273}ºK')

    elif pergunta in ['Kelvin', 'kelvin']:
        print(
            f'se sua temperatura em kelvin é de {temperatura}ºK, sua temperatura \nem celsius sera '
            f'{int(temperatura) - 273}ºC '
            f'e em fahrenheit sera {(int(temperatura) - 273) * 9 / 5 + 32}ºF')

    else:
        print('Erro, por favor repita o processo e confira se não digitou nenhuma letra errado')

    ask = input('Deseja continuar?')

