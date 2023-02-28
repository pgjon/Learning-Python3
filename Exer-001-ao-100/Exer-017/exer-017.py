
from math import hypot as hy

print('Programa para calcular Hipotenusa')

co = float(input('Digite o valor do CO: '))
ca = float(input('Digite o valor do CA: '))

hi = hy(co, ca)

print(f'A hipotenusa vale: {hi :.2f}')
