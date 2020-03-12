from time import sleep

print('Calculo de aumento de salario')

salary = float(input('Digite o seu salario atual R$: '))

print('Calculando Aumento...')
sleep(1)

if salary <= 1250:
    aumento = (salary * 0.15)
    print(f'O seu salario de R${salary} teve um reajuste de 15% e passa a ser R${aumento + salary}')

elif salary > 1250:
    aumento = (salary * 0.10)
    print(f'O seu salario de R${salary} teve um reajuste de 10% e passa a ser R${aumento + salary}')