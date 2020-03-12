"""Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

frase = str(input('Digite uma frase: ')). strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(f'Voce digitou a frase {frase}')
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo!')

# Outra maneira de resolver sem utilizarmos o FOR, É COM O FATIAMENTO DA STRING

frase = str(input('Digite uma frase: ')). strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo!')

# Outra maneira de resolver sem utilizarmos o FOR, É COM O FATIAMENTO DA STRING

x1 = input("Digite uma frase ").replace(" ","")
x2 = x1.replace(" ","")[::-1]

if(x1 == x2):
    print(f"Temos um palindromo")
else:
    print("foi diferente")