somapares = 0
print('Digite Seis numeros  ')
for count in range(1, 7):
    num = int(input(f'Digite {count} aqui : '))
    if num % 2 == 0:
        somapares = somapares + num
print(f'{somapares}')