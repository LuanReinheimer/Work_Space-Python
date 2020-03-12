
primeiro = int(input(f'Primeiro Termo: '))
razao = int(input(f'Razão: '))
decimo = primeiro + (11-1) * razao
for c in range(primeiro, decimo, razao):
    print(f'{c} ', end='-> ')
print('Acabou')