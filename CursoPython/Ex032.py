from datetime import date
print('Porgrama para descobrir se o ano é BISSEXTO')

ano = int(input('Qual ano deseja analisar? ou digite 0 para analisar o ano autal: '))

if ano == 0:
    ano = date.today().year
    print(f'O {ano} digitado é BISSEXTO!')

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O {ano} digitado é BISSEXTO!')

else:
    print(f'O {ano} digitado NÃO É BISSEXTO!')