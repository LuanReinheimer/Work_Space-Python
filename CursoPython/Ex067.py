'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. '''
tabuada = 0
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        print('Programa encerrado!')
        break
    for num in range(1, 11):
        print(f'''{num} x {tabuada} = {num * tabuada}''')



