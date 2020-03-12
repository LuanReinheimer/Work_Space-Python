'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
quando ele disser que quer mostrar 0 termos.'''

primeirotermo = int(input(f'Primeiro Termo: '))
rarzao = int(input(f'Razão: '))
total = 0
primeirotermo_novamente = 10
dez = 1

while primeirotermo_novamente != 0:
   total = total + primeirotermo_novamente
   while dez <= total:
      primeirotermo = primeirotermo + rarzao
      print(f'{primeirotermo} → ', end='')
      dez = dez + 1
   print('pausa')
   primeirotermo_novamente = int(input('Deseja mostrar mais alguns termos? '))
print(f'Finalizamos com {total} de termos')



