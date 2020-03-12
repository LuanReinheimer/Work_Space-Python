"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues."""

print('-=' * 30)

print('Caixa eletronico')

print('-=' * 30)


valorsaque = int(input('Que valor voce deseja sacar R$: '))
totalmontante = valorsaque
cedula = 50
total_de_ced = 0

while True:
    if totalmontante >= cedula:
        totalmontante = totalmontante - cedula
        total_de_ced = total_de_ced + 1
    else:
        if total_de_ced > 0:
            print(f'Total de {total_de_ced} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_de_ced = 0
        if totalmontante == 0:
            break
print('-='*30)
print('Fim do programa')


