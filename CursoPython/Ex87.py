"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[],[],[]]
spares = 0
maior = 0
soma = 0

for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-='*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
                if matriz[l][c] % 2 == 0:
                        spares = spares + matriz[l][c]
        print()
print('-='*30)

print(f'A soma dos valores pares é {spares}')
for l in range(0, 3):
        soma = soma + matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
