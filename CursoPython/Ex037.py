print('Bem vindo ao conversor de Bases Numericas ')

num = int(input('Digite um inteiro: '))

print('''Escolha uma das bases para convertermos
[1] Base Binaria
[2] Base Octal
[3] Base Hexadecimal''')

int(input('Sua opção: '))

if num == 1:
    print(f'A Base Binaria de {num} é {bin(num)}')
elif num == 2:
    print(f'A Base Octal de {num} é {oct(num)}')
elif num == 3:
    print(f'A Base Hexadecimal de {num} è {hex(num)}')
else:
    print('Opção invalida')



