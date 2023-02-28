
from random import choice as ch  # Chama a função choice da biblioteca random
from time import sleep as sl  # Chama a função sleep da biblioteca time

import emoji

print('Programa para sortear um(a) aluno(a) para apagar o quadro!\n')

al1 = input('Digite o nome do 1º Aluno(a): ')
al2 = input('Digite o nome do 2º Aluno(a): ')
al3 = input('Digite o nome do 3º Aluno(a): ')
al4 = input('Digite o nome do 4º Aluno(a): ')

sorteado = [al1, al2, al3, al4]  # Cria uma lista com o nome dos alunos

print('O(A) aluno(a) sorteado(a) foi: ')
print(7 * ' ', '3...')  # imprimi 7 vezes um espaço vazio junto a str '3...'
sl(1)  # delay de 1 segundo
print(7 * ' ', '2...')
sl(1)
print(7 * ' ', '1...')
sl(1)

print(7 * ' ', f'{ch(sorteado)}!', end='')
print(emoji.emojize(':grin:', language='alias'))
