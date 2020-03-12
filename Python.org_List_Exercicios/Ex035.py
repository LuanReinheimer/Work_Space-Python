"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""


while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota >= 0 and nota <= 10:
        print('nota valida!')
        break
    else:
        print('nota invalida!, digite apenas nota de 0 a 10.')

# =====================================================================================================================
#Forma2

nota = int(input('Digite uma nota entre 0 e 10: '))
while (nota < 0) or (nota > 10):
    nota = int(input('Digite uma nota entre 0 e 10: '))
    print('Nota invalida, digite apenas nota de 0 a 10.')
print('nota valida!')