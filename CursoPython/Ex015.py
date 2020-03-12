print(f'Bem vindo ao calculo de aluguel de uma locadora de carros')

dias = int(input('Quantos dias este carro ficou alugado ? '))
km = float(input('Quantos KM rodou este carro? '))

calculo = (dias * 60) + (km * 0.15)


print(f'O total a pagar é R${calculo:.2f}')