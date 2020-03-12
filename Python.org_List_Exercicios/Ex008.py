"""Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida."""
idade = []
altura = []

for i in range(5):
    print(f'Pessoa {i+1}')
    idade.append(str(input(f'Qual a sua idade? ')))
    altura.append(float(input(f'Qual a sua altura? ')))

idade.reverse()
print(f'IDADE: {idade}')
altura.reverse()
print(f'ALTURA: {altura}')
