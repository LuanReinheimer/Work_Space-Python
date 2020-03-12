from time import sleep

print(f'Programa para descobrir se seu nº é PAR ou IMPAR')

num = int(input(f'Digite qualquer Inteiro para o computador verificar se ele é PAR ou IMPAR:'))

print(f'Analisando...')
sleep(2)

if num % 2 == 0:
    print(f'O Nº {num} é PAR.')

else:
    print(f'O Nº {num} é IMPAR')