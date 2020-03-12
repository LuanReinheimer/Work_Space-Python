''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.'''

from random import randint
from time import sleep
num = 1
palpites = 0

print('Bem vindo ao jogo de adivinha, tente adivinhar de 0 a 10 qual numero é o que eu vou sortear')
print('-'*50)

computador = randint(0, 10)
print(f'Pensando...')
sleep(2)
print('-'*50)

while num != computador:
    num = int(input('Pronto! ja escolhi o numero, pode digitar o nº que voce acha que eu estou escondendo: '))
    if (num == computador):
        print('Voce acertou!!')
    palpites = palpites + 1
print(f'O numero de palpites foram {palpites} até acertar o numero escolhido pelo computador foi {computador}')