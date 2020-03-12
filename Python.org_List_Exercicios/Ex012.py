"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos."""

idade = []
altura = []
quantidade = 0

for pessoa in range(1,5):
    print(f'Aluno {pessoa}')
    idade.append(int(input('Digite sua idade: ')))
    altura.append(float(input('Digite sua altura: ')))
mediaaltura = sum(altura)/5
maiordetreze = []

for pessoa in idade:
    if pessoa > 13:
        maiordetreze.append(idade.index(pessoa))

for pessoa in maiordetreze:
    if altura[pessoa]:
        quantidade = quantidade + 1

print(f'Quantidade de alunos com mais de trezes anos e altura inferior à média: {quantidade}')
print(idade)
print(altura)


