
from random import shuffle as sh

print('Sorteador apresentação de trabalhos!')

al1 = input('Nome do(a) 1º aluno(a): ')
al2 = input('Nome do(a) 2º aluno(a): ')
al3 = input('Nome do(a) 3º aluno(a): ')
al4 = input('Nome do(a) 4º aluno(a): ')

nomes = [al1, al2, al3, al4]

sh(nomes)

print(f'\nPrimeiro(a) aluno(a) a apresentar: {nomes[0]}!')
print(f'Segundo(a) aluno(a) a apresentar: {nomes[1]}!')
print(f'Terceiro(a) aluno(a) a apresentar: {nomes[2]}!')
print(f'O(A) último(a) aluno(a) a apresentar: {nomes[3]}!')
