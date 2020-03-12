"""Façaa um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

print("""Em que turno você estuda\nDigite M-matutino ou V-Vespertino ou N- Noturno""")


resposta = str(input('Turno: ')).strip().upper()
print('=-'*30)

if resposta == 'M':
    print('Bom dia!')
elif resposta == 'V':
    print('Boa tarde!')
elif resposta == 'N':
    print('Boa Noite')

else:
    print('Resposta invalida')

print('=-'*30)