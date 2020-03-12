"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:"""

carga_horaria_diaria = 10
mes = 22

hora = float(input("Quanto ganha por hora: "))
salario_bruto = hora * carga_horaria_diaria * mes

imposto_de_renda = salario_bruto * 0.08
inss = salario_bruto * 0.11
sindicato = salario_bruto * 0.05


print("-="*20)

print(f'Seu salario bruto no mes sera de R$ {salario_bruto}')
if salario_bruto > 2200:
    print(f'Voce teve que pagar imposto de renda de R${imposto_de_renda:.2f}')
print(f'Voce pagou ao inss R$ {inss:.2f}')
print(f'Voce pagou ao sindicato R$ {sindicato:.2f}')
print("-="*20)

salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)
print(f'Então o seu salario liquido no mes sera de R$ {salario_liquido}')





