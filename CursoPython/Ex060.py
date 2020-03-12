'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''


# Usando um modulo
from math import factorial

n = int(input('Digite um numero para calcaular o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')


# codigo sem Modulo

n = int(input('Digite um numero para calcaular o seu fatorial: '))
c = n
f = factorial(c)
print(f'Calculando {c}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f'x' if c > 1 else '=', end='') #Podemos usar est. de condições dentro de um print.
    c = c - 1
print(f'{f}')
