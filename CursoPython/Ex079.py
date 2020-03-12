"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """


numbers = []
# Estrutura de repedição onde vai o Input do user.
while True:
    valor = (int(input('Digite um valor: ')))
    numbers.append(valor)
    if numbers.count(valor) == 2:
        print('Valor duplicado! Não vou adicionar...')
        numbers.pop()
    else:
        print('Valor adicionado com sucesso...')

# Estrutura do algoritimo onde pergunta se deseja continuar
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuacao == 'N':
        print(sorted(numbers))
        break