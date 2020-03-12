"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

lista = []
listapares = []
listaimpares = []

# Estrutura do input do usuário:

while True:
    numbers = int(input('Digite um valor: '))
    lista.append(numbers)
    continacao = ' '
    if numbers % 2 == 0:
        listapares.append(numbers)
    else:
        listaimpares.append(numbers)

    while continacao not in 'SN':
        continacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continacao == 'N':
            print(f'Os valores da lista são {lista}')
            print(f'A lista de impares é {listaimpares}')
            print(f'A lista de pares é {listapares}')
            break

# Outro modo de resolver apenas com um WHILE:
# lista = []
# pares = []
# impares = []
#
# while True:
#     numero = int(input('Digite um numero :'))
#     lista.append(numero)
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)
#     decisao = str(input('Quer continuar? S/N: '))
#     if decisao == 'n':
#         break
#
# print(f'Lista completa com os numeros : {lista}')
# print(f'Tendo os numeros pares : {pares}')
# print(f'Tendo os numeros impares : {impares}')
