print('Programa de aprovamento de emprestimo')

valorcasa = int(input('Qual o valor da casa: R$ '))

salario = int(input('Qual o seu atual salario: R$ '))
minimo = salario * 30 / 100
pagamentoAnos = int(input('Em quanto tempo em anos para pagar: '))
prestaçãoMensal =  valorcasa / (pagamentoAnos * 12)

if prestaçãoMensal <= minimo:
    print(f'Emprestimo APROVADO!, Para o emprestimo de R${valorcasa} voce pagara R$ {prestaçãoMensal  :.2f}', end='')
    print(f' ao mes em {pagamentoAnos} anos')

elif prestaçãoMensal > minimo:
    print(f'Emprestimo NEGADO!, pois a parcela exede a 30% do seu salário')