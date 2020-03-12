import math

A = float(input('informe o valor do angulo: '))

c = math.cos(math.radians(A))
s = math.sin(math.radians(A))
t = math.tan(math.radians(A))


print(f'Um angulo de {A}° Digitado possui:\nCosseno: {c:.2f}\nSeno: {s:.3f}\nTangente: {t:.2f}')


print('=' * 150 )

print(f'Outra maneira mais simples é utilizarmos o (from import) veja abaixo;')

print('=' * 150 )

from math import radians, sin, cos, tan

A = float(input('informe o valor do angulo: '))

c = cos(radians(A))
s = sin(radians(A))
t = tan(radians(A))

print(f'Um angulo de {A}° Digitado possui:\nCosseno: {c:.2f}\nSeno: {s:.3f}\nTangente: {t:.2f}')