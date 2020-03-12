"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos"""

# Variaveis globais para que sejam definidas as resoluçoes da estrutura condicional.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher = 0

# Estrutura de laço de repetição FOR para repetir o que esta dentro do escopo 5 vezes.
for p in range(1, 5):
    print(f'----{p}º Pessoa----')
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO M/F: ')).strip()
    somaidade = somaidade + idade

# Estrutura de Condições aninhadas para mostrar o que se pede no escopo do programa.
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher = totalmulher + 1
mediaidade = somaidade / 4

# imprição dos valores do fluxo
print(f'A media de idade da galera é {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totalmulher} mulheres com menos de 20 anos')