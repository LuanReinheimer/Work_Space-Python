nome = str(input('Digite o seu nome: '))
print(f'Seu nome apenas com letras minusculas: ', nome.lower())

print(f'Seu nome apenas com letras MAIUSCULAS: ', nome.upper())

nome1 = nome.strip()
nome2 = nome1.split()

print(f'Seu nome possui', len(''.join(nome2)), 'caracteres.')
print(f'Seu nome primeiro possui ', end='')
print(len(nome2[0]))

