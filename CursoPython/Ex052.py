
for count in range(1, 3):
    num = int(input(f'Digite {count} aqui : '))
    if num == 1:
        print(f'O {num} Não é primo')
    elif num == 2:
        print(f'O {num} É primo')
    elif num % 2 == 1:
        print(f'O {num} É primo')
    else:
        print(f'O {num} Não primo')
print(f'Fim')

# Outra maneira de resolver, ocupando menos o processador


num = int(input('Digite um número: '))
primo = 0
for verif in range(1, num + 1):
    if num % verif == 0:
        primo += 1
if primo == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')