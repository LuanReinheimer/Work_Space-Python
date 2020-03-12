"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0
for p in range(1, 6):
    kg = float(input(f'Então qual o seu peso pessoa {p}ª '))
    if p == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg
print(f'O maior peso é o {maior}')
print(f'O mnor peso é o {menor}')





# Maneira mais facil de resolver utilizando listas

pesos = []
for p in range(1, 6):
    kg = float(input(f'Então qual o seu peso pessoa {p}ª: '))
    pesos.append(kg)
print(f'O maior peso é o {max(pesos)}')
print(f'O mnor peso é o {min(pesos)}')
