
print(f'Olá aqui, voce pode saber quanto pode comprar com a nossa moeda')

nome = str(input('Qual seu nome completo: '))

reais = float(input('Quanto de dinheiro voce possui em sua carteira R$: '))

dollar = reais / 4.13
euro = reais / 4.56
libra = reais / 5.19

print(f'Com R$ {reais} voce pode comprar US$ {dollar :.2f}')
print(f'Com R$ {reais} voce pode comprar € {euro :.2f}')
print(f'Com R$ {reais} voce pode comprar £ {libra :.2f}')

print('Cotação de 14/10/2019')




