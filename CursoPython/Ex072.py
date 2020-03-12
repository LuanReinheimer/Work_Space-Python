"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso"""

contagem = ('Zero','Um','Dois','Tres',
          'Quatro', 'Cinco', 'Seis',
          'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Quatorze',
          'Quinze', 'Dezesseis', 'Dezessete', 'Dessoito',
          'Dessenove', 'Vinte')
lista = []

for i in range(20):
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero < 0:
        print('Numero fora do pedido.')
        break
    if numero > 20:
        print('Numero fora do pedido.')
        break
    else:
        lista.append(numero)
    print(f'Voce digitou {contagem[numero]}')


    print(f'Assim gerando uma lista de numeros digitados {lista}')
