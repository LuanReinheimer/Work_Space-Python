"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

numeros = []
pares = []
impares = []


for i in range(5):
    numeros = int(input("Digite um número: "))

    if (numeros % 2) == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print(f'A lista de pares {pares}')
print(f'Alista de impares {impares}')
print({numeros})