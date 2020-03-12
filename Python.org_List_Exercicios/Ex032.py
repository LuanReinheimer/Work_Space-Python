"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E"""

nota1 = (float(input('Digite sua nota: ')))
nota2 = (float(input('Digite sua nota: ')))
a = 0
b = 0
c = 0
d = 0
e = 0

media = (nota1 + nota2)/2
if media >= 9.0 and media <= 10:
    print(f'Sua media foi de {media:.2f} - CONCEITO A')
    a = a + 1
elif media >= 7.5 and media <= 9.0:
    print(f'Sua media foi de {media:.2f} - CONCEITO B')
    b = b + 1
elif media >= 6.0 and media <= 7.5:
    print(f'Sua media foi de {media:.2f} - CONCEITO C')
    c = c + 1
elif media >= 4.0 and media <= 6.0:
    print(f'Sua media foi de {media:.2f} - CONCEITO D')
    d = d + 1
elif media >= 0 and media <= 4.0:
    print(f'Sua media foi de {media:.2f} - CONCEITO E')
    e = e + 1

if a == 1:
    print('APROVADO!!')
elif b == 1:
    print('APROVADO!!')
elif c == 1:
    print('APROVADO!!')
elif d == 1:
    print('REPROVADO!!!')
elif e == 1:
    print('REPROVADO!!!')

