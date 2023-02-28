
from math import cos, radians, sin, tan

print('Programa para descobrir Seno, Cosseno'
      ' e Tangente de um ângulo (x)')

x = float(input('Informe o valor do ângulo: '))
seno = sin(radians(x))
cosseno = cos(radians(x))
tangente = tan(radians(x))

print(f'Seno do ângulo {x}º é {seno :.2f}')
print(f'Cosseno do ângulo {x}º é {cosseno :.2f}')
print(f'Tangente do ângulo {x}º é {tangente :.2f}')
