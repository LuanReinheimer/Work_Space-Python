"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

sexo = ''
nome = ''
estado_civil = ''
salario = 0
idade = 0

while True:
    nome = str(input('Digite seu nome: '))
    if len(nome) <= 3:
        print('Para realizar o cadastro seu nome precisa ter mais de 3 caractere.')
        continue
    else:
        print('NOME CADASTRADO')
    while True:
        idade = int(input('Digite sua idade: '))
        if idade < 0 or idade > 150:
            print('Para realizar o cadastro sua idade tem que ser entre 0 e 150 ')
            continue
        else:
            print('CADASTRADO')

        while True:
            salario = float(input('Digite seu salario: '))
            if salario <= 0:
                print('Seu salario tem que ser maior que 0')
                continue
            else:
                print('SALARIO CADASTRADO')

            while True:
                sexo = str(input('Digite seu sexo entre F/M: ')).upper()
                if sexo != 'F' and sexo != 'M':
                    print('Digite F= feminino ou M= masculino')
                    continue
                else:
                    print('SEXO CADASTRADO')

                while True:
                    estado_civil = str(input('Digite seu estado civil: ')).lower()
                    if estado_civil == 's' and 'c' and 'v' and 'd':
                        print('ESTADO CIVIL CADASTRADO ')
                    else:
                        print('Difite o estado civil s=solteiro c=casado v=viuvo d=seila')

print(f'Seu nome é {nome} do sexo {sexo} e sua idade é {idade}')

print(f'voce ganha R${salario} e seu estado civil é de {estado_civil}')


