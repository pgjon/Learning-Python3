
from random import randint as rd
from time import sleep as sl

print('\033[34m-==-\033[m' * 14)
print('\033[32m Vou pensar em um número entre \033[1;31m0\033[m \033[32me '
      '\033[1;31m5\033[m\033[32m. Tente advinhar...\033[m')
print('\033[34m-==-\033[m' * 14)

numPC = rd(0, 5)  # PC escolhe um número entre 0 e 5

# usuário escolhe um número
numero = int(input('Escolha um número entre 0 e 5: '))
print('\033[33mPROCESSANDO...\033[m')
sl(3)  # aguarda 3 segundos

if numero == numPC:
    print('\033[1;32mPARABÉNS!\033[m Você \033[1;32mACERTOU!!\033[m')
    print(f'Número escolhido: \033[32m{numero}\033[m')
else:
    print('Que \033[1;31mPENA!\033[m Você \033[1;31mERROU!!\033[m')
    print(f'Número escolhido por você: \033[31m{numero}\033[m')
    print(f'Número escolhido por mim: \033[32m{numPC}\n\033[m')
