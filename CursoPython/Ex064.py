'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = 0
soma = -999
contador = -1
while num != 999:
    num = int(input('Digite um numero: [999 para sair]: '))
    soma = soma + num
    contador = contador + 1
print(f'Voce digitou {contador} numeros e a soma entre eles foi {soma}')