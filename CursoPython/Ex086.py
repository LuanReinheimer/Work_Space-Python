"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[],[],[]]

for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()


"======================================================================================================================"
"Outra maneira de fazer com menos linha"
"======================================================================================================================"

matriz = [[],[],[]]
for c in range(3):
    for l in range(3):
        matriz[c].append(int(input(f'Digite valor para [{c},{l}]: ')))
print('-=' * 30)
for c in range(3):
    print('\n', end='') if c > 0 else ''
    for l in matriz[c]:
        print(f'[{l:^5}]', end='')