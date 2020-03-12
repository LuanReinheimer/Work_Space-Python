print('Calculo de média.')


nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = nota1 + nota2 / 2

if media < 5:
    print("REPROVADO")

elif media <= 5 and 6.9:
    print('RECUPERAÇÃO')

elif media >= 7:
    print('APROVADO!!')

print(f'Voce ficou com a média {media}')