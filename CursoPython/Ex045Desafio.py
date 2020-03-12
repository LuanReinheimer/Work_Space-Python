from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçoes:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
jogador = int(input('Qual é sua jogada? '))

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')