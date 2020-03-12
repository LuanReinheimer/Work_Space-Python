'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

opcao = 0

print('Digite dois valores para definir o que fazer com eles no menu abaixo:')
print('=-'*50)
valor1 = int(input('Inteiro 1: '))
valor2 = int(input('Inteiro 2: '))

while opcao != 5:
    print('''Menu de opçoes:
        [1] Somar.
        [2] Multiplicar.
        [3] Maior.
        [4] Novos numero.
        [5] Sair do programa.''')
    print('=-' * 50)
    opcao = int(input('Selecione umas das opções: '))

    if opcao == 1:
        valor3 = valor1 + valor2
        print(f'A soma dos dois valores são {valor3} ')

    if opcao == 2:
        valor4 = valor1 * valor2
        print(f'A Multiplicação dos dois valores são {valor4} ')

    if opcao == 3:
        if valor1 == valor2:
            print('Os valores são iguais')
        elif valor1 < valor2:
            print(f'O valor maior é o {valor2}')
        else:
            print(f'O valor maior é o {valor1}')
    elif opcao == 4:
        valor1 = 0
        valor2 = 0
        valor1 = int(input('Inteiro 1: '))
        valor2 = int(input('Inteiro 2: '))



print('Fim do programa....')
