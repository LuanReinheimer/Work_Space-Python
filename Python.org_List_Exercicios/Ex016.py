"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

h = float(input('Digite sua altura: '))

homens = (72.7*h) - 58
mulheres = (62.1 * h) - 44.7

sexo = str(input('Digite seu sexo, M/F:')).strip().upper()

if sexo == 'M':
    print(f'para os homens o peso ideal é {homens:.2f}')
if sexo == 'F':
    print(f'Para mulher o peso ideal é {mulheres:.2f}')