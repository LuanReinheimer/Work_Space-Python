from time import sleep
compra = 238.90
saida = 0
# Desconto Á vista\ Débito
desconto1 = 0.05 * 238.90
desconto2 = 0.10 * 238.90
# Desconto Parcelamento
desconto3 = 0.20 * 238.90

print('''Revenda de pneus X, seu carrinho de R$ 238.90 esta fechado.
Selecione as opções de pagamento:
        [1] Á vista (Dinheiro ou Débito)
        [2] Parcelamento no cartão
        [0] Sair do programa''')

opcão = int(input('Selecione a opção desejada: '))

if opcão == 1:
    escolha = str(input('Debito ou no dinheiro? '))
    if escolha == 'debito':
        valor = (compra - desconto1)
        print(f'Pagando no DÉBITO tera 5% de desconto, ficando R$ {valor:.2f}')
    elif escolha == 'dinheiro':
        valor = (compra - desconto2)
        print(f'Pagando no DINHEIRO tera 10% de desconto, ficando R$ {valor:.2f}')

elif opcão == 2:
    print('''Deseja parcelar em quantas vezes?
        [1] 2x No cartão
        [2] 3x no cartão
        [3] 4x no cartão
        [4] 5x no cartão
        [5] 8x no cartão
        [6] 10x no cartão''')
    escolha = int(input('Selecione a opção de parcelamento:'))
    if escolha == 1:
        print(f'Pagando em 2x no cartão não possuira desconto ou juros, ficando R${compra}')
    elif escolha == 2:
        valor = (compra + desconto1)
        print(f'Pagando em 3x no cartão acrecentara 5% de juros, ficando R${valor:.2f}')
    elif escolha == 3:
        valor = (compra + desconto2)
        print(f'Pagando em 4x no cartão acrescentara 10% de juros, ficando R${valor:.2f}')
    else:
        valor = (compra + desconto3)
        print('Pagando parcelado acima de 4x cartão sofrera 20% de juros', end='')
        print(f'Sua fatura ficara R${valor}')

else:
    print('Cancelando compra...')
    sleep(1)
    print('Compra cancelada!')