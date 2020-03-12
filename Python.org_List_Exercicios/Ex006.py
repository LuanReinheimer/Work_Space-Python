"""Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

notas = []
media = 0
soma = 0
mediamaiorque7 = []

for aluno in range(4):
    media = 0
    soma = 0
    for contagem in range(4):
        nota = int(input('Digite sua nota: '))
        soma = soma + nota
    media = soma / 4
    notas.append(media)
    print(notas)

for num in notas:
    if num >= 7.0:
        mediamaiorque7.append(num)

print(f'Tivemos {len(mediamaiorque7)} alunos com a media maior ou igual a 7 ')