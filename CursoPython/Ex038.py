a = int(input(f'Digite o primeiro inteiro: '))
b = int(input(f'Digite o segundo inteiro: '))
menor = b
maior = a
if a > b:
    print('O primeiro numero é maior que o segundo')

elif a < b:
    print('O segundo numero e maior que o primeiro')

iguais = maior
if maior == menor and menor == maior:
    iguais = menor
    print(f'Nao existe maior pois todos são iguais')

