"""No livro Make Way for Ducklings de Robert McCloskey, os patinhos são chamados de Jack, Kack, Lack, Mack, Nack, Ouack, Pack, e Quack. Esse laço tenta imprimir esses nomes ordenadamente.

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)
é claro que esse programa tem problemas pois Ouack e Quack não são escritos corretamente. Você consegue consertar o programa?"""


prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if prefixes[7] in p:
        print(p + 'u' + suffix)
        continue
    if prefixes[5] in p:
        print(p + 'u' + suffix)
        continue
    print(p + suffix)