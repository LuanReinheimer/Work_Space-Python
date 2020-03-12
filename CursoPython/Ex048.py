soma = 0
cont = 0
cont1 = 0
for mult in range(1, 501, 2):
    if mult % 3 == 0:
        soma = soma + mult
        cont1 = cont1 + 1
    cont = cont + 1

print(f'Entre 1 e 500 existem {cont} numeros impares')
print(f'Entre 1 e 500  soma de todos os {cont1} valores multiplos por 3 é de {soma}')