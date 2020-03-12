frase = str(input('Digite uma frase:')).strip()
frase2 = frase.upper()

print(f'A letra ''A'' aparece', frase2.count('A'), 'vez na sua frase')
print(f'A primeira vez que a pareceu "A" foi na possição', frase2.find('A')+1)
print(f'A ultima vez que apareceu a letra "A" foi na posição', frase2.rfind('A')+1)
