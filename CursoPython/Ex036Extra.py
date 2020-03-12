from time import sleep

print('Bem vindo ao Posto de combustivel!!')

print('=' * 50)
a = 3.90
g = 4.90

desconto1A = 0.04 * a
desconto2A = 0.06 * a

desconto1g = 0.03 * g
desconto2g = 0.06 * g

combustivel = str(input('Alcool ou gasolina? '))

if combustivel == 'g' or'G':
    print('Ok')

    litros = float(input('Quantos litros ? '))
    print('Abastecendo...')
    sleep(2)

    if litros <= 20:
        a = (g - desconto1g) * litros

        print(f'Voce abasteceu {litros}L e tera 3% de desconto, pagara R$ {a:.2f} ')

    elif litros > 20:
        b = (g - desconto2g) * litros
        print(f'Voce abasteceu {litros}L e tera 6% de desconto, pagara R$ {b - desconto2g:.2f} ')

elif combustivel == 'A' or 'a':
    print('OK')

    litros = float(input('Quantos litros ? '))
    print('Abastecendo...')
    sleep(2)

    if litros <= 20:
        a = (a * desconto1A) * litros
        print(f'Voce abasteceu {litros}L e tera 4% de desconto, pagara R$ {a:.2f} ')

    elif litros > 20:
        b = (a * desconto2A) * litros
        print(f'Voce abasteceu {litros}L e tera 6% de desconto, pagara R$ {b:.2f} ')