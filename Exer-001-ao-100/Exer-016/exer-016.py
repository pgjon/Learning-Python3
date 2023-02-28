
# importar a função trunc da math e nomeia como tr
from math import trunc as tr

num = float(input('Digite um numero real qualquer: '))

print(f'A porção inteira de {num} é {tr(num)}')
