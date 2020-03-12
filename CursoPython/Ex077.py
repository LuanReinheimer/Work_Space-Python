"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

tupla_cafe = ('pao', 'ovo', 'leite', 'margarina', 'nata', 'geleia')

print(tupla_cafe)

for itens_cafe in tupla_cafe:                                   # para 'itens_cafe em 'tupla_cafe'
    print(f'\nNa palavra {itens_cafe.lower()} temos', end=' ')  # imprima em laço até o final da tupla
    for letra in itens_cafe:                                    # para 'letra' em 'itens_café'
        if letra in 'aeiou':                                    # se 'letra' possui 'aeiou'
            print(letra, end=' ')                               # imprima 'letra'
