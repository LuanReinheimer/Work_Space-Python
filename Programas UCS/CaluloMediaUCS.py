print('Calculo de Médias UCS EAD')

aluno = str(input('Qual seu nome ?'))

nota1 = float(input('Digite a Nota do Forum Avaliativo: '))
nota2 = float(input('Digite a Nota da Prova presencial: '))

notaua = 0

notaforum = nota1 * 0.2
notaprova = nota2 * 0.6


print('Voce ganhara mais dois pontos se completou o todas as aulas em 100%')
ua = str(input('Se Completou todas as UAS 100% digite (sim) ? '))

if ua == 'sim':
    print(f'Certo!! Vamos adicionar mais 2 pontos a sua nota')
    notaua = notaua + 2


elif ua == 'nao':
    print('Nao sera adicionado 2 pontos em sua nota total')
    notaua = notaua + 0

else:
    print('Ok, não sera adicionado nada em sua nota')
    notaua = notaua + 0

notafinal = notaforum + notaprova + notaua

print(f'Média =  {notafinal :.2f}')

if notafinal >= 6:
    print(f'\x1b[32m{aluno} Voce foi Aprovado!!')

else:
    print(f'\x1b[31m{aluno} sua nota foi {notafinal:.2f} e deverar agendar a reucuperação')
