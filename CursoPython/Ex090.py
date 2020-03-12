"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""


alunos = {}

alunos['nome:'] = str(input('Nome: '))
alunos['nota'] = float(input(f'Apresente sua media: '))
if alunos['nota'] >= 7:
    alunos['situação']= 'aprovado'

elif 5 <= alunos['nota'] < 7:
    alunos['situação']= 'recuperacao'

else:
    alunos['situação']= 'reprovado'

print(f'Sua media é igual a {alunos["nota"]}')
print(f'Sua situação é {alunos["situação"]}')




