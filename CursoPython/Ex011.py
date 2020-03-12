print('Calculo para pintura')


altura = float(input(f'Qual a altura da parede? '))
largura = float(input(f'Qual a largura desta parede? '))
area = largura * altura
print(f'Sua parede possui {largura}x{altura} e sua area é de {area :.2f}m² ')
tinta = area / 2
print(f'Para voce poder pintar ira utilizar {tinta}L de tinta ')

