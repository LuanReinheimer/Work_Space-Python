"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""



preco_produto1 = float(input('Valor R$: '))

preco_produto2 = float(input('Valor R$: '))

preco_produto3 = float(input('Valor R$: '))

print(f'Voce deve comprar o produto mais barato que tem o preco de R$ {min(preco_produto1, preco_produto2, preco_produto3)}')