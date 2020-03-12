'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
 elementos de uma Sequência de Fibonacci.'''

print('=-'*30)
print('Sequencia de Fibonacci')
print('=-'*30)

n = int(input('Quantos termos voce quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1} -> {termo2} ', end='')
contador_continuação = n - 2
total = 0
contador = 1

while contador_continuação != 0:
    total = total + contador_continuação
    while contador <= total:
        termo3 = termo1 + termo2
        print(f'-> {termo3} ', end='')
        termo1 = termo2
        termo2 = termo3
        contador = contador + 1
    print('-> Pausa...')
    contador_continuação = int(input('Deseja continuar a Sequenciade Fibonacci: '))
print('Fim...')


