nome = str(input(f'Digite seu nome:'))

salary = float(input(f' {nome} Informe o seu salario atual R$'))

desconto = 0.15 * salary

print(f'O seu salario de R${salary} teve um abono mensal de 15%, então vai passar a ser R${salary + desconto :.2f}')
