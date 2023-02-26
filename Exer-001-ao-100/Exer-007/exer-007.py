
print('Calculo de média entre duas notas.\n')

# Entrada de dados
nome = input('Olá aluno! Qual seu nome: ')
nota1 = float(input(f'Qual valor da primeira nota, {nome}? '))
nota2 = float(input('Valor da segunda nota? '))

media = (nota1 + nota2) / 2

print(f'\nNome do Aluno: {nome}.')
print(f'1º Nota: {nota1}.')
print(f'2º Nota: {nota2}.')
print(f'Média: {media :.2f}.')
