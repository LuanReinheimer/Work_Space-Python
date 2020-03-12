


from random import randint

lista = []
soma = 0

for num in range(5):
    num = randint(1,10)
    lista.append(num)
for num in lista:
      soma+=num

print(f'A SOMA DA LISTA = {lista} É DE {soma}')



