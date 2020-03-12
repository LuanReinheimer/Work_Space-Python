"""faça um programa que leia 5 números e informe o maior número."""

lista = []
for num in range(1,6):
    lista.append(int(input(f'Digite o {num}º: ')))
print(f'O Maior numero é {max(lista)}')
print(f'A soma dos numero é {sum(lista)}')
print(f'A media dos numeros é {sum(lista)/5}')

