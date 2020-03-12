pessoas = [['lucas',23], ['luan',23], ['bebeto', 25]]

for nome in pessoas:
    print(f' {nome[0]} tem {nome[1]} anos de idade. ')
#-----------------------------------------------------------------------------

galera = []
dado = []

totalmaior = 0
totalmenor = 0

for c in range(5):
    dado.append(str(input('NOME: ')))
    dado.append(int(input('IDADE: ')))
    galera.append(dado.copy())
    dado.clear()
print(f'A Galera da lista é {galera}')

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior = totalmaior + 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor = totalmenor = 1
print(f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade.')