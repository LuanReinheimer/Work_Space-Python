"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

galera = []
dado = []

maispesada = 0
menospesada = 0

while True:
    dado.append(str(input('NOME: ')))
    dado.append(float(input('PESO: ')))
    if len(galera) == 0:
        maispesada = menospesada = dado[1]
    else:
        if dado[1] > maispesada:
            maispesada = dado[1]
        if dado[1] < maispesada:
            menospesada = dado[1]
    galera.append(dado.copy())
    dado.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

print(f'fora cadastrados {len(galera)} pessoas ')
print(f'A pessoa mais pesada é foi de {maispesada}kg, as pessoas foram ', end='')
for p in galera:
    if p[1] == maispesada:
        print(f'{p[0]}')
print(f'A pessoa menos pesada é de {menospesada}kg, as pessoas foram ', end='')
for p in galera:
    if p[1] == menospesada:
        print(f'{p[0]}')


