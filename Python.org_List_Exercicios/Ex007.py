"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

vetor = []
multiplicaçao = 1

for num in range(5):
    multiplicaçao = 1
    vetor.append(int(input(F'Digite o numero {num+1}: ')))
    for num in vetor:
        multiplicaçao = multiplicaçao * num

print(f'A lista em ordem ficou', sorted(vetor))
print(f'A soma do vetor é {sum(vetor)}')
print(f'A multiplicação é {multiplicaçao}')
