"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""


lista = [[], []]
dado = 0

for num in range(8):
    dado = (int(input(f'Digite o {num} numero: ')))
    if dado % 2 == 0:
        lista[0].append(dado)
    else:
        lista[1].append(dado)

print(f' Os valores pares digitados foram {sorted(lista[0])}')
print(f' Os valores impares digitados foram {sorted(lista[1])}')