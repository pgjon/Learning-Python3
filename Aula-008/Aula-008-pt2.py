# Utilizando a biblioteca random para gerar números aleatórios

import random

num = random.random()  # gera um número aleatório, float entre 0 e 1

print(f'O número aleatório entre 0 e 1 é: {num :.2f}')

num2 = random.randint(1, 10)  # gera um int entre 1 e 10

print(f'O número aleário entre 1 e 10 é: {num2}')
