"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
print('-=' * 30)
print('=' * 10, 'Loja de produtos', '=' * 10)

# Variaveis que o sistema pede
total_gasto = 0

produtos_mais_100 = 0

nome_produto_barato = ' '
contador = 0
menor = 0

# Estrutura de repedição onde vai o Input do user.
while True:
    produtos_comprados = str(input('Nome do Produto comprado: ')).upper().strip()
    preco_produto = float(input('Preço: R$ '))
    contador = contador + 1
    total_gasto = preco_produto + preco_produto

    if preco_produto > 100:
        produtos_mais_100 = produtos_mais_100 + 1

    if contador == 1:
        menor = preco_produto
        nome_produto_barato = produtos_comprados
    else:
        if preco_produto < menor:
            menor = preco_produto
            nome_produto_barato = produtos_comprados


# Estrutura do algoritimo onde pergunta se deseja continuar
    continuacao = ' '
    while continuacao not in 'SN':
        continuacao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuacao == 'N':
        break
# print apos o utilizarmos o break 'quebra do looping'
print(f"""O total da compra foi de R$ {total_gasto}
Temos {produtos_mais_100} produtos custando mais de R$ 100.00,
O produto mais barato foi {nome_produto_barato} que custou {menor}""")
