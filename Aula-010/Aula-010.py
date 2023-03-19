# Exemplo 1
print('Primeiro exemplo: \n')
nome = str(input('Qual seu nome? '))

if nome == 'Jones':
    print('Nome legal!')
print(f'Bom dia {nome}!')
print('Fim do Ex. 1 \n')

# Exemplo 2
print('Segundo exemplo: \n')
nome = str(input('Qual seu nome? '))

if nome == 'Jones':
    print('Nome legal!')
else:
    print('Seu nome é normal!')
print(f'Bom dia {nome}!')
print('Fim do Ex. 2 \n')

# Exemplo 3
print('Terceiro exemplo:')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua média é: {media :.2}')
if media >= 6.0:
    print('Aprovado!')
else:
    print('Reprovado!')
print('Fim do Ex. 3. \n')

# Exemplo 4
print('Quarto exemplo:')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Sua média é: {media :.2}')
print('PARABÉNS!' if media >= 6.0 else 'ESTUDE MAIS!')
print('Fim do Ex. 4\n')
