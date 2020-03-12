"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes"""
lista_letras = []
consoantes = 0


for letra in range(10):
    lista_letras.append((input('Digite uma letra: ')))
    letras = (lista_letras[letra])
    if letras not in ('a', 'e', 'i', 'o', 'u'):
        consoantes = consoantes + 1

print(lista_letras)
print(f'foram lidas {consoantes} consoantes')
