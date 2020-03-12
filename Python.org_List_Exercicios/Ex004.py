"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela.."""
notas = []

for i in range(4):
    notas.append(int(input('Digite sua nota: ')))

media = sum(notas)/4
print(f'A nota do aluno é {notas} e sua media é {media}')