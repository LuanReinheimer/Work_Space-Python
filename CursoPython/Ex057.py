''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
 peça a digitação novamente até ter um valor correto '''

while True:
    print('''Digite o seu sexo:
    [1] Masculino
    [2] Feminino''')
    sexo = str(input('Digite a opção: '))

    if sexo == '1':
        print(f'O seu sexo é Masculino')
        break
    elif sexo == '2':
        print(f'O seu sexo é Feminino')
        break
    else:
        print('O isto não é um sexo valido')


# Outra forma de resolver.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida. Tente novamente')