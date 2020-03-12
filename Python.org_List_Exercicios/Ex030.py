"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

ajuste20 = 0.20
ajuste15 = 0.15
ajuste10 = 0.10
ajuste05 = 0.05


print('-='*3,'Programa que calculará os reajustes','-='*3)

salario = float(input('Digite seu salario R$: '))

if salario <= 280.00:
    salarioajustado = salario * 0.20
    print(f'Seu salario de {salario} teve um aumento de 20% e passou a ser {salarioajustado + salario}')

elif salario > 280.00 and salario <= 700.00:
    salarioajustado = salario * 0.15
    print(f'Seu salario de {salario} teve um aumento de 15% e passou a ser {salarioajustado + salario}')

elif salario > 700.00 and salario <= 1500:
    salarioajustado = salario * 0.10
    print(f'Seu salario de {salario} teve um aumento de 10% e passou a ser {salarioajustado + salario}')
else:
    salarioajustado = salario * 0.05
    print(f'Seu salario de {salario} teve um aumento de 5% e passou a ser {salarioajustado + salario}')

