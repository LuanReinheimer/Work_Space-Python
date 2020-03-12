print('-'*20)
print('Analisidaor de Triangulo')
print('-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r3 < r1 + r2:
    print(f'Os segmentos acima FORMAM UM TRIANGULO ')
else:
    print(f'Os segmentos acima NÃO FORMAM UM TRIANGULO ')