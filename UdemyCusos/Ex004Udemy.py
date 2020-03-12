def par_impar(numero):
    if numero % 2 != 0:
        return 'Impar'
    return 'Par'



print(f'Informe um numero : ')


print(par_impar((int(input()))))
