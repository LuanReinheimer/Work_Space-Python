"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""


tabela_brasileirão = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',  'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí', )

print(f'Segue a lista de times do Brasileirão: {tabela_brasileirão}')
print(f'Os 5º primeiros colocados são : {tabela_brasileirão[0:5]}')
print(f'Os 4º ultimos colocados são: {tabela_brasileirão[16:]}')
print(f'Times em ordem alfabetica: {sorted(tabela_brasileirão)}')
print(f'O time Chapecoense esta na {tabela_brasileirão.index("Chapecoense")}º posição.')