""" Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

vetor = []
maior = []
menor = []
for num in range(5):
    vetor.append(int(input(f'Digite um numero para a posiçao {num}: ')))
for posicao, valores in enumerate(vetor):
    if valores == max(vetor):
        maior.append(posicao)
    if valores == min(vetor):
        menor.append(posicao)
print('=-'*30)
print(vetor)
print(f'O maior valor digitado foi {max(vetor)} na posição {maior}')

print(f'O menor valor digitado foi {min(vetor)} na posição {menor}', end=' ')



#for c, v in enumerate(vetor):
    #print(f'Na posição {c} encontrei o valor {v}!')
#print(f'Cheguei ao final da lista')
#print(vetor)
#print(f'O maior valor digitado foi {max(vetor)} na posição {vetor.index(max(vetor))}')
#print(f'O menor valor digitado foi {min(vetor)} na posição {c}')


#a = [2, 3, 4, 7]
#b = a.copy()
#b[2] = 8
#print(a)
#print(b)
