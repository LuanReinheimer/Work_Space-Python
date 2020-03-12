print('Conversão de temperaturas graus Celsius para Fahrenheit')

c = float(input('Digite a temperatura em graus Celsius: '))
f = c * (9.0/5.0) + 32.0
print(f'A temperatura de °C {c} equivale a {f} FAHRENHEIT ')

print('='*50)

print('Conversão de temperaturas de Fahrenheit para graus Celsius')

f = float(input('Digite a temperatura em FAHRENHEIT: '))

c = 5.0*(f - 32.0)/9.0

print(f'A temperatura de {f} FAHRENHEIT equivale a  °C {c:.2f}')

print('='*50)