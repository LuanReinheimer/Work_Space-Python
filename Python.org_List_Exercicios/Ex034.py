"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""

# Forma 1

minha_matriz = [[1,2,3],[4,5,6],[7,8,9]]

# Criando uma matriz com valores dados
print(minha_matriz)

print('-='*30)

for num in range(0,3):
    print(minha_matriz[num])

print('-='*30)

# Alterando valores dentro da matriz
print('Vamos alterar os valores das matrizes')

minha_matriz[0][0] = int(input('Digite um numero para [1:1]: '))
minha_matriz[0][1] = int(input('Digite um numero para [1:2]: '))
minha_matriz[0][2] = int(input('Digite um numero para [1:3]: '))

minha_matriz[1][1] = int(input('Digite um numero para [2:1]: '))
minha_matriz[1][1] = int(input('Digite um numero para [2:2]: '))
minha_matriz[1][2] = int(input('Digite um numero para [2:3]: '))

minha_matriz[2][1] = int(input('Digite um numero para [3:1]: '))
minha_matriz[2][1] = int(input('Digite um numero para [3:2]: '))
minha_matriz[2][2] = int(input('Digite um numero para [3:3]: '))

print('-='*30)

for num in range(0,3):
    print(minha_matriz[num])

print('-='*30)
# =====================================================================================================================

# Forma 2

minha_matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        minha_matriz2[linha][coluna] = int(input(f'Digite um valor para [{linha+1}.{coluna+1}]: '))
print('--'*30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{minha_matriz2[linha][coluna]}]', end=' ')
    print( )