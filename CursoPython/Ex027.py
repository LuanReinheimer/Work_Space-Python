nome = str(input('Digite seu nome completo: ')).strip()
nome2 = nome.title()
nome3 = nome2.split()
print(f'O seu primeiro nome é: ', nome3[0])
print(f'O seu ultimo nome é: ', nome3[-1])