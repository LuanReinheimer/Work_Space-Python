"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

print("""Digite seu sexo conforme abaixo
        [M] Masculino
        [F] Feminino""")

sexo = str(input('Sexo: ')).upper()

if sexo =='M':
    print('Sexo Masculino')
elif sexo == 'F':
    print('Sexo Feminino')
else:
    print('Sexo invalido')