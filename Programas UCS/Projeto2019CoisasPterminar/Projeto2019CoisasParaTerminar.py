import csv
import random


cadastro =[]
jogador=[]
lista_jogador=[]
listaCompleta=[]
erros=0
acertos=0
pontos=0
total_pontos=0
perguntas=0
leitores=0
contador=0
ini=0


#  Print do MENU ======================================================================================================
def menu():
    print( '\x1b[32m \n!!!Bem vindo ao jogo do QUIZ!!!' )
    print( '\x1b[39m \nMenu:' )
    print( '0. Sair: ' )
    print( '1. Cadastrar jogador: ' )
    print( '2. Jogadores cadastrados e respectiva pontuação: ' )
    print( '3. Jogador que possui a maior pontuação:' )
    print( '4. Iniciar um quiz: ' )
    enter=input( 'Digite a opçao desejada: ' )
    return enter


#  funçoes do MENU ====================================================================================================
opcao = menu()

while opcao != '6':

    # opção1 ==============================================================================================================
    if opcao == '1':
        nome=str( input( 'Digite seu nome:' ) )
        msg=['\n', nome, ]
        arq=open( 'cadastro.csv', 'a' )
        arq.writelines( msg )
        print( 'jogador Matriculado' )
        arq.close()
        pass

    # opção2 =============================================================================================================
    if opcao == '2':
        print( 'Jogadores cadastrados e respectiva pontuação' )
        arquivoCSV=open( 'list_jogador.csv', 'r' )
        leitor=csv.reader( arquivoCSV, delimiter=';' )

        for linha in leitor:
            print( linha )
        arquivoCSV.close()
        pass

    # opção3 ==============================================================================================================
    if opcao == '3':
        linha = list()
        nome = pontos = (0)
        print( 'O jogador com maior placar é :' )
        arquivoCSV=open( 'list_jogador.csv', 'r' )
        leitor=csv.reader( arquivoCSV, delimiter=';' )
        for linha in leitor:
            for linha in range( 0 ):
               print(f'nome{linha}:')
        else:
               print(f'pontos{linha}: ')

        print(max(f'nome{0},pontos{0}'))

    # opção4 ==============================================================================================================
    if opcao == '4':
        cadastro=str( input( 'digite seu nome:' ) )
        print( 'iniciar quiz ' )


        def quiz():

            global pontos
            quizFile=open( 'perguntasERespostas.CSV', 'r' )
            quizData=quizFile.readlines()
            random.shuffle( quizData )
            questionno=1
            pontos=0

            for i in range( 5 ):
                x=quizData[i].strip()
                data=x.split( ';' )
                questao=data[0]
                resposta_correta=data[4]

                print( '\x1b[33m \nQuestion #', questionno )
                print( questao )

                print( 'alternativa 1:' )
                print( data[1], '.' )
                print( 'alternativa 2:' )
                print( data[2], '.' )
                print( 'alternativa 3:' )
                print( data[3], '.' )
                print( "\nResposta Correta: ", data[4] )
                resposta=input( '\n-->Digite a resposta correta: ' )

                if resposta == data[4]:
                    print( '\x1b[32m ***correto!***' )
                    pontos=pontos + 20
                    print( 'Você já tem: ', pontos )
                    questionno=questionno + 1
                    print()

                else:
                    print( '\x1b[31m ===incorreto!!!===' )
                    print( '\t===Não fez nenhum ponto!===' )
                    print( 'A resposta correta deve ser: ' + resposta_correta )
                    questionno=questionno + 1
                print()

            pontos=(pontos + 0) + pontos
            print( "\x1b[36m ", " Seu total de pontos desta vez foi: ", pontos )

            jogadores=([f'\n {cadastro};{pontos,total_pontos}'])
            arquivoCSV=open( 'list_jogador.csv', 'a' )
            arquivoCSV.writelines( jogadores )

            arquivoCSV.close()


            pass




        quiz()
    salvar_cadastro=()
    opcao=menu()
