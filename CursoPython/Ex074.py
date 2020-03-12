"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint

tupla_sorteada = (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10))

print(tupla_sorteada)
print(f'O MAIOR valor sorteado foi {max(tupla_sorteada)}')
print(f'O MENOR valor sorteado foi {min(tupla_sorteada)}')

