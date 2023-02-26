# Ex. calculo raiz quadrada utilizando biblioteca math

import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print(f'A raiz quadrada de {num} é {raiz :.2f}.')

print(f'A raiz quadrada de {num} arredondada para cima vale'
      f' {math.ceil(raiz)}.')

print(f'A raiz quadrada de {num} arredondada para baixo vale'
      f' {math.floor(raiz)}.')

''' Outra maneira de fazer

from math import sqrt, ceil, floor   # -> importa as funções sqrt,
                             ceil e floor da biblioteca math.

num = int(input('Digite um número: '))

raiz = sqrt(num)        # -> não há necessidade de utilizar
                            math.sqrt(num) como na linha 7

print(f'A raiz quadrada de {num} é {raiz :.2f}.')

print(f'A raiz quadrada de {num} arredondada para cima vale'
      f' {ceil(raiz)}.')

print(f'A raiz quadrada de {num} arredondada para baixo vale'
      f' {floor(raiz)}.')

'''
