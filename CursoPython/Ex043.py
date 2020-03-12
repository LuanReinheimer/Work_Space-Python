from time import sleep
print('Calculo do IMC')

peso = float(input('Peso: '))

altura = float(input('Altura em M: '))

imc = (peso / (altura * altura))

print('Calculando...')
sleep(2)

print(f'Seu IMC {imc :.2f}')

print('CLASSIFICAÇÃO:')

if imc <= 18.5:
    print('MAGREZA')
elif imc <= 24.9:
    print('NORMAL')
elif imc <= 29.9:
    print('SOBREPESO')
elif imc <= 39.9:
    print('OBSIDADE')
else:
    print('OBSIDADE MÓRBIDA')