import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

posicao = random.randint(0, 4)

print(f'Então o aluno {lista[posicao]} escolhido tera que apagar o quadro após o fim da aula')