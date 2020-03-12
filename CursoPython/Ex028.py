from random import randint
from time import sleep

print('Bem vindo ao jogo de adivinha, tente adivinhar de 0 a 20 qual numero é o que eu vou sortear')
print('-'*50)
computador = randint(0, 20)
print(f'Pensando...')
sleep(2)
print('-'*50)

num = int(input('Pronto! ja escolhi o numero, pode digitar o nº que voce acha que eu estou escondendo:'))
if (num == computador):
    print('Voce acertou!!')

else:
    print(f'NÃO FOI DESTA VEZ, o nº escolhido foi {computador}')



