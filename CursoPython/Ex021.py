import playsound
from random import randint

print('Bem vindo a playlist Python')

nome = input(f'Aperte qualquer coisa para dar PLAY! e tocar aleatoriamente:  ')

nome = randint(0, 3)
if nome == 1:
    print('Tocando Gareth Emery & Emma Hewitt - Take Everything')
    audio1 = playsound.playsound('ex021.mp3')
elif nome == 2:
    print('Tocando Linkin Park - In The End (Mellen Gi & Tommee Profitt Remix)')
    audio1 = playsound.playsound('ex02101.mp3')
