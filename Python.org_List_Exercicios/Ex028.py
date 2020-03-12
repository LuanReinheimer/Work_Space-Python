"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

a = int(input('Digite o primeiro num: '))
b = int(input('Digite o segundo num: '))
c = int(input('Digite o terceirp num: '))

if a > b > c:
    print(f'{a,b,c}')
elif b > a > c:
    print(f'{b,a,c}')
elif c > b > a:
    print(f'{c, b, a}')