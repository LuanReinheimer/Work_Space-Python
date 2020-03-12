'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''


print(30 * '=')
print('Vamos jogar Par ou Impar')
print(30 * '=')
vitorias = 0

from random import randint

while True:
    jogadasua = int(input('Diga um valor: '))
    computador = randint(0, 10)
    jogadas = jogadasua + computador
    par_ou_impar = ' '
    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('[P/I]:')).strip().upper()[0]
    print(f'Voce jogou {jogadasua} e o computador jogou {computador} o total é {jogadas} ', end='')
    if par_ou_impar == 'P':
        if jogadasua % 2 == 0:
            print('Deu PAR!')
            print('Voce Ganhou!')
            vitorias = vitorias + 1

        else:
            print('Deu IMPAR!')
            print('Voce Perdeu!')
            break

    elif par_ou_impar == 'I':
        if jogadasua % 2 == 1:
            print('Deu PAR!')
            print('Voce Ganhou!')
            vitorias = vitorias + 1

        else:
            print('Deu IMPAR!')
            print('Voce Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! VOCE VENCEU {vitorias} vezes')

