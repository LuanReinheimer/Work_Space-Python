from random import sample
from random import choices
from time import sleep

jogos = []
n = int(input('Quantos jogos?: '))

for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a.copy())
    print(f'Jogo {c + 1}: {a}')
    sleep(0.5)

print("Sorteando 2 jogos aleatoriamente:",sample(jogos, 2))
print('Sorteando um jogo', choices(jogos))