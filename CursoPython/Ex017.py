import math

o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(o, a)

print(f'A hipotenusa vai medir {h:.2f}')
