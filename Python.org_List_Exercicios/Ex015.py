"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo"""

string1 = "Brasil Hexa 2006"
string2 = "Brasil! Hexa 2006!"

print(f'{string1} - Possui ',(len(string1),'Caracteres'))

print(f'{string2} - Possui',(len(string2),'Caracteres'))

if len(string1) != len(string2):
    print('As duas strings são de tamanhos diferentes')
else:
    print('As duas strings são de tamanhos iguais')

if string2 == string1:
    print('As duas strings possuem conteúdo iguais ')
else:
    print('As duas strings possuem conteúdo diferente')
