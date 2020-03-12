"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""


# COM UMA LATA SE PINTA 54 metros.

tamanho = int(input('Metros a ser pintados: '))
litros = tamanho / 3

if tamanho % 54 == 0:
    latas = tamanho / 54
else:
    latas = int(tamanho / 54) + 1

preço_por_lata = latas * 80

print(f'Voce precisa comprar {latas:.0f} para pintar {tamanho}M', end=' ')
print(f'E vai pagar R$ {preço_por_lata:.2f} ')


