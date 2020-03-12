from time import sleep

print('Calculo da passagem por KM')

dis = float(input('Qual a distancia da sua viagem me km: '))

print('Calculando...')
sleep(1)

if dis <= 200:
    valorpass1 = (dis * 0.50)
    print(f'O valor da passagem sera de R${valorpass1}')

elif dis > 200:
    valorpass2 = (dis * 0.45)
    print(f'O valor da passagem de viagens mais longas sera de R${valorpass2}')
