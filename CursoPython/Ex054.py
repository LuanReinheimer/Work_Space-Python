"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""


maioridade = 0
menoridade = 0
for c in range(1, 8):
    ano1 = int(input(f'Digite o ano que voce nasceu aqui : '))
    idades = 2019 - ano1
    if idades >= 21:
        maioridade = maioridade + 1
    else:
        menoridade = maioridade + 1
print(f'São {maioridade} pessoas com maioridade e tivemos {maioridade} pessoas menor de idade')





