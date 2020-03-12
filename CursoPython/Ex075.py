""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""


tupla_lida_pelo_teclado = (int(input('Digite um numero: ')), int(input('Digite mais um numero: ')),
                           int(input('Digite outro numero: ')), int(input('Digite o ultimo numero: ')))

print(f'Voce digitou {tupla_lida_pelo_teclado}')
print(f'O valor 9 apareceu {tupla_lida_pelo_teclado.count(9)} vezes')

if 3 not in tupla_lida_pelo_teclado:
    print('O Valor 3 não foi digitado em nenhuma poisição')

else:
    print(f'O valor 3 foi digitado na posição {tupla_lida_pelo_teclado.index(3)+1}º posição')

print('Os valores pares digitados:', end='')
for n in tupla_lida_pelo_teclado:
    if n % 2 == 0:
        print(n, end=' ')


