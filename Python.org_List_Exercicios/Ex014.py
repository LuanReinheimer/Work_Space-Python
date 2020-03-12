"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
 O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:"""

numeroslidos = []

while True:
    tabuada = (int(input('Digite um numero para mostrar sua tabuada: ')))
    numeroslidos.append(tabuada)
    resultado = 0
    print(f'Tabuada do {tabuada}:')
    print('-='*30)
    for num in range(1,10):
        resultado = tabuada * num
        print(f'{tabuada} x {num}: {resultado}')

    outra = str(input('Deseja saber a tabuda de outro numero? ')).strip().upper()[0]
    if outra in 'Nn':
        break

print(f'Voce olhou a tabuada de {len(numeroslidos)} numero/s e a lista dos numeros é {numeroslidos}')