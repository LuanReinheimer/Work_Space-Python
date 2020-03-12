"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo"""

tabuada = int(input('Digite um numero para saber a sua tabuada: '))
print(f'Tabuada do {tabuada}:')
print('-=' * 30)
for num in range(1, 11):
    resultado = tabuada * num
    print(f'{tabuada} x {num}: {resultado}')