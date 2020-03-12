print('-'*20)
print('Analisidaor de Triangulo')
print('-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r3 < r1 + r2:
    print(f'Os segmentos acima FORMAM UM TRIANGULO ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print(f'Os segmentos acima NÃO FORMAM UM TRIANGULO ')

#https://www.youtube.com/watch?v=ZX7sCPjcHA0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=56