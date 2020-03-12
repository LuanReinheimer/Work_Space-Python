#===================================== Maneira mais complexa ===============================================
# print(f'Maior e menor')

# maior = -1000000
# menor = 1000000

# a = int(input(f'Digite o primeiro inteiro: '))
# b = int(input(f'Digite o segundo inteiro: '))
# c = int(input(f'Digite o terceiro inteiro: '))

# if a > maior:
    #maior = a
# if a < menor:
    #menor = a

# if b > maior:
    #maior = b
# if b < menor:
    #menor = b

# if c > maior:
    #maior = c
# if c < menor:
    #menor = c

# print(f'O maior é o Nº{maior}')
# print(f'O menor é o Nº{menor}')
# ===================================== Maneira mais facil com menos codigo ===========================================

a = int(input(f'Digite o primeiro inteiro: '))
b = int(input(f'Digite o segundo inteiro: '))
c = int(input(f'Digite o terceiro inteiro: '))

# Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Veirificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

# Imprimindo
print(f'O maior é o Nº{maior}')
print(f'O menor é o Nº{menor}')
