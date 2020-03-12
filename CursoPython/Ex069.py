"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

# Variaveis solicitadas pelo enunciado
total_mais_18 = 0
homens = 0
mulheres_menos_20 = 0

# Estrutura do algoritimo onde solicita o input do usuário
while True:
    idade = int(input('Qual a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        total_mais_18 = total_mais_18 + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 = mulheres_menos_20 + 1

# Estrutura do algoritimo onde pergunta se deseja continuar
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuacao == 'N':
            break

# print apos o utilizarmos o break 'quebra do looping'
print(f''''Neste programa tivemos {total_mais_18 } pessoas tem mais de 18 anos,
{homens} homen's foram cadastrados e {mulheres_menos_20} mulhere's tem menos de 20 anos.''')
