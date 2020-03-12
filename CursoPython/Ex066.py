'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
o final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

num = 0
soma = 0
contador = 0
while True:
    num = int(input('Digite um numero: [999 para sair]: '))
    soma = soma + num
    if num == 999:
        break
    contador = contador + 1
print(f'Voce digitou {contador} numeros e a soma entre eles foi {soma}')