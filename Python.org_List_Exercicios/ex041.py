"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
print('Os numeors impars de 1 a 50 são: ')

for num in range(1,50):
    if num % 2 == 1:
        print(f'{num}', end=', ')