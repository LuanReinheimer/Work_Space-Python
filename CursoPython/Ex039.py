idade = 2019 - int(input('Em que ano você nasceu? '))


if idade == 18:
    print(f'{idade} anos! Está na hora de se alistar!')

elif idade > 18:
    passou = idade - 18
    print(f'Já se passaram {passou} anos da data que você deveria se alistar...')

elif idade < 18:
    falta = 18 - idade
    print(f'Se acalme... Ainda faltam {falta} anos para seu alistamento voce possui {idade} anos...')