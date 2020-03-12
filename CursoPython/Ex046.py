from time import sleep

import playsound

for i in range(1):
    print(5)
    sleep(1)
    print(4)
    sleep(1)
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)
print('E que comece o batidão!!')
audio1 = playsound.playsound('ex021.mp3')

# Outra maneira Pythonico de realizar

for count in range(10, -1, -1):
    print(count)
    sleep(1)
print('E que comece o batidão!!')
audio1 = playsound.playsound('ex021.mp3')