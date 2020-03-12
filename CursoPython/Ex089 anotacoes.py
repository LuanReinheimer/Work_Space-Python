
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita.values())
print(receita.keys())
print(receita.items())





# Adicionando dicionarios dentro de listas:

brazil = []
estado = {}


for c in range(0 ,3):
    estado['UF'] = str(input(f'Unidade Federativa: '))
    estado['Sigla'] = str(input(f'Sigla do estado: '))
    print('- ' *4 ,'Outro Estado' ,'- ' *4)
    brazil.append(estado.copy())

print(brazil)
