''' Faça um programa que leia um ângulo qualquer
    e mostre na tela o valor do seno, cosseno
    e tangente desse ângulo.    '''

from math import cos, sin, tan

print('Programa para descobrir Seno, Cosseno'
      ' e Tangente de um ângulo (x)')

x = float(input('Informe o valor do ângulo: '))

print(f'Seno do ângulo {x} é {sin(x) :.2f}')
print(f'Cosseno do ângulo {x} é {cos(x) :.2f}')
print(f'Tangente do ângulo {x} é {tan(x) :.2f}')
