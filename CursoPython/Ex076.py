tabela_de_compra = ('Guidão', 200.95, 'Manetes', 180.30, 'Capa de Banco', 50)

print('=-'*30)
print('LISTAGEM DE PREÇOS')
print('=-'*30)

# Forma 1
for c in tabela_de_compra:
    print(f'{tabela_de_compra[0]}', end=f"{'.'*15}R$ ")
    print(f'{tabela_de_compra[1]:.2f}')
    print(f'{tabela_de_compra[2]}', end=f"{'.'*14}R$ ")
    print(f'{tabela_de_compra[3]:.2f}')
    print(f'{tabela_de_compra[4]}', end=f"{'.'*8}R$ ")
    print(f'{tabela_de_compra[5]:.2f}')
    break
print('=-'*30)


# Forma 2

for posicao in range(0, len(tabela_de_compra)):
    if posicao % 2 == 0:
        print(f'{tabela_de_compra[posicao]:.<30}', end='')
    else:
        print(f'R${tabela_de_compra[posicao]:>7.2f}')
print('=-'*30)