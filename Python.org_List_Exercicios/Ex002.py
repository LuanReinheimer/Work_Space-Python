"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""

#vetor = [int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')),
        #int(input('Digite um numero: '))]


vetor = []

for num in range(8):
    vetor.append(int(input('Digite um numero. ')))

soma = 0
for elemento in vetor:
    print(elemento)
    soma = soma + elemento
print(f'a soma é {soma}')

# Nas listas podemos utilizar estes comandos

print(f'Print do vetor é {vetor}')
print(f'maior numero do vetor é {max(vetor)}')
print(f'menor numero do vetor é {min(vetor)}')
print(f'O vetor em ordem crescente {sorted(vetor)}')
print(f'A soma dos numeros dentro do vetor é {sum(vetor)}')

lista = [2,3,4,5,62,1,3,4,]
lista.sort()
print(lista)
print(len(lista))
