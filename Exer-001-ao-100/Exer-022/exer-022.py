
nome = str(input('Qual seu nome completo? '))
lista = nome.split()

print('NOME EM MAIÚSCULAS: ', nome.upper())
print('nome em minúsculas: ', nome.lower())

nome = nome.replace(" ", "")

print('Total de letras em todo nome: ', len(nome))
print('Total de letras no primeiro nome: ', len(lista[0]))
