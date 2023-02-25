nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:_^20}!'.format(nome))
''' '{:_^20}' FAZ COM QUE O NOME SEJA IMPRIMIDO COM 20 UNDERLINES '_'
    NOS EXTREMOS DA VARIÁVEL NOME '''

# Outro Ex. para somar dois números
print('\nSomando dois números!')
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
print(f'A soma dos números informados vale {num1+num2}, {nome}!')

# Calculando entre dois valores multiplas operações
print(
    f'\nAgora {nome}, me informe abaixo mais outros dois valores'
    # Quebra de linha entre o print por limitação do Python
    'para fazer outras operações!')
num3 = int(input('Digite novo valor: '))
num4 = int(input('Digite mais outro valor para mostrar outras operações: '))
sub = num3 - num4
mult = num3 * num4
divi = num3 / num4
div_int = num3 // num4
pot = num3 ** num4


print(
    f'Subtração = {sub}\nMultiplicação = {mult}\n'
    f'Divisão = {divi :.2f},', end='')
# (end='') faz com que os dois prints fiquem juntos
# Outra forma
# print('A subtração = {} Multiplicação = {} e a Divisão {:.2f}'
#      .format(sub, mult, divi))
print(f' Divisão inteira = {div_int} e a Potência = {pot}')
