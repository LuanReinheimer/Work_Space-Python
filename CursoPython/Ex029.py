print(f'---Nota de velocidade e respectivo calculo de multa acrecentado\n----se a velocidade foi exedida.----')

velocidade = float(input(f'----Qual a velocidade consta em sua notificação: '))

print('=' * 50)

if velocidade > 80:
    multa = (velocidade-80) * 7
    print(f'\x1b[31mMULTADO! Voce esta acima da velocidade permitida sua multa é de R${multa :.2f}')
    print('Tenha um bom dia!')

else:
    print(f'\x1b[36mVoce esta dentro do limite permitido, não havera acrescimo de multa.')
    print('Tenha um bom dia!')

print('=' * 50)
