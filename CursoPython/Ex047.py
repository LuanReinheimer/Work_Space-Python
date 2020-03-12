
print('Os numero pares de 1 a 50 são')
for count in range(1, 50 + 1):
    if count % 2 == 0:
        print(f'{count}')
print('FIM')


# Outra maneira de resolver, ocupando menos o processador

print('Os numero pares de 1 a 50 são')
for count in range(2, 51, 2):
    print(count)
print('FIM')