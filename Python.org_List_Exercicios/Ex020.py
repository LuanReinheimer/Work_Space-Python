"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""


tamanho_do_dowload = int(input('Tamanho de um arquivo para download em MB: '))
velocidade_internet = int(input('Velocidade de um link de Internet em Mbps:'))
# Conversão de MB para KB/s

resultado_convercao = velocidade_internet * 1024
taxa_de_transferencia = resultado_convercao / 8

# Tempo de Download

calculo_tamanho = tamanho_do_dowload * 1024
taxa_tempo = calculo_tamanho / taxa_de_transferencia

# Velocidade da internet

calculo_seguntos = calculo_tamanho/128
calculo_minutos = taxa_tempo/60


print(f'A sua internet de {velocidade_internet}MB tem a velocidade de dowload de {taxa_de_transferencia} KBps', end=' ')
print(f'E baixa um arquivo de {tamanho_do_dowload} MB em {calculo_minutos:.2f} minutos ou {calculo_seguntos:.2f} segundos')