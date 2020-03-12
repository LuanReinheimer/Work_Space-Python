'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resp = 'S'
media = 0
soma = 0
contador = 0
parada = 0
maior = 0
menor = 0

while resp in 'Ss':
    num = int(input('Digite um numero: '))
    contador = contador + 1
    soma = soma + num
    media = soma / contador
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Ao final temos {contador} numeros digitados e a media de todos os numeros digitados de {media :.2f} ', end='')
print(f'e o maior nº é {maior} e o menor é {menor} respectivamente digitados')

