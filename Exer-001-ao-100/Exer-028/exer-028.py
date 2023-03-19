
from random import randint as rd
from time import sleep as sl

print('-==-' * 14)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-==-' * 14)

numPC = rd(0, 5)  # PC escolhe um número entre 0 e 5

# usuário escolhe um número
numero = int(input('Escolha um número entre 0 e 5: '))
print('PROCESSANDO...')
sl(3)  # aguarda 3 segundos

if numero == numPC:
    print('PARABÉNS! Você acertou!')
    print(f'Número escolhido: {numero}')
else:
    print('Que pena! Você errou!')
    print(f'Número escolhido por você: {numero}')
    print(f'Número escolhido por mim: {numPC}\n')
