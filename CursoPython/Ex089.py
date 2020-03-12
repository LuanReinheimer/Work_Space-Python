"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""


notas_alunos = []
dados = []

# Estratégia de colocar lista dentro de outra.

while True:
    nome = (str(input('NOME: ')))
    nota1 = (int(input('Nota 1: ')))
    nota2 = (int(input('Nota 2: ')))
    media = (nota1+nota2)/2

    dados.append([nome, [nota1, nota2], media])
    notas_alunos.append(dados.copy())
    dados.clear()
    resposta = (str(input('Deseja continuar? [S/N] ')))
    if resposta in 'Nn':
        break
print(notas_alunos)