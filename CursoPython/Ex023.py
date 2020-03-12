a = int(input('Digite um numero: '))

print(f'Verificando seu N° {a}')


b = a // 1 % 10
print(f'Unidade:{b} ')

c = a // 10 % 10
print(f'Dezena:{c} ')

d = a // 100 % 10
print(f'Centena:{d} ')

e = a // 1000 % 10
print(f'Milhar:{e}')


# Outa maneira de ser feito porem mais rapido e facil.


num = str(int(input('Digite um número entre 0 e 9999: '))+10000)
print(f'unidade:{num[4]} \ndezena:{num[3]} \ncentena:{num[2]} \nmilhar:{num[1]}')



