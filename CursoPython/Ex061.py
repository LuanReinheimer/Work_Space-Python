'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while'''

primeirotermo = int(input(f'Primeiro Termo: '))
rarzao = int(input(f'Razão: '))
d = primeirotermo + (11-1) * rarzao
dez = 1
print(f'{primeirotermo} → ', end='')
while dez <= 10:
   primeirotermo = primeirotermo + rarzao
   print(f'{primeirotermo} → ', end='')
   dez = dez + 1
print('Acabou!')