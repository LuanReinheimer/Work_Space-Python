"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

lista = []

# Estrutura do input do usuário:


while True:
    numbers = int(input('Digite um valor: '))
    lista.append(numbers)
    continacao = ' '
    while continacao not in 'SN':
        continacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        lista.sort(reverse=True)
        if continacao == 'N':
            print(f'Os valores decresente são {lista}')
            print(f'Voce digitou {len(lista)} elementos')
            if 5 in lista:
                print('O 5 faz parte da lista!')
            else:
                print('O 5 não esta na lista!')
            break
